from ..Models.uml_diagram import UML_Diagram
from ..Models.uml_class import UML_Class
from ..Models.uml_relation import UML_Relation

def test_ctor_dia():
    dia = UML_Diagram()
    assert dia
    assert isinstance(dia, UML_Diagram)

def test_add_class():
    dia = UML_Diagram()
    bender = UML_Class("Bender Bending Rodriguez")
    
    assert len(dia.get_all_classes()) == 0
    dia.add_class("Bender Bending Rodriguez")
    assert dia._classes[0].get_name() == bender.get_name()
    assert len(dia.get_all_classes()) == 1

def test_add_relation():
    dia = UML_Diagram()

    bender = UML_Class("Bender Bending Rodriguez")
    dia.add_class("Bender Bending Rodriguez")
    fry = UML_Class("Philip J. Fry")
    dia.add_class("Philip J. Fry")
    
    frender = UML_Relation(bender, fry, "composition")
    assert len(dia.get_all_relations()) == 0
    dia.add_relation("Bender Bending Rodriguez", "Philip J. Fry", "composition")
    assert len(dia._relations) == 1
    assert dia._relations[0].get_src_name() == "Bender Bending Rodriguez"
    assert dia._relations[0].get_dst_name() == "Philip J. Fry"

def test_get_class():
    dia = UML_Diagram()
    bender = UML_Class("Bender Bending Rodriguez")
    fry = UML_Class("Philip J. Fry")
    dia.add_class("Bender Bending Rodriguez")
    dia.add_class("Philip J. Fry")
    
    class_gotten = dia.get_class("Bender Bending Rodriguez")
    assert str(class_gotten) == str(bender)
    assert str(class_gotten) != str(fry)
    
    class_gotten = dia.get_class("Philip J. Fry")
    assert str(class_gotten) != str(bender)
    assert str(class_gotten) == str(fry)

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
    assert str(get_frender) == str(frender)
    assert str(get_a_winning_combination) == str(a_winning_combination)
    assert get_frender != a_winning_combination
    assert get_a_winning_combination != frender

def test_get_all_classes():
    dia = UML_Diagram()
    bender = UML_Class("Bender")
    fry = UML_Class("Fry")
    leela = UML_Class("Leela")

    dia.add_class("Bender")
    dia.add_class("Fry")
    dia.add_class("Leela")
    
    crew = dia.get_all_classes()
    assert len(crew) == 3
    assert str(crew[0]) == str(bender)
    assert str(crew[1]) == str(fry)
    assert str(crew[2]) == str(leela)


def test_get_relations():
    dia = UML_Diagram()
    bender = UML_Class("Bender")
    fry = UML_Class("Fry")
    leela = UML_Class("Leela")
     
    dia.add_class("Bender")
    dia.add_class("Fry")
    dia.add_class("Leela")
    dia.add_class("Zoiberg")

    friend1 = UML_Relation(bender, fry, "generalization")
    friend2 = UML_Relation(fry, leela, "inheritance")
    friend3 = UML_Relation(bender, leela, "aggregation")

    dia.add_relation("Bender", "Fry", "generalization")
    dia.add_relation("Fry", "Leela", "inheritance")
    dia.add_relation("Bender", "Leela", "aggregation")

    get_crew = dia.get_all_relations()
    assert len(get_crew) == 3
    assert str(get_crew[0]) == str(friend1)
    assert str(get_crew[1]) == str(friend2)
    assert str(get_crew[2]) == str(friend3)

def test_delete_class():
    dia = UML_Diagram()
    bender = UML_Class("Bender")
    dia.add_class("Bender")

    assert next((str(v) for v in dia._classes if str(v) == str(bender)), False)
    dia.delete_class("Bender")
    assert next((str(v) for v in dia._classes if str(v) == str(bender)), True)

def test_add_multiple_delete_one_class():
    dia = UML_Diagram()
    bender = UML_Class("Bender")
    fry = UML_Class("Fry")
    dia.add_class("Bender")
    dia.add_class("Fry")

    assert next((str(v) for v in dia._classes if str(v) == str(bender)), False)
    assert next((str(v) for v in dia._classes if str(v) == str(fry)), False)
    dia.delete_class("Bender")
    assert next((str(v) for v in dia._classes if str(v) == str(bender)), True)
    assert next((str(v) for v in dia._classes if str(v) == str(fry)), False)

def test_delete_relation():
    dia = UML_Diagram()
    bender = UML_Class("Bender")
    fry = UML_Class("Fry")
    dia.add_class("Bender")
    dia.add_class("Fry")
    frender = UML_Relation(bender, fry, "aggregation")

    dia.add_relation("Bender", "Fry", "aggregation")
    
    assert str(dia._relations[0]) == str(frender)
    dia.delete_relation("Bender", "Fry")
    assert len(dia._relations) == 0

def test_delete_relations_containing():
    dia = UML_Diagram()
    bender = UML_Class("Bender")
    fry = UML_Class("Fry")
    zoidberg = UML_Class("Zoidberg")

    dia.add_class("Bender")
    dia.add_class("Fry")
    dia.add_class("Zoidberg")

    friends1 = UML_Relation(bender, fry, "aggregation")
    friends3 = UML_Relation(bender, zoidberg, "aggregation")
    friends4 = UML_Relation(fry, zoidberg, "aggregation")

    dia.add_relation("Bender", "Fry", "aggregation")
    dia.add_relation("Bender", "Zoidberg", "aggregation")
    dia.add_relation("Fry", "Zoidberg", "aggregation")

    rels = dia.get_all_relations()
    assert len(rels) == 3
    assert len(rels) != 16
    assert str(rels[0]) == str(friends1) 
    assert str(rels[1]) == str(friends3)
    assert str(rels[2]) == str(friends4)
    
    dia.delete_relations_containing("Zoidberg")

    rels = dia.get_all_relations()
    assert len(rels) == 1
    assert str(rels[0]) == str(friends1)

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
