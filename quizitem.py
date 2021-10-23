import dataclasses
from string import Template
import xml.dom.minidom as minidom


# We'll group all fields in a dataclass:
@dataclasses.dataclass
class QuizItem:
    title: str
    geogebra: str
    statement: str
    answer: str


def get_field(document: minidom.Document, field_name: str) -> str:
    def _children_to_str(elem: minidom.Element) -> str:
        return "".join([c.toxml() for c in elem.childNodes])

    elems: list[minidom.Element] = document.getElementsByTagName(field_name)

    # **TODO** normally we don't want more than one field,
    # but maybe later an .xml file will be allowed to have several
    # <item>s? E.g. to group some things by topic
    if len(elems) == 0:
        raise Exception(f"Cannot find <{field_name}>")
    if len(elems) > 1:
        raise Exception(f"Didn't expect more than one <{field_name}>")

    return _children_to_str(elems[0])


def get_item_from_xml(file_name: str) -> QuizItem:
    with open(file_name, "r") as ifile:
        document: minidom.Document = minidom.parse(ifile)

    title: str = get_field(document, "title")
    geogebra: str = get_field(document, "geogebra")
    statement: str = get_field(document, "statement")
    answer: str = get_field(document, "answer")

    return QuizItem(title, geogebra, statement, answer)
