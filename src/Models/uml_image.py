import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

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

    def draw_framebuffer(self, diagram: UML_Diagram):
        left_border = 0
        right_border = 0
        top_border = 0
        bot_border = 0
        class_rects = []
        for cls in diagram.get_all_classes():
            text_cls_width = len(cls.get_name()) * self.letter_width
            text_cls_height = self.line_height
            text_cls_height += 2 * self.line_height
            text_fields = []
            for field in cls.get_fields():
                text_field = ' '.join([field.get_type(), field.get_name()])
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
        framebuffer.fill((64, 64, 64))
        font = pygame.font.Font(None, 36)
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
        relations = [[rel.get_src().get_position(), rel.get_dst().get_position(), rel.get_type()] for rel in diagram.get_all_relations()]
        pygame.image.save(framebuffer, "framebuffer_image.png")

        image = Image.frombytes('RGB', (width, height), pygame.image.tostring(framebuffer, 'RGB'))
        tk_image = ImageTk.PhotoImage(image)
        return tk_image