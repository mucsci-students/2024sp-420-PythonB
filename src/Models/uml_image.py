import math

from PIL import Image, ImageDraw, ImageFont

from Models.uml_diagram import UML_Diagram

class UML_Image:
    def __init__(self) -> None:
        self.line_height = 30
        self.letter_width = 8
        self.margin = 250
        self.background_color = (100, 100, 100)
        self.font_size = 15
        self.header_font_size = 20
        self._viewport_width = 1000
        self._viewport_height = 800
        self._image = Image.new("RGB", (self._viewport_width, self._viewport_height), self.background_color)
        self._draw = ImageDraw.Draw(self._image)
        self.font = ImageFont.truetype("Anonymous Pro.ttf", self.font_size)  # Regular for fields and methods
        self.header_font = ImageFont.truetype("Anonymous Pro B.ttf", self.header_font_size)  # Bold for class name

    def draw_framebuffer(self, diagram: UML_Diagram, camera_pos: tuple[int, int], viewport_size: tuple[int, int]):
        class_boxes, class_rects, _, _ = self.__generate_class_boxes_and_class_rects_and_boarders(diagram)
        if viewport_size[0] != self._viewport_width or viewport_size[1] != self._viewport_height:
            self._viewport_width, self._viewport_height = viewport_size
            self._image = Image.new("RGB", viewport_size, self.background_color)
            self._draw = ImageDraw.Draw(self._image)
        # reset background
        self._draw.rectangle([0, 0, self._viewport_width, self._viewport_height], fill=self.background_color)
        # move camera
        for class_rect in class_rects:
            class_rect[0] -= camera_pos[0]
            class_rect[0] -= self.margin
            class_rect[1] -= camera_pos[1]
            class_rect[1] -= self.margin
        # draw relationship arrows
        self.__draw_relationship_arrows(self._draw, diagram, class_rects)
        # draw class boxes
        self.__draw_class_boxes(self._draw, class_rects)
        return self._image, class_boxes
    
    def save_image(self, diagram: UML_Diagram) -> Image:
        _, class_rects, width, height = self.__generate_class_boxes_and_class_rects_and_boarders(diagram)
        image = Image.new("RGB", (width, height), self.background_color)
        draw = ImageDraw.Draw(image)
        draw.rectangle([0, 0, width, height], fill=self.background_color)
        # draw relationship arrows
        self.__draw_relationship_arrows(draw, diagram, class_rects)
        # draw class boxes
        self.__draw_class_boxes(draw, class_rects)
        return image

    ############################################## helpers ################################################

    def __generate_class_boxes_and_class_rects_and_boarders(self, diagram: UML_Diagram):
        left_border = 0
        right_border = 0
        top_border = 0
        bot_border = 0
        class_boxes = []
        class_rects = []
        for cls in diagram.get_all_classes():
            text_cls_width = len(cls.get_name()) * (1.75 * self.letter_width)
            text_cls_height = self.line_height
            text_fields = []
            for field in cls.get_fields():
                text_field = '{} {}'.format(field.get_type(), field.get_name())
                text_fields.append(text_field)
                text_cls_width = max(text_cls_width, len(text_field) * self.letter_width)
                text_cls_height += self.line_height
            text_methods = []
            for method in cls.get_methods():
                # ret name(param1, param2, param3)
                text_method = '{} {}({})'.format(method.get_ret(), method.get_name(), ', '.join(param.get_name() for param in method.get_params()))
                text_methods.append(text_method)
                text_cls_width = max(text_cls_width, len(text_method) * self.letter_width)
                text_cls_height += self.line_height
            #padding
            text_cls_width += 5 * self.letter_width
            #text_cls_height += self.line_height
            left_border = min(left_border, cls.get_position_x())
            right_border = max(right_border, cls.get_position_x() + text_cls_width)
            top_border = min(top_border, cls.get_position_y())
            bot_border = max(bot_border, cls.get_position_y() + text_cls_height)
            class_rects.append([cls.get_position_x(), cls.get_position_y(), text_cls_width, text_cls_height, cls.get_name(), text_fields, text_methods])
            # GUI use
            class_box = {}; class_boxes.append(class_box)
            class_box['name'] = cls.get_name()
            class_box['x'] = cls.get_position_x()
            class_box['y'] = cls.get_position_y()
            class_box['width'] = text_cls_width
            class_box['height'] = text_cls_height
            class_box['fields'] = [field.get_name() for field in cls.get_fields()]
            class_box['methods'] = {}
            for method in cls.get_methods():
                class_box['methods'][method.get_name()] = [param.get_name() for param in method.get_params()]
        # margin
        left_border -= self.margin
        right_border += self.margin
        top_border -= self.margin
        bot_border += self.margin

        width = right_border - left_border
        height = bot_border - top_border
        #padding
        width += 3 * self.letter_width
        height += 2 * self.line_height
        return class_boxes, class_rects, width, height

    def __draw_relationship_arrows(self, draw: ImageDraw.ImageDraw, diagram: UML_Diagram, class_rects) -> None:
        for rel in diagram.get_all_relations():
            for rect in class_rects:
                if rect[4] == rel.get_src_name():
                    src_x, src_y, src_width, src_height, _, _, _ = rect
                    src_x += self.margin
                    src_y += self.margin
                elif rect[4] == rel.get_dst_name():
                    dst_x, dst_y, dst_width, dst_height, _, _, _ = rect
                    dst_x += self.margin
                    dst_y += self.margin
            #self relationship
            if rel.get_src_name() == rel.get_dst_name():
                radius = 0.5 * min(src_width, src_height)
                #bounding(left, top, right, bottom)
                bbox = src_x - radius, src_y - radius, src_x + radius, src_y + radius
                # draw line
                if rel.get_type() == 'Realization':
                    segment_count = 40
                    delta_angle = 360 / segment_count
                    for i in range(0, segment_count, 2):
                        start_angle = i * delta_angle
                        end_angle = (i + 1) * delta_angle
                        draw.arc(bbox, start_angle, end_angle, fill=(0, 0, 0), width=5)
                    # draw arrow
                    self.__draw_triangle(draw, [src_x - radius, src_y + radius - 5], [src_x, src_y + radius - 5], (255, 255, 255))
                else:
                    draw.arc(bbox, 0, 360, fill=(0, 0, 0), width=5)
                    # draw arrow
                    if rel.get_type() == 'Aggregation':
                        self.__draw_diamond(draw, [src_x - radius, src_y + radius - 5], [src_x, src_y + radius - 5], (255, 255, 255))
                    elif rel.get_type() == 'Composition':
                        self.__draw_diamond(draw, [src_x - radius, src_y + radius - 5], [src_x, src_y + radius - 5], (0, 0, 0))
                    elif rel.get_type() == 'Inheritance':
                        self.__draw_triangle(draw, [src_x - radius, src_y + radius - 5], [src_x, src_y + radius - 5], (255, 255, 255))
                continue
            # from
            src_center_x = (src_x + src_x + src_width) // 2
            src_center_y = (src_y + src_y + src_height) // 2
            # target
            dst_center_x = (dst_x + dst_x + dst_width) // 2
            dst_center_y = (dst_y + dst_y + dst_height) // 2
            # direction
            direction = self.__vec([src_center_x, src_center_y], [dst_center_x, dst_center_y])
            # slope
            # m = dy / dx
            m = direction[1] / (direction[0] + 1e-11) + 1e-11
            # y - y0 = m(x - x0)
            # x0 = src_center_x
            # y0 = src_center_y
            intersection = [0, 0]
            dist = float('inf')
            data = [dist, intersection]
            # y = m(x - x0) + y0
            # left: x = dst_x
            y = m * (dst_x - src_center_x) + src_center_y
            if dst_y <= y <= dst_y + dst_height:
                self.__update_intersection([src_center_x, src_center_y], [dst_x, y], data)
            # right: x = dst_x + dst_width
            y = m * (dst_x + dst_width - src_center_x) + src_center_y
            if dst_y <= y <= dst_y + dst_height:
                self.__update_intersection([src_center_x, src_center_y], [dst_x + dst_width, y], data)
            # x = (y - y0) / m + x0
            # top: y = dst_y
            x = (dst_y - src_center_y) / m + src_center_x
            if dst_x <= x <= dst_x + dst_width:
                self.__update_intersection([src_center_x, src_center_y], [x, dst_y], data)
            # bot: y = dst_y + dst_height
            x = (dst_y + dst_height - src_center_y) / m + src_center_x
            if dst_x <= x <= dst_x + dst_width:
                self.__update_intersection([src_center_x, src_center_y], [x, dst_y + dst_height], data)
            # draw an arrow from src_center to intersection
            if rel.get_type() == 'Aggregation':
                self.__draw_aggregation(draw, [src_center_x, src_center_y], data[1])
            elif rel.get_type() == 'Composition':
                self.__draw_composition(draw, [src_center_x, src_center_y], data[1])
            elif rel.get_type() == 'Inheritance':
                self.__draw_inheritance(draw, [src_center_x, src_center_y], data[1])
            elif rel.get_type() == 'Realization':
                self.__draw_realization(draw, [src_center_x, src_center_y], data[1])

    def __update_intersection(self, start: list[int], end: list[int], data: list[float | list[int]]) -> None:
        temp = math.dist(start, end)
        if temp < data[0]:
            data[0] = temp
            data[1][0] = end[0]
            data[1][1] = end[1]

    def __draw_class_boxes(self, draw: ImageDraw.ImageDraw, class_rects) -> None:
        for cls_x, cls_y, cls_width, cls_height, cls_name, text_fields, text_methods in class_rects:
            border_color = (0, 0, 0)
            border_thickness = 2
            
            draw.rectangle([cls_x + self.margin, cls_y + self.margin, cls_x + cls_width + self.margin, cls_y + cls_height + self.margin],
                           outline=border_color, fill=(200, 200, 200), width=border_thickness)
            curr = 0

            # Text formatting
            class_font = self.header_font
            regular_font = self.font

            draw.text((cls_x +(cls_width - len(cls_name) * self.letter_width) // 2 + self.margin, cls_y + curr * self.line_height + self.margin),
                      cls_name, fill=(0, 0, 0), font=class_font)
            curr += 1
            draw.line([cls_x + self.margin, cls_y + curr * self.line_height + self.margin - 10,
                       cls_x + cls_width + self.margin, cls_y + curr * self.line_height + self.margin - 10], fill=(0, 0, 0), width=2)
            for text_field in text_fields:
                draw.text((cls_x + (cls_width - len(text_field) * self.letter_width) // 2 + self.margin, cls_y + curr * self.line_height + self.margin),
                      text_field, fill=(0, 0, 0), font=regular_font)
                curr += 1
            draw.line([cls_x + self.margin, cls_y + curr * self.line_height + self.margin - 10,
                    cls_x + cls_width + self.margin, cls_y + curr * self.line_height + self.margin - 10], fill=(0, 0, 0), width=2)
            for text_method in text_methods:
                draw.text((cls_x + (cls_width - len(text_method) * self.letter_width) // 2 + self.margin, cls_y + curr * self.line_height + self.margin),
                      text_method, fill=(0, 0, 0), font=regular_font)
                curr += 1

    def __vec(self, p1: list[int], p2: list[int]):
        return p2[0] - p1[0], p2[1] - p1[1]
    
    def __rotate(self, v, rad: float):
        return v[0] * math.cos(rad) - v[1] * math.sin(rad), v[0] * math.sin(rad) + v[1] * math.cos(rad)
    
    def __normalized(self, v):
        ac = 1e-11 + (v[0]**2 + v[1]**2)**0.5
        return v[0] / ac, v[1] / ac
    
    def __add(self, v1, v2):
        return v1[0] + v2[0], v1[1] + v2[1]

    def __multiply(self, v, x):
        return v[0] * x, v[1] * x
    
    def __draw_diamond(self, draw: ImageDraw.ImageDraw, start: list[int], end: list[int], color: tuple[int, int, int], side_length: int=30) -> None:
        orgin = self.__vec(start, end)
        left = self.__normalized(self.__rotate(orgin, -5 * math.pi / 6))
        right = self.__normalized(self.__rotate(orgin, 5 * math.pi / 6))
        p1 = end[0] + left[0] * side_length, end[1] + left[1] * side_length
        p2 = end[0] + right[0] * side_length, end[1] + right[1] * side_length
        v = self.__normalized(self.__vec(end, start))
        to = end[0] + v[0] * side_length * 3**0.5, end[1] + v[1] * side_length * 3**0.5
        draw.polygon([*end, *p1, *to, *p2], fill=color)

    def __draw_triangle(self, draw: ImageDraw.ImageDraw, start: list[int], end: list[int], color: tuple[int, int, int], side_length: int=40) -> None:
        orgin = self.__vec(start, end)
        left = self.__normalized(self.__rotate(orgin, -5 * math.pi / 6))
        right = self.__normalized(self.__rotate(orgin, 5 * math.pi / 6))
        p1 = end[0] + left[0] * side_length, end[1] + left[1] * side_length
        p2 = end[0] + right[0] * side_length, end[1] + right[1] * side_length
        draw.polygon([*end, *p1, *p2], fill=color)
    
    def __draw_aggregation(self, draw: ImageDraw.ImageDraw, start: list[int], end: list[int]) -> None:
        # line with white diamond
        draw.line([*start, *end], fill=(0, 0, 0), width=5)
        self.__draw_diamond(draw, start, end, (255, 255, 255))

    def __draw_composition(self, draw: ImageDraw.ImageDraw, start: list[int], end: list[int]) -> None:
        # line with solid diamond
        draw.line([*start, *end], fill=(0, 0, 0), width=5)
        self.__draw_diamond(draw, start, end, (0, 0, 0))

    def __draw_inheritance(self, draw: ImageDraw.ImageDraw, start: list[int], end: list[int]) -> None:
        # line with white triangle
        draw.line([*start, *end], fill=(0, 0, 0), width=5)
        self.__draw_triangle(draw, start, end, (255, 255, 255))

    def __draw_realization(self, draw: ImageDraw.ImageDraw, start: list[int], end: list[int]) -> None:
        # dash line with white triangle
        delta_len = 10
        segment_count = int(math.dist(start, end) / delta_len)
        direction = self.__normalized(self.__vec(start, end))
        for i in range(0, segment_count, 2):
            draw.line([*self.__add(start, self.__multiply(direction, i * delta_len)), *self.__add(start, self.__multiply(direction, (i + 1) * delta_len))],
                      fill=(0, 0, 0), width=5)
        self.__draw_triangle(draw, start, end, (255, 255, 255))