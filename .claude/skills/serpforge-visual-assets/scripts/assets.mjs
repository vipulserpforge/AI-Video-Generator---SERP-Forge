#!/usr/bin/env node
// SERP Forge visual assets: find meaningful icons and real brand logos from the local libraries (library/icons).
//
//   node assets.mjs search <words...>                     best-fitting icons for an idea (Phosphor first, then Lucide)
//   node assets.mjs icon <name> --out <file.svg> [--weight duotone|fill|regular|bold|light|thin] [--color #hex] [--accent #hex] [--lib phosphor|lucide]
//   node assets.mjs logo <brand> --out <file.svg> [--mono #hex]   official brand mark (Simple Icons, CC0) in the brand's own colour
//   node assets.mjs brands <words...>                     find brand slugs
//
// Everything is offline and deterministic: SVGs are copied from node_modules into the video's assets folder.
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";

function projectRoot(start = process.cwd()) {
  let d = path.resolve(start);
  while (d !== path.dirname(d)) { if (fs.existsSync(path.join(d, "library", "icons", "package.json"))) return d; d = path.dirname(d); }
  const here = path.dirname(new URL(import.meta.url).pathname);
  return path.resolve(here, "../../../..");
}
const ROOT = projectRoot();
const LIB = path.join(ROOT, "library", "icons", "node_modules");
const req = createRequire(path.join(ROOT, "library", "icons", "package.json"));
const args = process.argv.slice(2);
const cmd = args.shift();
const opt = (k, d) => { const i = args.indexOf(k); return i >= 0 ? args.splice(i, 2)[1] : d; };

async function phosphor() { return (await import(path.join(LIB, "@phosphor-icons/core/dist/index.mjs"))).icons; }
function lucideTags() { return JSON.parse(fs.readFileSync(path.join(LIB, "lucide-static/tags.json"), "utf8")); }

function score(words, name, tags = [], cats = []) {
  let s = 0; const n = name.toLowerCase();
  for (const w of words) {
    if (n === w) s += 10; else if (n.split("-").includes(w)) s += 6; else if (n.includes(w)) s += 3;
    if (tags.some(t => t.toLowerCase() === w)) s += 4; else if (tags.some(t => t.toLowerCase().includes(w))) s += 1.5;
    if (cats.some(c => c.toLowerCase().includes(w))) s += 1;
  }
  return s;
}

if (cmd === "search") {
  const words = args.join(" ").toLowerCase().split(/\s+/).filter(Boolean);
  const ph = (await phosphor()).map(i => ({ lib: "phosphor", name: i.name, s: score(words, i.name, i.tags, i.categories), tags: i.tags.slice(0, 5) }));
  const lt = lucideTags();
  const lu = Object.entries(lt).map(([name, tags]) => ({ lib: "lucide", name, s: score(words, name, tags) - 2.5, tags: tags.slice(0, 5) }));
  const top = [...ph, ...lu].filter(x => x.s > 0).sort((a, b) => b.s - a.s).slice(0, 14);
  if (!top.length) console.log("no match: try other words (the idea, not the look)");
  for (const t of top) console.log(`${t.lib.padEnd(9)} ${t.name.padEnd(28)} score ${t.s.toFixed(1).padStart(4)}  ${t.tags.join(", ")}`);
} else if (cmd === "icon") {
  const name = args.shift(); const lib = opt("--lib", "phosphor"); const weight = opt("--weight", "duotone");
  const color = opt("--color", "#ABDCD6"); const accent = opt("--accent", null); const out = opt("--out", `${name}.svg`);
  let src, svg;
  if (lib === "lucide") {
    src = path.join(LIB, "lucide-static/icons", `${name}.svg`);
    svg = fs.readFileSync(src, "utf8").replace(/stroke="currentColor"/g, `stroke="${color}"`).replace(/stroke-width="2"/g, 'stroke-width="1.75"');
  } else {
    const file = weight === "regular" ? `${name}.svg` : `${name}-${weight}.svg`;
    src = path.join(LIB, "@phosphor-icons/core/assets", weight, file);
    svg = fs.readFileSync(src, "utf8").replace('fill="currentColor"', `fill="${color}"`);
    if (accent) svg = svg.replace(/(<path[^>]*?)opacity="0\.2"/g, `$1fill="${accent}" opacity="0.35"`);
  }
  fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true }); fs.writeFileSync(out, svg);
  console.log(`icon ${lib}:${name} (${lib === "lucide" ? "stroke" : weight}) -> ${out}`);
} else if (cmd === "logo" || cmd === "brands") {
  const si = req("simple-icons"); const all = Object.values(si).filter(x => x && x.slug);
  const q = args.filter(a => !a.startsWith("--")).join(" ").toLowerCase();
  if (cmd === "brands") {
    const hits = all.filter(x => x.title.toLowerCase().includes(q) || x.slug.includes(q.replace(/\s+/g, ""))).slice(0, 20);
    for (const h of hits) console.log(`${h.slug.padEnd(24)} ${h.title.padEnd(28)} #${h.hex}`);
    if (!hits.length) console.log(`not in Simple Icons. Fallback: npx hyperframes media-use resolve --type logo --entity "${q}" --project <build>`);
  } else {
    const mono = opt("--mono", null); const out = opt("--out", null);
    const b = all.find(x => x.slug === q.replace(/\s+/g, "")) || all.find(x => x.title.toLowerCase() === q);
    if (!b) { console.log(`not in Simple Icons: ${q}. Fallback (official mark, never redrawn): npx hyperframes media-use resolve --type logo --entity "${q}" --project <build>`); process.exit(2); }
    const svg = b.svg.replace("<svg ", `<svg fill="${mono || "#" + b.hex}" `);
    const file = out || `${b.slug}.svg`;
    fs.mkdirSync(path.dirname(path.resolve(file)), { recursive: true }); fs.writeFileSync(file, svg);
    console.log(`logo ${b.title} (#${b.hex}${mono ? `, mono ${mono}` : ""}) -> ${file}  [Simple Icons, CC0; the mark itself is the brand's trademark]`);
  }
} else {
  console.log("usage: search <words> | icon <name> --out f.svg [--weight duotone] [--color #hex] [--accent #hex] [--lib lucide] | logo <brand> --out f.svg [--mono #fff] | brands <words>");
}
