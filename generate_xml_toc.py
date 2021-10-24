from quizitem import *
from generate_html import get_all_xml_files
from glob import glob

if __name__ == "__main__":
    for n,f in enumerate(get_all_xml_files()):
        item = get_item_from_xml(f)
        print(f"{n+1}. `{f}`: {item.title}\n")
        print(f"   (https://geogebra.org/geometry/{item.geogebra})\n")
