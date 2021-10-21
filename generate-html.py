import xml.dom.minidom as minidom
from glob import glob
import os.path


# from bs4 import BeautifulSoup

# def prettify_html(s):
#     return BeautifulSoup(s, "html.parser").prettify()


def children_to_str(elem):
    return "".join([c.toxml() for c in elem.childNodes])


def get_field(document, field_name):
    elems = document.getElementsByTagName(field_name)
    assert len(elems) == 1
    return children_to_str(elems[0])


def xml_to_str(file_name):
    with open(file_name, "r") as ifile:
        document = minidom.parse(ifile)

    title = get_field(document, "title")
    geogebra = get_field(document, "geogebra")
    statement = get_field(document, "statement")
    answer = get_field(document, "answer")

    result = ""

    result += f"<h2>{title}</h2>\n"
    result += f'<div class="statement">\n{statement}\n'
    result += f'<div class="geogebra-iframe"><iframe src="https://www.geogebra.org/geometry/{geogebra}?embed" width="600" height="500" allowfullscreen></iframe></div>'
    result += "</div>\n"
    result += (
        f'<div class="answer"><div class="hidden">\n{answer}\n</div></div>\n'
    )

    return result


def print_file(input_file_name, output_file):
    with open(input_file_name, "r") as input_file:
        for line in input_file:
            print(line, file=output_file, end="")


HEADER = "template/header.html"
FOOTER = "template/footer.html"


def valid_input_file(name):
    return all((str.isdigit(name[0]), str.isdigit(name[1]), name[2] == '-'))


def get_item_num(name):
    basename = os.path.basename(name)

    if not valid_input_file(basename):
        raise Exception(f"Wrong input file name: {basename}")

    return int(basename[0:2])


def num_to_page(n):
    if n == 0:
        return "index.html"
    else:
        return f"{n:02}.html"


def toc_str(n):
    def num_to_href(i):
        if i != n:
            return f'<a href="{num_to_page(i)}">{i}</a>'
        else:
            return f'<span>{i}</span>'

    # **FIXME** MAGICK NUNBER
    links = map(num_to_href, range(0,13))
    return '<nav>' + " ".join(links) + "</nav>"


def write_html(xml_file_name, n):
    output_file_name = num_to_page(n)

    with open(output_file_name, "w") as output_file:
        print_file(HEADER, output_file)
        print(toc_str(n), file=output_file)
        print(xml_to_str(xml_file_name), file=output_file)
        print_file(FOOTER, output_file)


def write_index(xml_files):
    output_file_name = num_to_page(0)

    with open(output_file_name, "w") as output_file:
        print_file(HEADER, output_file)
        print(toc_str(0), file=output_file)

        print('<ol id="toc">', file=output_file)
        for _file in xml_files:
            n = get_item_num(_file)
            with open(_file, "r") as ifile:
                document = minidom.parse(ifile)
                title = get_field(document, "title")
            print(f'<li><a href="{num_to_page(n)}">{title}</a></li>', file=output_file)
        print("</ol>", file=output_file)

        print_file(FOOTER, output_file)


if __name__ == "__main__":
    xml_files = glob("src/*.xml")
    xml_files.sort()

    toc = { x : get_item_num(x) for x in xml_files }

    for ifile,n in toc.items():
        write_html(ifile,n)

    write_index(xml_files)
