from ..Models.uml_relation import UML_Relation
from ..Models.uml_class import UML_Class

def test_ctor_relation():
    src = UML_Class("source")
    dest = UML_Class("destination")
    type1 = "Aggregation"
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
    type1 = "Realization"
    rel1 = UML_Relation(src, dest, type1)

    get_source_name = rel1.get_src_name()
    assert get_source_name == src_name
    assert get_source_name != dest_name

def test_get_dst_name():
    src_name = "Pied Piper"
    dest_name = "Hawaii"
    src = UML_Class(src_name)
    dest = UML_Class(dest_name)
    type1 = "Realization"
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
    type1 = "Realization"
    rel1 = UML_Relation(src, dest, type1)

    new_src_name = "Hooli"
    rel1.set_src(new_src_name)

    assert rel1.get_src() == new_src_name
    assert rel1.get_src() != 'Minecraft'
    assert rel1.get_src() != src_name

def test_set_dst():
    src_name = "Pied Piper"
    dest_name = "Hawaii"
    src = UML_Class(src_name)
    dest = UML_Class(dest_name)
    type1 = "Realization"
    rel1 = UML_Relation(src, dest, type1)

    new_dst_name = "Stan"
    rel1.set_dst(new_dst_name)

    assert rel1.get_dst() == new_dst_name
    assert rel1.get_dst() != 'Minecraft'
    assert rel1.get_dst() != dest_name

def test_set_type():
    src_name = "Pied Piper"
    dest_name = "Hawaii"
    src = UML_Class(src_name)
    dest = UML_Class(dest_name)
    type1 = "Realization"
    rel1 = UML_Relation(src, dest, type1)

    new_type = "Inheritance"
    rel1.set_type(new_type)

    assert rel1.get_type() == new_type
    assert rel1.get_type() != 'Minecraft'
    assert rel1.get_type() != type1

def test_eq():
    rel1 = UML_Relation(UML_Class("name1"), UML_Class("name2"), "inheritance")
    rel2 = UML_Relation(UML_Class("name1"), UML_Class("name2"), "inheritance")
    diff_rel = UML_Relation(UML_Class("name3"), UML_Class("name2"), "inheritance")

    assert rel1 == rel1
    assert rel1 == rel2
    assert rel1 != diff_rel
    assert rel1 != "Hello"

def test_str():
    rel1 = UML_Relation(UML_Class("name1"), UML_Class("name2"), "inheritance")

    assert str(rel1) == "name1 <--- Inheritance ---> name2"
    assert str(rel1) != "Bullock"