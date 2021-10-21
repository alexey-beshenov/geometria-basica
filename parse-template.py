import re

IN_FILE = "index.html.template"
OUT_FILE = "index.html"

with open (IN_FILE, 'r') as ifile:
  with open (OUT_FILE, 'w') as ofile:
      for line in ifile:
          new_line = re.sub("<!-- geogebra:([a-z0-9]*) -->",
                            r'<div class="geogebra-iframe"><iframe src="https://www.geogebra.org/geometry/\1?embed" width="600" height="480" allowfullscreen></iframe></div>',
                            line)
          print (new_line, file=ofile, end="")
