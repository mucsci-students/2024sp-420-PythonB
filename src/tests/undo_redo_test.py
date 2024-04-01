from Models.uml_undo_redo import UML_States
from Models.uml_diagram import UML_Diagram

def test_save_state():
    dgm0 = UML_Diagram()

    states = UML_States(dgm0) # at dgm0
    # inital state is correct
    assert states.get_current_state() is not dgm0
    assert states.get_current_state() == dgm0

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

    states.save_state(dgm1) # at dgm1
    # saved state is correct
    assert states.get_current_state() is not dgm1
    assert states.get_current_state() == dgm1

def test_undo():
    dgm0 = UML_Diagram()

    states = UML_States(dgm0) # at dgm0

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

    states.save_state(dgm1) # at dgm1

    dgm2 = UML_Diagram()
    dgm2.add_class('Class1')

    states.save_state(dgm2) # at dgm2

    undo_dgm1 = states.undo() # at dgm1
    # undo to previous state
    assert states.get_current_state() == undo_dgm1
    assert undo_dgm1 is not dgm1
    assert undo_dgm1 == dgm1

    undo_dgm0 = states.undo() # at dgm0
    # undo to previous state
    assert states.get_current_state() == undo_dgm0
    assert undo_dgm0 is not dgm0
    assert undo_dgm0 == dgm0

    undo_dgm0 = states.undo() # at dgm0
    # undo when out of bounds
    assert states.get_current_state() == undo_dgm0
    assert undo_dgm0 is not dgm0
    assert undo_dgm0 == dgm0

def test_redo():
    dgm0 = UML_Diagram()

    states = UML_States(dgm0) # at dgm0

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

    states.save_state(dgm1) # at dgm1

    dgm2 = UML_Diagram()
    dgm2.add_class('Class1')

    states.save_state(dgm2) # at dgm2

    undo_dgm1 = states.undo() # at dgm1
    undo_dgm0 = states.undo() # at dgm0

    redo_dgm1 = states.redo() # at dgm1
    # redo to next state
    assert states.get_current_state() == redo_dgm1
    assert redo_dgm1 is not dgm1
    assert redo_dgm1 == dgm1

    redo_dgm2 = states.redo() # at dgm2
    # redo to next state
    assert states.get_current_state() == redo_dgm2
    assert redo_dgm2 is not dgm2
    assert redo_dgm2 == dgm2

    redo_dgm2 = states.redo() # at dgm2
    # redo when out of bounds
    assert states.get_current_state() == redo_dgm2
    assert redo_dgm2 is not dgm2
    assert redo_dgm2 == dgm2

    undo_dgm1 = states.undo() # at dgm1

    dgm3 = UML_Diagram()
    dgm3.add_class('Class1')
    dgm3.add_class('Class2')
    dgm3.add_relation('Class1', 'Class2', 'Aggregation')

    states.save_state(dgm3) # at dgm3, dgm2 is deleted
    # saved state is correct
    assert states.get_current_state() is not dgm3
    assert states.get_current_state() == dgm3

    redo_dgm3 = states.redo() # at dgm3
    # redo when out of bounds
    assert states.get_current_state() == redo_dgm3
    assert redo_dgm3 is not dgm3
    assert redo_dgm3 == dgm3

    undo_dgm1 = states.undo() # at dgm1
    # undo to previous state
    assert states.get_current_state() == undo_dgm1
    assert undo_dgm1 is not dgm1
    assert undo_dgm1 == dgm1

    undo_dgm0 = states.undo() # at dgm0
    # undo to previous state
    assert states.get_current_state() == undo_dgm0
    assert undo_dgm0 is not dgm0
    assert undo_dgm0 == dgm0

    undo_dgm0 = states.undo() # at dgm0
    # undo when out of bounds
    assert states.get_current_state() == undo_dgm0
    assert undo_dgm0 is not dgm0
    assert undo_dgm0 == dgm0

def test_singleton():
    dgm1 = UML_Diagram()
    states = UML_States(dgm1)
    dgm1.add_class("clTest")
    
    dgm2 = UML_Diagram()
    dgm2.add_class("cl1")

    states2 = UML_States(dgm2)
    states.save_state(dgm1)

    #if they were different objects, states would have one save and states2 would have 0
    assert states == states2
    assert states is states2