const SHOW_ANSWER = "▾ ver la respuesta";
const HIDE_ANSWER = "▴ esconder la respuesta";

function addMoreLink(elem) {
    const p = document.createElement("p");
    const a = document.createElement("a");
    const id = elem.id;
    a.setAttribute("class", "more-link");
    a.setAttribute("id", id+"-more-link");
    a.textContent = SHOW_ANSWER;
    a.setAttribute("href", "javascript:showMore(\""+id+"\")");
    p.appendChild(a);
    elem.parentElement.insertBefore(p, elem);
}

function showMore(id) {
    const elem = document.getElementById(id);
    elem.setAttribute("style", "display: block");
    const a = document.getElementById(id+"-more-link");
    a.textContent = HIDE_ANSWER;
    a.setAttribute("href", "javascript:showLess(\""+id+"\")");
}

function showLess(id) {
    const elem = document.getElementById(id);
    elem.setAttribute("style", "display: none");
    const a = document.getElementById(id+"-more-link");
    a.textContent = SHOW_ANSWER;
    a.setAttribute("href", "javascript:showMore(\""+id+"\")");
}

document.addEventListener("DOMContentLoaded", function() {
    const divs = document.getElementsByTagName("div");
    let j = 0;
    for (i = 0; i < divs.length; i++) {
	if (divs[i].getAttribute("class") === "hidden") {
	    divs[i].setAttribute("id", `answer-${j}`);
	    j++;
	    addMoreLink(divs[i]);
	}
    }
});
