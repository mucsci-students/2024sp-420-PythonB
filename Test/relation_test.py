from Models.UML_Relation import UML_Relation
from Models.UML_Diagram import rel_types
from Models.UML_Class import UML_Class

def test_ctor_relation():
    src = UML_Class("source")
    dest = UML_Class("destination")
    type1 = "aggregation"
    rel1 = UML_Relation(src, dest, type1)
    assert isinstance(rel1, UML_Relation)
    assert rel1._src == src
    assert rel1._src != dest
    assert rel1._dst == dest
    assert rel1._dst != src
    assert rel1._type == type1
    assert rel1._type != "composition"

def test_get_src():
    src = UML_Class("source")
    dest = UML_Class("destination")
    type1 = "aggregation"
    rel1 = UML_Relation(src, dest, type1)

    get_src = rel1.get_src()
    assert get_src == rel1._src
    assert get_src != rel1._dst

def test_get_dst():
    src = UML_Class("source")
    dest = UML_Class("destination")
    type1 = "aggregation"
    rel1 = UML_Relation(src, dest, type1)

    get_dst = rel1.get_dst()
    assert get_dst == rel1._dst
    assert get_dst != rel1._src

def test_get_type():
    src = "source"
    dest = "destination"
    type1 = "aggregation"
    rel1 = UML_Relation(src, dest, type1)

    get_type = rel1.get_type()
    assert get_type == rel1._type

def test_get_src_name():
    src_name = "Pied Piper"
    dest_name = "Hawaii"
    src = UML_Class(src_name)
    dest = UML_Class(dest_name)
    type1 = "generalization"
    rel1 = UML_Relation(src, dest, type1)

    get_source_name = rel1.get_src_name()
    assert get_source_name == src_name
    assert get_source_name != dest_name

def test_get_dst_name():
    src_name = "Pied Piper"
    dest_name = "Hawaii"
    src = UML_Class(src_name)
    dest = UML_Class(dest_name)
    type1 = "generalization"
    rel1 = UML_Relation(src, dest, type1)

    get_dest_name = rel1.get_dst_name()
    get_source_name = rel1.get_src_name()
    assert get_dest_name == dest_name
    assert get_dest_name != get_source_name

def test_set_src():
    src_name = "Pied Piper"
    dest_name = "Hawaii"
    src = UML_Class(src_name)
    dest = UML_Class(dest_name)
    type1 = "generalization"
    rel1 = UML_Relation(src, dest, type1)

    new_src_name = "Hooli"
    rel1.set_src(new_src_name)

    assert rel1.get_src() == new_src_name
    assert rel1.get_src() != 'Minecraft'
    assert rel1.get_src() != src_name



    

#"aggregation", "composition", "generalization", "inheritance"