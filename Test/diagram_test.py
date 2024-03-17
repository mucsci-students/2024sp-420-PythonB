from Models.uml_diagram import UML_Diagram
from Models.uml_class import UML_Class
from Models.uml_relation import UML_Relation

def test_ctor_dia():
    dia = UML_Diagram()
    assert dia
    assert isinstance(dia, UML_Diagram)

def test_add_class():
    dia = UML_Diagram()
    bender = UML_Class("Bender Bending Rodriguez")
    
    assert bender not in dia._classes
    dia.add_class("Bender Bending Rodriguez")
    assert bender in dia._classes

def test_add_relation():
    dia = UML_Diagram()
    bender = UML_Class("Bender Bending Rodriguez")
    dia.add_class("Bender Bending Rodriguez")
    fry = UML_Class("Philip J. Fry")
    dia.add_class("Philip J. Fry")
    
    frender = UML_Relation(bender, fry, "composition")
    assert frender not in dia._relations
    dia.add_relation("Bender Bending Rodriguez", "Philip J. Fry", "composition")
    assert frender in dia._relations

def test_get_class():
    dia = UML_Diagram()
    bender = UML_Class("Bender Bending Rodriguez")
    fry = UML_Class("Philip J. Fry")
    dia.add_class("Bender Bending Rodriguez")
    dia.add_class("Philip J. Fry")
    
    class_gotten = dia.get_class("Bender Bending Rodriguez")
    assert class_gotten == bender
    assert class_gotten != fry
    
    class_gotten = dia.get_class("Philip J. Fry")
    assert class_gotten != bender
    assert class_gotten == fry

def test_get_relation():
    dia = UML_Diagram()
    bender = UML_Class("Bender Bending Rodriguez")
    dia.add_class("Bender Bending Rodriguez")
    fry = UML_Class("Philip J. Fry")
    dia.add_class("Philip J. Fry")
    
    frender = UML_Relation(bender, fry, "composition")
    a_winning_combination = UML_Relation(fry, bender, "aggregation")
    
    dia.add_relation("Bender Bending Rodriguez", "Philip J. Fry", "composition")
    dia.add_relation("Philip J. Fry", "Bender Bending Rodriguez", "aggregation")
    
    get_frender = dia.get_relation("Bender Bending Rodriguez", "Philip J. Fry")
    get_a_winning_combination = dia.get_relation("Philip J. Fry", "Bender Bending Rodriguez")
    assert get_frender == frender
    assert get_a_winning_combination == a_winning_combination
    assert get_frender != a_winning_combination
    assert get_a_winning_combination != frender

def test_get_all_classes():
    dia = UML_Diagram()
    bender = UML_Class("Bender")
    fry = UML_Class("Fry")
    leela = UML_Class("Leela")
    zoidberg = UML_Class("Zoidberg")

    dia.add_class("Bender")
    dia.add_class("Fry")
    dia.add_class("Leela")
    
    list1 = [bender, fry, leela]
    list2 = [bender, fry, leela, zoidberg]
    
    crew = dia.get_all_classes()
    assert crew == list1
    assert crew != list2

def test_get_relations():
    dia = UML_Diagram()
    bender = UML_Class("Bender")
    fry = UML_Class("Fry")
    leela = UML_Class("Leela")
    zoidberg = UML_Class("Zoidberg")
     
    dia.add_class("Bender")
    dia.add_class("Fry")
    dia.add_class("Leela")
    dia.add_class("Zoiberg")

    friend1 = UML_Relation(bender, fry, "generalization")
    friend2 = UML_Relation(fry, leela, "inheritance")
    friend3 = UML_Relation(bender, leela, "aggregation")
    friend4 = UML_Relation(fry, zoidberg, "aggregation")

    dia.add_relation("Bender", "Fry", "generalization")
    dia.add_relation("Fry", "Leela", "inheritance")
    dia.add_relation("Bender", "Leela" "aggregation")

    list1 = [friend1, friend2, friend3]
    list2 = [friend1, friend2, friend4]

    get_crew = dia.get_all_relations()
    assert get_crew == list1
    assert get_crew != list2

def test_delete_class():
    dia = UML_Diagram()
    bender = UML_Class("Bender")
    dia.add_class("Bender")

    assert bender in dia._classes
    dia.delete_class("Bender")
    assert bender not in dia._classes

def test_add_multiple_delete_one_class():
    dia = UML_Diagram()
    bender = UML_Class("Bender")
    fry = UML_Class("Fry")
    dia.add_class("Bender")
    dia.add_class("Fry")

    assert bender in dia._classes
    assert fry in dia._classes
    dia.delete_class("Bender")
    assert bender not in dia._classes
    assert fry in dia._classes

def test_delete_relation():
    dia = UML_Diagram()
    bender = UML_Class("Bender")
    fry = UML_Class("Fry")
    dia.add_class("Bender")
    dia.add_class("Fry")
    frender = UML_Relation(bender, fry, "aggregation")

    dia.add_relation("Bender", "Fry", "aggregation")
    
    assert frender in dia._relations
    dia.delete_relation("Bender", "Fry")
    assert frender not in dia._relations

def test_delete_relations_containing():
    dia = UML_Diagram()
    bender = UML_Class("Bender")
    fry = UML_Class("Fry")
    zoidberg = UML_Class("Zoidberg")

    dia.add_class("Bender")
    dia.add_class("Fry")
    dia.add_class("Zoidberg")

    friends1 = UML_Relation(bender, fry, "aggregation")
    friends2 = UML_Relation(fry, bender, "aggregation")
    friends3 = UML_Relation(bender, zoidberg, "aggregation")
    friends4 = UML_Relation(fry, zoidberg, "aggregation")

    dia.add_relation("Bender", "Fry", "aggregation")
    dia.add_relation("Fry", "Bender", "aggregation")
    dia.add_relation("Bender", "Zoidberg", "aggregation")
    dia.add_relation("Fry", "Zoidberg", "aggregation")

    list1 = [friends1, friends2, friends3, friends4]
    list2 = [friends1, friends2]

    assert dia.get_all_relations() == list1
    assert dia.get_all_relations() != list2

    dia.delete_relations_containing("Zoidberg")

    assert dia.get_all_relations != list1
    assert dia.get_all_relations == list2

#TODO: Remove this test if we make diagram Singleton
def test_equals():
    dia = UML_Diagram()
    class1 = UML_Class("Bender")
    dia.add_class("Bender")

    dia2 = UML_Diagram()
    class2 = UML_Class("Fry")
    dia2.add_class("Fry")

    assert dia != class1
    assert dia == dia
    assert dia2 != class2
    assert dia2 == dia2
    assert dia != dia2
