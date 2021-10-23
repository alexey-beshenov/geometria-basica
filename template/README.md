# Templates

We are using `string.Template` for basic substitutions. 

* `geogebra-app.html` : JS code to include GeoGebra App.

  Template parameter: `$material_id`.

* `item.html` : HTML code for one item.

  Parameters: `$title`, `$statement`, `$answer`.

* `katex.html` : JS code to include KaTeX
  (to be pasted verbatim, not a template).

* `main.html` : main page template.

  Parameters: `$page_title`, `$katex`, `$geogebra`, `$toc`, `$content`.
