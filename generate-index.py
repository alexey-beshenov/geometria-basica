import xml.dom.minidom as minidom
from bs4 import BeautifulSoup
from glob import glob


def children_to_str(elem):
    return "".join([c.toxml() for c in elem.childNodes])


def get_field(document, field_name):
    elems = document.getElementsByTagName(field_name)
    assert len(elems) == 1
    return children_to_str(elems[0])


def xml_to_str(file):
    with open(file, "r") as ifile:
        document = minidom.parse(ifile)

    title = get_field(document, "title")
    geogebra = get_field(document, "geogebra")
    statement = get_field(document, "statement")
    answer = get_field(document, "answer")

    result = ""

    result += f"<h2>{title}</h2>\n"
    result += f'<div class="statement">\n{statement}\n'
    result += f'<div class="geogebra-iframe"><iframe src="https://www.geogebra.org/geometry/{geogebra}?embed" width="600" height="480" allowfullscreen></iframe></div>'
    result += "</div>\n"
    result += (
        f'<div class="answer"><div class="hidden">\n{answer}\n</div></div>\n'
    )

    return result


def prettify_html(s):
    return BeautifulSoup(s, "html.parser").prettify()


HEADER = "template/header.html"
FOOTER = "template/footer.html"

OUT_FILE = "index.html"


if __name__ == "__main__":
    result = []

    with open(HEADER, "r") as ifile:
        result += [line for line in ifile]

    for file in sorted(glob("src/*.xml")):
        result.append(xml_to_str(file))

    result += [line for line in open(FOOTER)]

    with open(OUT_FILE, "w") as ofile:
        print(prettify_html("".join(result)), file=ofile, end="")
