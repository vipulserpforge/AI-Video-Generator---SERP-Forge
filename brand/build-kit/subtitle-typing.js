// SERP Forge subtitle typing (STYLE-SHEET section 7): every word types in letter by letter from its spoken start
// (data-t) to its end (data-e), 0.025-0.06 s per letter, 2-frame soft fade per letter, one solid orange caret
// that follows the last typed letter and fades 0.45 s after the phrase. Silent: no sound is tied to it.
window.sfType = function (tl, root) {
  const words = Array.from(document.querySelectorAll(root + " .tx [data-t]"));
  const chars = [], italics = [];
  words.forEach((w) => {
    const t0 = +w.dataset.t, t1 = +(w.dataset.e || w.dataset.t);
    const nodes = [];
    const walk = (n) => n.childNodes.forEach((c) => {
      if (c.nodeType === 3) nodes.push(c);
      else if (!(c.classList && (c.classList.contains("fr") || c.classList.contains("box")))) walk(c);
    });
    walk(w);
    const spans = [];
    nodes.forEach((tn) => {
      const frag = document.createDocumentFragment();
      for (const ch of tn.textContent) {
        const s = document.createElement("span"); s.className = "ch"; s.textContent = ch;
        const cr = document.createElement("span"); cr.className = "cr"; s.appendChild(cr);
        frag.appendChild(s); spans.push(s);
      }
      tn.replaceWith(frag);
    });
    const per = Math.min(0.06, Math.max(0.025, (t1 - t0) / Math.max(1, spans.length)));
    spans.forEach((s, i) => chars.push([s, t0 + i * per]));
    w.dataset.done = (t0 + spans.length * per).toFixed(3);
    w.dataset.dur = (spans.length * per).toFixed(3);
    const it = w.classList.contains("italic") ? w : w.querySelector(".italic");
    if (it) { it.classList.add("typed"); italics.push(it); }
  });
  // italic accent: each letter gets its colour sampled along the mint-to-peach gradient (#C2E4DC -> #FCBB82),
  // so untyped letters stay invisible (a background-clip gradient would show the whole word at once)
  italics.forEach((it) => {
    const cs = Array.from(it.querySelectorAll(".ch")), n = cs.length;
    cs.forEach((c, i) => {
      const f = n > 1 ? i / (n - 1) : 0, a = [0xC2, 0xE4, 0xDC], b = [0xFC, 0xBB, 0x82];
      c.style.color = "rgb(" + a.map((v, k) => Math.round(v + (b[k] - v) * f)).join(",") + ")";
    });
  });
  chars.forEach(([s, t], i) => {
    tl.fromTo(s, { opacity: 0 }, { opacity: 1, duration: 0.066, ease: "power1.out" }, t);
    const cr = s.querySelector(".cr");
    tl.fromTo(cr, { opacity: 0 }, { opacity: 1, duration: 0.001, immediateRender: false }, t);
    if (i + 1 < chars.length) tl.to(cr, { opacity: 0, duration: 0.001 }, chars[i + 1][1]);
    else tl.to(cr, { opacity: 0, duration: 0.3, ease: "power2.out" }, t + 0.45);
  });
};
