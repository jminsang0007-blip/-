// usage: node render.mjs specs.json outdir
import { chromium } from '/opt/node22/lib/node_modules/playwright/index.mjs';
import fs from 'fs'; import path from 'path';
const [,, specFile, outDir] = process.argv;
const specs = JSON.parse(fs.readFileSync(specFile, 'utf8'));
fs.mkdirSync(outDir, { recursive: true });
const nm = path.resolve('node_modules');
const font = (pkg, fam, w) => ['korean','latin'].map(sub => `@font-face{font-family:'${fam}';font-weight:${w};src:url(file://${nm}/@fontsource/${pkg}/files/${pkg}-${sub}-${w}-normal.woff2) format('woff2');}`).join('');
const css = [400,600,700].map(w => font('ibm-plex-sans-kr','IBM Plex Sans KR',w)).join('') + [700].map(w => font('noto-serif-kr','Noto Serif KR',w)).join('');
const icons = {};
const MI = JSON.parse(fs.readFileSync(`${nm}/@iconify-json/mingcute/icons.json`,'utf8'));
for (const s of specs) for (const m of s.dsl.matchAll(/ref:mi:([a-z0-9-]+)/g)) { const ic = MI.icons[m[1]]; if (!ic) throw new Error('no icon '+m[1]); icons[m[1]] = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">${ic.body}</svg>`; }
const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
const page = await browser.newPage({ deviceScaleFactor: 2 });
for (const s of specs) {
  const html = `<!doctype html><html><head><meta charset="utf-8"><style>${css} html,body{margin:0;background:${s.bg||'transparent'}} #c{width:${s.w}px;height:${s.h}px}</style>
  <script src="file://${nm}/@antv/infographic/dist/infographic.min.js"></script></head><body><div id="c"></div><script>
  const ICONS=${JSON.stringify(icons)};
  AntVInfographic.registerResourceLoader(async cfg => ICONS[String(cfg.data).replace(/^ref:mi:/,"")] ? AntVInfographic.loadSVGResource(ICONS[String(cfg.data).replace(/^ref:mi:/,"")]) : null);
  const ig = new AntVInfographic.Infographic({container:'#c',width:${s.w},height:${s.h},editable:false});
  ig.render(${JSON.stringify(s.dsl)});
  </script></body></html>`;
  const f = path.resolve(outDir, s.name + '.html'); fs.writeFileSync(f, html);
  await page.setViewportSize({ width: s.w, height: s.h });
  await page.goto('file://' + f); await page.waitForTimeout(2500);
  await page.locator('#c').screenshot({ path: path.resolve(outDir, s.name + '.png'), omitBackground: !s.bg });
  fs.unlinkSync(f); console.log('ok', s.name);
}
await browser.close();
