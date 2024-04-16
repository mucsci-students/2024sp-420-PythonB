from Models.uml_diagram import UML_Diagram
from Models.uml_class import UML_Class
from Models.uml_relation import UML_Relation

import pytest

def test_ctor_dia():
    dia = UML_Diagram()
    assert dia
    assert isinstance(dia, UML_Diagram)

def test_add_class():
    dia = UML_Diagram()
    bender = UML_Class("Bender Bending Rodriguez")
    assert len(dia.get_all_classes()) == 0
    dia.add_class("Bender Bending Rodriguez")
    assert dia._classes[0] == bender
    assert len(dia.get_all_classes()) == 1

def test_add_repeat_class():
    dia = UML_Diagram()

    dia.add_class("cl")
    assert len(dia.get_all_classes()) == 1
    
    with pytest.raises(ValueError) as VE:
        dia.add_class("cl")
    assert str(VE.value) == "Class cl already exists"
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

def test_invalid_relations():
    dia = UML_Diagram()
    dia.add_class("cl")
    dia.add_relation("cl", "cl", "Aggregation")

    assert len(dia.get_all_relations()) == 1

    with pytest.raises(ValueError) as VE:
        dia.add_relation("cl", "cl", "Composition")
    assert str(VE.value) == "Relation between cl and cl already exists"

    with pytest.raises(ValueError) as VE:
        dia.add_class("c2")
        dia.add_relation("cl", "c2", "badType")
    assert str(VE.value) == "Relation type badType is invalid"


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

    dia.add_class("Bender")
    dia.add_class("Fry")
    dia.add_class("Leela")
    
    crew = dia.get_all_classes()
    assert len(crew) == 3
    assert crew[0] == bender
    assert crew[1] == fry
    assert crew[2] == leela


def test_get_relations():
    dia = UML_Diagram()
    bender = UML_Class("Bender")
    fry = UML_Class("Fry")
    leela = UML_Class("Leela")
     
    dia.add_class("Bender")
    dia.add_class("Fry")
    dia.add_class("Leela")
    dia.add_class("Zoiberg")

    friend1 = UML_Relation(bender, fry, "Realization")
    friend2 = UML_Relation(fry, leela, "inheritance")
    friend3 = UML_Relation(bender, leela, "aggregation")

    dia.add_relation("Bender", "Fry", "Realization")
    dia.add_relation("Fry", "Leela", "inheritance")
    dia.add_relation("Bender", "Leela", "aggregation")

    get_crew = dia.get_all_relations()
    assert len(get_crew) == 3
    assert get_crew[0] == friend1
    assert get_crew[1] == friend2
    assert get_crew[2] == friend3

def test_delete_class():
    dia = UML_Diagram()
    bender = UML_Class("Bender")
    dia.add_class("Bender")

    assert next((v for v in dia._classes if v == bender), False)
    dia.delete_class("Bender")
    assert next((v for v in dia._classes if v == bender), True)

def test_add_multiple_delete_one_class():
    dia = UML_Diagram()
    bender = UML_Class("Bender")
    fry = UML_Class("Fry")
    dia.add_class("Bender")
    dia.add_class("Fry")

    assert next((v for v in dia._classes if v == bender), False)
    assert next((v for v in dia._classes if v == fry), False)
    dia.delete_class("Bender")
    assert next((v for v in dia._classes if v == bender), True)
    assert next((v for v in dia._classes if v == fry), False)

def test_delete_relation():
    dia = UML_Diagram()
    bender = UML_Class("Bender")
    fry = UML_Class("Fry")
    dia.add_class("Bender")
    dia.add_class("Fry")
    frender = UML_Relation(bender, fry, "aggregation")

    dia.add_relation("Bender", "Fry", "aggregation")
    
    assert dia._relations[0] == frender
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
    assert rels[0] == friends1 
    assert rels[1] == friends3
    assert rels[2] == friends4
    
    dia.delete_relations_containing("Zoidberg")

    rels = dia.get_all_relations()
    assert len(rels) == 1
    assert rels[0] == friends1

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

def test_replace_content():
    d1 = UML_Diagram()
    d2 = UML_Diagram()

    d1.add_class("c1")
    d1.add_class("c2")
    d1.add_class("c3")
    d1.add_relation("c1", "c2", "aggregation")

    d2.add_class("d1")
    d2.add_class("d2")
    d2.add_class("d3")
    d2.add_relation("d2", "d3", "realization")

    c1 = d1.get_class("c1")
    c2 = d1.get_class("c2")

    assert d1.get_class("c1") == UML_Class("c1")
    assert d1.get_class("c2") == UML_Class("c2")
    assert d1.get_class("c3") == UML_Class("c3")
    assert d1.get_relation("c1", "c2") == UML_Relation(c1, c2, "aggregation")

    d1.replace_content(d2)

    c3 = d1.get_class("d2")
    c4 = d1.get_class("d3")

    assert d1.get_class("d1") == UML_Class("d1")
    assert d1.get_class("d2") == UML_Class("d2")
    assert d1.get_class("d3") == UML_Class("d3")
    assert d1.get_relation("d2", "d3") == UML_Relation(c3, c4, "aggregation")

    with pytest.raises(ValueError) as VE:
        d1.get_class("c1")
    assert str(VE.value) == "Class c1 does not exist"

    with pytest.raises(ValueError) as VE: 
        d1.get_relation("d1", "d2")
    assert str(VE.value) == "Relation between d1 and d2 does not exist"