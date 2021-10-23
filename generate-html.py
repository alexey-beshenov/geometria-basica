import xml.dom.minidom as minidom
from glob import glob
import os
from string import Template

from quizitem import *

# Some configuration:
TEMPLATE_DIR = "template"
MAIN_TEMPLATE = f"{TEMPLATE_DIR}/main.html"
ITEM_TEMPLATE = f"{TEMPLATE_DIR}/item.html"
KATEX_CODE = f"{TEMPLATE_DIR}/katex.html"
GEOGEBRA_TEMPLATE = f"{TEMPLATE_DIR}/geogebra-app.html"
XML_DIR = "xml"


def read_template(file_name: str) -> Template:
    with open(file_name, "r") as f:
        return Template(f.read())


def get_xml_files() -> list[str]:
    return sorted([f for f in glob(f"{XML_DIR}/*.xml")])


def output_file_name(xml_file_name: str) -> str:
    """Transforms xml/foo.xml --> foo.html"""
    name = os.path.splitext(xml_file_name)[0]
    basename = os.path.basename(name)
    return f"{basename}.html"


def generate_toc(
    input_items: list[tuple[str, QuizItem]], current_item: QuizItem
) -> str:
    result: list[str] = []

    result.append(f'<a href="./">0</a>')

    for n, input_item in enumerate(input_items):
        file, item = input_item
        href = output_file_name(file)
        if current_item is not item:
            result.append(f'<a href="{href}" title="{item.title}">{n+1}</a>')
        else:
            result.append(f"<span>{n+1}</span>")

    return "<nav>" + " ".join(result) + "</nav>"


def generate_full_toc(input_items: list[tuple[str, QuizItem]]) -> str:
    result: list[str] = []

    for file, item in input_items:
        href = output_file_name(file)
        result.append(f'<li><a href="{href}">{item.title}</a></li>')

    return "<ol>" + "\n".join(result) + "</ol>"


if __name__ == "__main__":
    # Read all the templates
    print(f"Reading {MAIN_TEMPLATE} ...")
    main_tmpl: Template = read_template(MAIN_TEMPLATE)
    print(f"Reading {ITEM_TEMPLATE} ...")
    item_tmpl: Template = read_template(ITEM_TEMPLATE)
    print(f"Reading {GEOGEBRA_TEMPLATE} ...")
    geogebra_tmpl: Template = read_template(GEOGEBRA_TEMPLATE)

    print(f"Reading {KATEX_CODE} ...")
    with open(KATEX_CODE, "r") as f:
        katex: str = f.read()

    quiz_items: list[tuple[str, QuizItem]] = [
        (f, get_item_from_xml(f)) for f in get_xml_files()
    ]

    for file, item in quiz_items:
        geogebra: str = geogebra_tmpl.substitute(material_id=item.geogebra)
        content: str = item_tmpl.substitute(dataclasses.asdict(item))
        toc: str = generate_toc(quiz_items, item)
        result: str = main_tmpl.substitute(
            katex=katex, geogebra=geogebra, toc=toc, content=content
        )

        html_file = output_file_name(file)
        print(f"Writing {html_file}")
        with open(html_file, "w") as output_file:
            print(result, file=output_file)

    full_toc: str = generate_full_toc(quiz_items)
    index: str = main_tmpl.substitute(
        katex=katex, geogebra="", toc="", content=full_toc
    )

    index_file = "index.html"
    print(f"Wrting {index_file}")
    with open(index_file, "w") as output_file:
        print(index, file=output_file)
