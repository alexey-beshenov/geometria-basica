# geometria-basica

This is the source code for the interactive presentation that you may see at

https://alexey-beshenov.github.io/geometria-basica/


## Files

* `basic.css` : CSS style.

* `generate_html.py` : script to generate HTML from XML.
  To be run from the same directory. Generates from each file
  `xml/foo.xml` the corresponding `foo.html` in the root,
  plus writes `index.html`.

* `quizitem.py` : some extra Python code used by `generate-html.py`.

* `show-hide.js` : basic script to show/hide blocks on the page.

* `template/` : basic HTML templates.

* `xml/` : source files.

* `*.html` : all HTML files in the root directory are automatically generated
  from `xml/*.xml` and overwritten silently by `generate_html.py`.


## Contents

* `xml/01-area-de-triangulo.xml`: Área de triángulo

  (https://geogebra.org/geometry/rrfkyqtq)

* `xml/02-area-de-n-agono.xml`: Área de un n-ágono regular

  (https://geogebra.org/geometry/myfjveys)

* `xml/03-area-de-cuadrilatero-convexo.xml`: Área de un cuadrilátero convexo

  (https://geogebra.org/geometry/yfe7vtzq)

* `xml/04-recta-de-Euler.xml`: Recta de Euler

  (https://geogebra.org/geometry/bvcsqszf)

* `xml/05-nueve-puntos.xml`: Circunferencia de los nueve puntos

  (https://geogebra.org/geometry/tmcezq4g)

* `xml/06-Ceva.xml`: Teorema de Ceva

  (https://geogebra.org/geometry/pbrjszyj)

* `xml/07-Menelao.xml`: Teorema de Menelao

  (https://geogebra.org/geometry/expkswct)

* `xml/08-Pappus.xml`: Teorema del hexágono de Pappus

  (https://geogebra.org/geometry/n4h2je78)

* `xml/09-Pascal.xml`: Teorema de Pascal (Hexagrammum Mysticum)

  (https://geogebra.org/geometry/uzbzbnkx)

* `xml/10-Desargues.xml`: Teorema de Desargues

  (https://geogebra.org/geometry/f2nm93cx)

* `xml/11-Simson.xml`: Línea de Simson

  (https://geogebra.org/geometry/fpqvppq5)


## Contact

Alexey Beshenov (cadadr@gmail.com)
