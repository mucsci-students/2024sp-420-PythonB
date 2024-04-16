import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import math

from PIL import Image, ImageTk

from Models.uml_diagram import UML_Diagram
from Models.uml_class import UML_Class
from Models.uml_field import UML_Field
from Models.uml_method import UML_Method
from Models.uml_param import UML_Param
from Models.uml_relation import UML_Relation

class UML_Image:
    def __init__(self) -> None:
        pygame.init()
        self.line_height = 72
        self.letter_width = 20
        self.margin = 500
        self.background_color = (64, 64, 64)

        self._framebuffer = pygame.Surface((self.margin * 2, self.margin * 2))
        self._framebuffer.fill(self.background_color)

    def draw_framebuffer(self, diagram: UML_Diagram):
        left_border = 0
        right_border = 0
        top_border = 0
        bot_border = 0
        class_boxes = []
        class_rects = []
        for cls in diagram.get_all_classes():
            text_cls_width = len(cls.get_name()) * self.letter_width
            text_cls_height = self.line_height
            text_cls_height += 2 * self.line_height
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
            text_cls_height += self.line_height
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
        framebuffer = pygame.Surface((width, height))
        framebuffer.fill(self.background_color)
        font = pygame.font.Font(None, 36)
        # draw relationship arrows
        #TODO: self relationship
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
            m = direction[1] / direction[0] + 1e-11
            # y - y0 = m(x - x0)
            # x0 = src_center_x
            # y0 = src_center_y
            intersection = 0, 0
            dist = float('inf')
            # y = m(x - x0) + y0
            # left: x = dst_x
            y = m * (dst_x - src_center_x) + src_center_y
            if dst_y <= y <= dst_y + dst_height:
                temp = math.dist([src_center_x, src_center_y], [dst_x, y])
                if temp < dist:
                    dist = temp
                    intersection = dst_x, y
            # right: x = dst_x + dst_width
            y = m * (dst_x + dst_width - src_center_x) + src_center_y
            if dst_y <= y <= dst_y + dst_height:
                temp = math.dist([src_center_x, src_center_y], [dst_x + dst_width, y])
                if temp < dist:
                    dist = temp
                    intersection = dst_x + dst_width, y
            # x = (y - y0) / m + x0
            # top: y = dst_y
            x = (dst_y - src_center_y) / m + src_center_x
            if dst_x <= x <= dst_x + dst_width:
                temp = math.dist([src_center_x, src_center_y], [x, dst_y])
                if temp < dist:
                    dist = temp
                    intersection = x, dst_y
            # bot: y = dst_y + dst_height
            x = (dst_y + dst_height - src_center_y) / m + src_center_x
            if dst_x <= x <= dst_x + dst_width:
                temp = math.dist([src_center_x, src_center_y], [x, dst_y + dst_height])
                if temp < dist:
                    dist = temp
                    intersection = x, dst_y + dst_height
            # draw an arrow from src_center to intersection
            if rel.get_type() == 'Aggregation':
                self.__draw_aggregation(framebuffer, [src_center_x, src_center_y], intersection)
            elif rel.get_type() == 'Composition':
                self.__draw_composition(framebuffer, [src_center_x, src_center_y], intersection)
            elif rel.get_type() == 'Inheritance':
                self.__draw_inheritance(framebuffer, [src_center_x, src_center_y], intersection)
            elif rel.get_type() == 'Realization':
                self.__draw_realization(framebuffer, [src_center_x, src_center_y], intersection)
        # draw class boxes
        for cls_x, cls_y, cls_width, cls_height, cls_name, text_fields, text_methods in class_rects:
            curr = 1
            pygame.draw.rect(framebuffer, (200, 200, 200), ((cls_x + self.margin, cls_y + self.margin), (cls_width, cls_height)))
            text_surface = font.render(cls_name, True, (0, 0, 0))
            framebuffer.blit(text_surface, (cls_x + (cls_width - len(cls_name) * self.letter_width) // 2 + self.margin,
                                            cls_y + curr * self.line_height + self.margin))
            curr += 2
            for text_field in text_fields:
                text_surface = font.render(text_field, True, (0, 0, 0))
                framebuffer.blit(text_surface, (cls_x + (cls_width - len(text_field) * self.letter_width) // 2 + self.margin,
                                                cls_y + curr * self.line_height + self.margin))
                curr += 1
            for text_method in text_methods:
                text_surface = font.render(text_method, True, (0, 0, 0))
                framebuffer.blit(text_surface, (cls_x + (cls_width - len(text_method) * self.letter_width) // 2 + self.margin,
                                                cls_y + curr * self.line_height + self.margin))
                curr += 1

        self._framebuffer = framebuffer

        image = Image.frombytes('RGB', (width, height), pygame.image.tostring(framebuffer, 'RGB'))
        tk_image = ImageTk.PhotoImage(image)
        return tk_image, class_boxes
    
    def save_image(self, name: str):
        pygame.image.save(self._framebuffer, name)

    # helpers #

    def __vec(self, p1: list[int], p2: list[int]):
        return p2[0] - p1[0], p2[1] - p1[1]
    
    def __rotate(self, v, rad: float):
        return v[0] * math.cos(rad) - v[1] * math.sin(rad), v[0] * math.sin(rad) + v[1] * math.cos(rad)
    
    def __normalized(self, v):
        ac = 1e-11 + (v[0]**2 + v[1]**2)**0.5
        return v[0] / ac, v[1] / ac
    
    def __draw_diamond(self, framebuffer: pygame.Surface, start: list[int], end: list[int], color: str, side_length: int=30) -> None:
        orgin = self.__vec(start, end)
        left = self.__normalized(self.__rotate(orgin, -5 * math.pi / 6))
        right = self.__normalized(self.__rotate(orgin, 5 * math.pi / 6))
        p1 = end[0] + left[0] * side_length, end[1] + left[1] * side_length
        p2 = end[0] + right[0] * side_length, end[1] + right[1] * side_length
        v = self.__normalized(self.__vec(end, start))
        to = end[0] + v[0] * side_length * 3**0.5, end[1] + v[1] * side_length * 3**0.5
        pygame.draw.polygon(framebuffer, color, [end, p1, to, p2])

    def __draw_triangle(self, framebuffer: pygame.Surface, start: list[int], end: list[int], color: str, side_length: int=40) -> None:

        orgin = self.__vec(start, end)
        left = self.__normalized(self.__rotate(orgin, -5 * math.pi / 6))
        right = self.__normalized(self.__rotate(orgin, 5 * math.pi / 6))
        p1 = end[0] + left[0] * side_length, end[1] + left[1] * side_length
        p2 = end[0] + right[0] * side_length, end[1] + right[1] * side_length
        pygame.draw.polygon(framebuffer, color, [end, p1, p2])
    
    def __draw_aggregation(self, framebuffer: pygame.Surface, start: list[int], end: list[int]) -> None:
        # line with white diamond
        pygame.draw.line(framebuffer, (0, 0, 0), start, end, 5)
        self.__draw_diamond(framebuffer, start, end, (255, 255, 255))

    def __draw_composition(self, framebuffer: pygame.Surface, start: list[int], end: list[int]) -> None:
        # line with solid diamond
        pygame.draw.line(framebuffer, (0, 0, 0), start, end, 5)
        self.__draw_diamond(framebuffer, start, end, (0, 0, 0))

    def __draw_inheritance(self, framebuffer: pygame.Surface, start: list[int], end: list[int]) -> None:
        # line with white triangle
        pygame.draw.line(framebuffer, (0, 0, 0), start, end, 5)
        self.__draw_triangle(framebuffer, start, end, (255, 255, 255))

    def __draw_realization(self, framebuffer: pygame.Surface, start: list[int], end: list[int]) -> None:
        # dash line with white triangle
        #TODO: dash line
        pygame.draw.line(framebuffer, (0, 0, 0), start, end, 5)
        self.__draw_triangle(framebuffer, start, end, (255, 255, 255))