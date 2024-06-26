from Models.uml_diagram import UML_Diagram
from Models.uml_image import UML_Image

def test_create_image_for_gui():
    dgm1 = UML_Diagram()
    dgm1.add_class('Class1')
    cls1 = dgm1.get_class('Class1')
    cls1._position[0] = 0
    cls1._position[1] = 0
    dgm1.add_class('Class2')
    cls2 = dgm1.get_class('Class2')
    cls2._position[0] = 100
    cls2._position[1] = 0
    cls2.add_field('Field1', 'string')
    cls2.add_field('Field2', 'int')
    dgm1.add_class('Class3')
    cls3 = dgm1.get_class('Class3')
    cls3._position[0] = -100
    cls3._position[1] = 0
    cls3.add_method('Method1', 'string')
    cls3.add_method('Method2', 'int', 'Param1')
    cls3.add_method('Method3', 'void', 'Param1', 'Param2')
    dgm1.add_class('Class4')
    cls4 = dgm1.get_class('Class4')
    cls4._position[0] = 0
    cls4._position[1] = 100
    cls4.add_field('Field1', 'string')
    cls4.add_field('Field2', 'int')
    cls4.add_method('Method1', 'string')
    cls4.add_method('Method2', 'int', 'Param1')
    cls4.add_method('Method3', 'void', 'Param1', 'Param2')
    dgm1.add_relation('Class1', 'Class2', 'Aggregation')
    dgm1.add_relation('Class1', 'Class3', 'Realization')
    dgm1.add_relation('Class1', 'Class4', 'Inheritance')
    dgm1.add_relation('Class2', 'Class1', 'Composition')
    dgm1.add_relation('Class1', 'Class1', 'Aggregation')
    dgm1.add_relation('Class2', 'Class2', 'Composition')
    dgm1.add_relation('Class3', 'Class3', 'Inheritance')
    dgm1.add_relation('Class4', 'Class4', 'Realization')

    image = UML_Image()
    image.draw_framebuffer(dgm1, [0, 0], [1000, 800])
    image.draw_framebuffer(dgm1, [0, 0], [1920, 1080])

def test_export_image():
    dgm1 = UML_Diagram()
    dgm1.add_class('Class1')
    cls1 = dgm1.get_class('Class1')
    dgm1.add_class('Class2')
    cls2 = dgm1.get_class('Class2')
    cls2.add_field('Field1', 'string')
    cls2.add_field('Field2', 'int')
    dgm1.add_class('Class3')
    cls3 = dgm1.get_class('Class3')
    cls3.add_method('Method1', 'string')
    cls3.add_method('Method2', 'int', 'Param1')
    cls3.add_method('Method3', 'void', 'Param1', 'Param2')
    dgm1.add_class('Class4')
    cls4 = dgm1.get_class('Class4')
    cls4.add_field('Field1', 'string')
    cls4.add_field('Field2', 'int')
    cls4.add_method('Method1', 'string')
    cls4.add_method('Method2', 'int', 'Param1')
    cls4.add_method('Method3', 'void', 'Param1', 'Param2')
    dgm1.add_relation('Class1', 'Class2', 'Aggregation')
    dgm1.add_relation('Class2', 'Class1', 'composition')

    image = UML_Image()
    image.save_image(dgm1)