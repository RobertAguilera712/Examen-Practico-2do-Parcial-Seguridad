function(t) {
  var n, i = this,
    o = l.getSelectorFromElement(this);
  o && (n = document.querySelector(o));
  var r = e(n).data("bs.modal") ? "toggle" : s(s({}, e(n).data()), e(this).data());
  "A" !== this.tagName && "AREA" !== this.tagName || t.preventDefault();
  var a = e(n).one("show.bs.modal", (function(t) {
    t.isDefaultPrevented() || a.one("hidden.bs.modal", (function() {
      e(i).is(":visible") && i.focus()
    }))
  }));
  qt._jQueryInterface.call(e(n), r, this)
}