---
title: "Prompt-based dashboard build — Global Commerce exact rebuild spec"
project: diy-ai-reporting
type: note
status: raw
created: 2026-11-09
author: Arthur
annotated_by: Libby
source: https://drive.google.com/file/d/1GcXniPYEqh8Bgu9kZn4V0N0igeTXk7DY/view
source_filename: Global_Commerce_Exact_Build_Spec.md
target_output: global_commerce_dashboard.html
inputs: Excel workbook + dark world-map image
spec_lines: ~420
code_blocks_supplied: 18
visibility: private
---

# Prompt-based dashboard build — Global Commerce

First-hand artefact: the prompt used to make an AI build a working analytics
dashboard from an Excel workbook, in one shot. The full prompt is reproduced
verbatim at the end. These are notes on what it reveals.

## Why it belongs in this research

The project exists to characterise what non-developers actually produce when
they "build it with AI." This is the opposite data point and therefore the
control case: what it takes to produce a *correct* dashboard this way, written
by someone who knows data and code.

It is also the most concrete illustration available of the
specification/generation/validation frame — not borrowed from an advisor, but
from our own hands.

## The details worth noting

### 1. The specification is the work

~420 lines of prose and code to produce one HTML file. The generation step was
a single request. **Everything expensive in this artefact is specification.**

### 2. Half the normative language is prohibition

Rough counts across the spec: 40 uses of "must", 17 of "exact"/"exactly",
against 32 prohibitions — 10 × "do not", 8 × "never", 3 × "must not", 11 × "no".

Specifying what to build turned out to require roughly as much effort as
forbidding what not to build.

### 3. The defensive clauses are scar tissue

Several read as prior failures encoded as rules:

- "**Mandatory map implementation contract — do not replace with a static map.**
  The Country Market Explorer is a required interactive control, not a visual
  element."
- "The period dropdown is **a working data control, not a decorative label**."
- "**Map tooltip must not be empty.**"
- "It **must not be permanently hidden** after rendering."
- "Do not use pseudo-elements alone for the click target."
- "Do not add navigation icons, menu items, links, settings buttons, profile
  buttons, collapse controls or any other sidebar buttons... it must contain no
  non-functional controls."

Each one documents a way the model produced something that *looked* right and
was inert. The recurring failure is plausible surface over absent function —
which is precisely the failure a non-expert would not catch.

### 4. By the end, the human writes the code

The spec supplies **18 code blocks**, and the later ones are not descriptions
but working implementations: `selectCountry()`, `renderMapDots()`,
`bindMapInteractionsOnce()`, `clearCountrySelection()`, `showMapTooltip()`,
`moveMapTooltip()`, `renderCountryDetailCard()`, plus the state object and the
exact `render()` call order.

So the claim "the AI built it" does not survive contact with the artefact. The
AI assembled and styled; **the hard interaction logic was hand-written and
pasted in.** That requires knowing what the hard parts are, which is the part
that does not transfer to a non-developer.

### 5. A semantic model, written in prose

The calculations table is a semantic layer by another name — every measure
defined before any code exists:

- one distinct `Order ID` is one order, even across several product rows
- return rate denominator is filtered rows, not orders
- profit margin is `SUM(Profit) / SUM(Sales) * 100`, not an average of margins
- a category filter must affect comparison periods too

These are exactly the definitions that differ between two people asked for the
same number. Here one person fixed them in writing. **Nothing in the tutorial
corpus does this.**

### 6. Validation requirements, expressed as specification

Because the author cannot eyeball every number, the spec names the failure
modes in advance:

- "If a comparison denominator is zero or absent, render an em dash (—), **not
  0%, NaN, Infinity, a blank badge or a made-up value**."
- "**Never use a hard-coded Jan–Dec list.** A Jan–Sep data range must display
  Jan–Sep only."
- "no NaN, Infinity, undefined, hard-coded metric, broken tooltip or missing
  label"
- "displayed totals **reconcile to the workbook**"

The anti-fabrication and anti-hard-coding clauses are the interesting ones:
they anticipate the model inventing something plausible rather than admitting
absence.

### 7. Validation is explicit, manual, and enumerated

A 16-item verification checklist, with named test cases — "test one dot and one
row for at least United States, Canada, Germany and Australia." Acceptance
criteria written by the person who knows what correct looks like.

## What it demonstrates

Generation was outsourced. **Specification and validation were retained
entirely by the human, at length, in writing.** That is the Mylovanov frame
without needing to assert it.

And it sharpens the contrast with the tutorial corpus: tutorials pick tasks with
no verifiable answer — a news digest, a flight-price alert — so none of this
apparatus is needed and none of it appears. Here the numbers must reconcile to a
workbook, so all of it is needed. **The tutorials are not teaching a cheaper
version of this work; they are avoiding the class of problem where the work
exists.**

## To check

- Whether the delivered dashboard actually passed its own 16-item checklist,
  and which items failed first
- How many iterations this spec went through — the defensive clauses imply
  several, and that count is the real cost figure
- Whether an equivalent result is reachable without hand-written interaction
  code, which is the question a non-developer faces

---

*Everything below is the prompt as written, reproduced in full. Markdown
structure (headings, the calculations table, code fences) was restored after the
Google Drive paste flattened it; no wording was changed, added or removed.*

## Global Commerce — Exact Rebuild Specification

### Instruction to the builder

You have exactly two attachments: an Excel workbook and a dark world-map image.
Build a single self-contained file named `global_commerce_dashboard.html` that
reproduces this specification exactly. Do not redesign, simplify, substitute
components, add sections, omit sections, or choose alternative colours,
proportions, metrics or behaviours. Return only the finished HTML file.

The Excel workbook is the sole source of all business values. The supplied map
image is the sole visual source for the map background. Read both attachments
before writing code.

The finished HTML must open locally with no network connection. Embed all parsed
Excel rows as JSON in the generated script and embed the attached map image as a
Base64 data URI. Use only native HTML, CSS, JavaScript and inline SVG: no CDN,
packages, framework, Chart.js, D3, Leaflet, external fonts or external assets.

### Required data model and calculations

Use the workbook's data sheet and its actual column headers. The expected
headers are:

`Order ID`, `Order Date`, `Ship Date`, `Market`, `Country`, `Region`, `State`,
`City`, `Customer Segment`, `Category`, `Sub-Category`, `Product Name`, `Sales`,
`Quantity`, `Discount`, `Profit`, `Shipping Cost`, `Returned`, `Order Priority`.

Parse `Order Date` as a valid local calendar date. Use it for every period,
chart and comparison. One distinct `Order ID` is one order even when it has
several product rows.

| Displayed measure | Exact calculation |
|---|---|
| Total Sales | `SUM(Sales)` of filtered rows |
| Total Profit | `SUM(Profit)` of filtered rows |
| Orders | `COUNT DISTINCT(Order ID)` of filtered rows |
| Category sales | `SUM(Sales)` grouped by Category |
| Country sales | `SUM(Sales)` grouped by Country |
| Profit margin | `SUM(Profit) / SUM(Sales) * 100` |
| Return rate | `COUNT(rows where Returned equals Yes) / COUNT(filtered rows) * 100` |
| Growth % | `(current - comparison) / ABS(comparison) * 100` |

If a comparison denominator is zero or absent, render an em dash (—), not 0%,
NaN, Infinity, a blank badge or a made-up value.

Find the largest calendar year in `Order Date`:

- **This Year** is January through December of that largest year and is the
  default selection.
- **Last Year** is January through December of the preceding year.
- In This Year view, compare the latest year with the previous year.
- In Last Year view, compare the selected year with the year before it.
- A category filter must affect all calculations including comparison periods.

Generate the monthly list by iterating only from the first to final month in the
selected period where the selected range has data. Never use a hard-coded
Jan–Dec list. A Jan–Sep data range must display Jan–Sep only.

Use these display formatters:

- values at or above 1,000,000: `$1.25M`
- values at or above 1,000: `$125K` (one decimal only where it materially
  improves clarity)
- smaller values: `$950`
- counts: `1,234`
- percentages: one decimal place, e.g. `+5.6%`

### Fixed visual tokens

```css
:root {
  --canvas:#090D16;
  --surface:#101625;
  --surface-deep:#0A101C;
  --sidebar:#151E30;
  --chart-surface:#202A3D;
  --line:#1B2234;
  --ink:#FFFFFF;
  --muted:#8E9CAE;
  --blue:#2B78FE;
  --pink:#E03B8B;
  --pink-dark:#B8206E;
  --coral:#FA5A5A;
  --violet:#4D2CFA;
  --mint:#05DF96;
  --raised:0 4px 20px rgba(0,0,0,.45),0 1px 3px rgba(0,0,0,.3);
}
```

Use `system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif`
everywhere. Use a `#090D16` page canvas, compact white typography, `#8E9CAE`
secondary text, 20px card radius, 16px gaps and dark, low-contrast shadows. This
is a dark premium analytics interface, not neumorphism, a light dashboard or a
generic SaaS template.

### Exact page grid

- `.shell`: CSS grid, `grid-template-columns: 80px minmax(0,1fr)`,
  `min-height:100vh`.
- Sidebar: `#151E30`, 24px 12px padding, right border `1px solid #1B2234`.
- Main: top/bottom/side padding `26px clamp(16px,2.5vw,40px) 40px`;
  `max-width:1600px`; centre horizontally.
- Header: title at left and controls at right; 24px bottom margin.
- All dashboard cards have `background:#101625`, `border-radius:20px`,
  `overflow:hidden`, a subtle white 5% border and `var(--raised)` shadow.
- KPI grid: `1.4fr 1fr 1fr 1.55fr`; 16px gap; 16px lower margin.
- Chart grid: `1.58fr 1fr`; 16px gap; 16px lower margin.
- Bottom grid: `.95fr 1.55fr`; 16px gap.

Responsive:

- At maximum width 1280px, KPI grid becomes 2 columns and the bottom grid
  becomes 1 column.
- At maximum width 960px, charts stack; sidebar changes to 72px; chart height
  can reduce to 316px.
- At maximum width 640px, hide the sidebar, use 18px × 13px main padding, stack
  all grids to 1 column and reduce map panel to 240px.

No horizontal page scroll, card overlap, clipping, internal country list
scrollbar or layout shift is allowed.

### Sidebar and header

Create an 80px sidebar with only:

- a 40px rounded-square house icon logo using
  `linear-gradient(135deg,#2D4BFE,#4D2CFA)`;
- small uppercase `GLOBAL` label beneath it.

Do not add navigation icons, menu items, links, settings buttons, profile
buttons, collapse controls or any other sidebar buttons. The sidebar is branding
only; it must contain no non-functional controls.

Header content exactly:

- `Global Commerce`
- `Sales performance across the world`

At right, create only:

- One real `<select id="periodSelect">` dropdown with exactly two options:
  `This Year` (`value="thisYear"`) and `Last Year` (`value="lastYear"`). It
  defaults to This Year.
- A Category select list, populated from the actual category column, with
  `All categories` as its first option.

Controls are dark `#101625`, 38px tall, 10px radius, `1px #1B2234` border. The
selected period dropdown option must drive the whole dashboard and show white
text. Do not create segmented period buttons, date buttons, export buttons, or
any other header controls.

### Mandatory period-dropdown behaviour

The period dropdown is a working data control, not a decorative label. Wire it
once using `change` and update state, then re-render the entire dashboard:

```js
document.getElementById('periodSelect').addEventListener('change', (event) => {
  state.period = event.target.value;
  state.selectedCountry = null;
  render();
});
```

When This Year is selected, all KPIs, deltas, sparklines, category gauge,
charts, country rankings, map dots, tooltips, country card and signals must use
the latest calendar year. When Last Year is selected, all of those same elements
must use the immediately preceding calendar year. The comparison period must
move back one year accordingly. Changing the dropdown must visibly change the
displayed values wherever the workbook contains different data, must preserve
the currently selected category filter, and must clear any country selection so
no stale map detail remains.

### KPI cards

All three metric cards are 186px high with 20px padding. They contain an icon
tile at top left, delta plus comparison context at top right, label and value in
middle, and sparkline at bottom.

#### Total Sales

- pink card background: `linear-gradient(135deg,#E03B8B 0%,#B8206E 100%)`;
- border `#C02878`;
- pink glow: `0 0 0 1px rgba(224,59,139,.3),0 8px 32px rgba(224,59,139,.35)`;
- white shopping bag icon and white sparkline;
- label `Total Sales`;
- white value and white positive/negative delta treatment.

#### Total Profit

- dark standard card;
- subtle coral icon tile;
- coral trend icon;
- label `Total Profit`;
- pink (`#E03B8B`) smooth sparkline.

#### Orders

- dark standard card;
- subtle violet icon tile;
- violet receipt icon;
- label `Orders`;
- violet (`#4D2CFA`) smooth sparkline.

#### Sales by Category

- standard dark card; 20px padding; minimum height 186px;
- title `Sales by Category`; subtitle `Share of total sales`;
- 270-degree inline SVG semi-donut, 148px × 128px;
- the empty arc track is `#202A3D`, 13px wide, fully round line caps;
- category arc colours must be Technology `#2B78FE`, Furniture `#FA5A5A`,
  Office Supplies `#4D2CFA`;
- put filtered Total Sales in the centre with tiny `Total sales` sublabel;
- a compact legend at right shows each category and one-decimal share of sales;
- category arcs and legend update on every filter change.

### Charts

Each chart card has height 338px. Its header uses 20px top/side padding. Its
plot area is `#202A3D`, 12px radius, `height:257px`, with an inset margin of
`8px 10px 0`.

#### Sales & Profit

- title `Sales & Profit`; subtitle `Monthly trend`;
- inline legend: Sales blue `#2B78FE`, Profit coral `#FA5A5A`;
- inline SVG dimensions close to 700 × 245; chart left margin 52px, right 10px,
  top 14px, bottom 32px;
- four faint dashed horizontal grid lines: white at 6% opacity,
  `stroke-dasharray:3 5`;
- left axis labels represent Sales only;
- Sales uses a 2.6px blue smooth cubic Bézier line and blue vertical fade fill;
- Profit uses a 2.3px `#E03B8B` smooth cubic Bézier line and pink vertical fade
  fill;
- both fills must fade from roughly 45% / 38% at top to 0% at bottom;
- use a transparent 22px hover target around each Sales monthly point;
- hover tooltip shows month, blue Sales value and coral Profit value;
- labels must be dynamic, skipped where required and the final month label
  always remains visible.

#### Monthly Orders

- title `Monthly Orders`; subtitle `Order volume by month`;
- inline SVG dimensions close to 410 × 245;
- dark transparent bar track at every month;
- actual data bar uses blue/violet colour and opacity from 0.50 through 1.00
  according to value relative to the maximum;
- bars must have `rx = width / 2`, producing visibly rounded/pill tops and
  bottom corners;
- use real dynamic months only;
- show a hover tooltip with month and distinct Orders;
- avoid label collision by skipping labels at responsive intervals.

Implement all line curves and sparklines with cubic Bézier SVG paths. Do not
make lines angular. Do not use canvas or a charting package.

### Performance Signals card

Title: `Performance Signals`

Subtitle: `Filtered period intelligence`

Use four vertically stacked cards, each `#090D16` at approximately 82% opacity,
10px radius, `1px solid #1B2234`, 10px × 14px padding and a 32px coloured icon
tile. Build all copy from filtered data:

- **Top Category** — `[category] leads at [share]% revenue share · [sales] of [total] total sales`
- **Market Leader** — `[country] ranked #1 with [sales] · [share]% portfolio share`
- **Profit Margin** — `[margin]% blended margin · Sales [growth] vs prior yr · Profit [profit]`
- **Total Orders** — `[orders] orders processed · [growth] vs prior yr · [return rate]% return rate`

Use blue, violet, pink and mint icon accents respectively. Green text is
`#05DF96`; negative text is `#FA5A5A`; highlighted values use blue or pink as
appropriate.

### Country Market Explorer

Use the standard dark card with `#0A101C` card background and no visible card
border. Give it 20px padding.

Header:

- `Country Market Explorer`
- `Click a region to drill in`
- Add one dark compact `Reset` button at top right.

Below the header, use this desktop grid:

```css
grid-template-columns: minmax(180px,.62fr) minmax(300px,1.5fr);
gap:18px;
```

#### Country ranking list

- Rank every country in filtered Excel data by sales descending.
- Never limit it, never hide countries and never make it scrollable.
- Compact row: rank / country flag / country name with growth / sales amount.
- row padding `8px 9px`; 10px radius; 6px row gap;
- use flag emoji beside every country;
- positive growth over 5% is mint, below -5% coral, else blue;
- hover fill `#18233A`;
- selected row fill `#18233A`, 2px blue left border and violet country text;
- every row must be clickable.

#### Map background and dots

Use the attached image, embedded in the output HTML, as the exact map visual.
The map panel is 420px tall, `background:#0A101C`, `overflow:hidden`, and must
use `background-size:contain`; `background-position:center`;
`background-repeat:no-repeat`. Never replace the supplied image with a map
library, vector map or a different graphic. Never crop or distort it. Never
create a scrollbar.

Do not use country shape overlays. Use only absolutely positioned interactive
signal dots. Country positions are percentage coordinates in the map panel:

```js
const countryPositions = {
  "United States": [16.8, 31.7],
  "Canada": [15.0, 20.7],
  "Mexico": [13.4, 42.8],
  "Brazil": [22.5, 67.5],
  "United Kingdom": [32.6, 21.5],
  "Germany": [36.3, 22.8],
  "France": [34.3, 25.1],
  "South Africa": [37.9, 76.7],
  "India": [54.1, 43.2],
  "China": [62.3, 31.7],
  "Japan": [72.0, 30.2],
  "Australia": [72.0, 72.6]
};
```

Create a dot only when the country exists in both the filtered data and this
object. Keep other countries in the ranking list but do not invent their
geographic location.

Default dot properties:

```css
width:16px;
height:16px;
border:2px solid rgba(255,255,255,.85);
border-radius:50%;
box-shadow:0 0 0 5px rgba(255,255,255,.08),0 0 22px var(--signal);
transform:translate(-50%,-50%);
```

Dot colour is mint for growth above +5%, coral below -5%, blue otherwise. Hover
grows it to 1.35 scale.

Hover must reveal an in-map tooltip with country flag, country name, sales and
growth. Keep the tooltip inside map boundaries.

Clicking a dot or ranking row must select exactly that country:

- reset any prior selected dot;
- set selected dot colour to `#4D2CFA`;
- add white outline and violet glow to the selected dot itself;
- add two repeating expanding golden rings around that violet selected dot,
  using `#F6C453` (not violet, blue, white, mint or coral);
- mark matching ranking row selected;
- open a floating dark country detail card beside the dot;
- dynamically position the card left or right of dot and clamp it inside the
  panel;
- update lower-left summary.

Selection pulse must use this visual behaviour. The centre dot stays violet; the
expanding blinking rings are gold:

```css
@keyframes signalPulse {
  0% { transform:scale(.45); opacity:.85; }
  100% { transform:scale(2.5); opacity:0; }
}
```

The floating card is dark blue-black `rgba(10,22,36,.94)`, 14px radius, blur
backdrop, approximately 180px wide, 14px × 16px padding. It contains country
flag/name, Sales, growth, Profit and profit margin, then Top Category.

The fixed lower-left map detail panel is compact, dark translucent, 9px radius
with `#1B2234` border and must display:

```
[flag] [country] — Sales: [sales] · Growth: [growth] · Margin: [margin] · Orders: [orders]
```

Before selection, its exact content is:

```
Click a dot or country row to explore.
```

The Reset button must clear selected state, remove pulse, hide card, remove
selected ranking row and restore this exact default text.

### Mandatory map implementation contract — do not replace with a static map

The Country Market Explorer is a required interactive control, not a visual
element. The delivered HTML fails acceptance unless all four actions work:

1. hover a signal dot → tooltip opens and follows cursor;
2. click a signal dot → the matching dot becomes violet and pulses, matching
   country row highlights, country detail card opens;
3. click a country row → it performs the exact same selection behaviour and
   activates the matching dot;
4. click Reset → all selected state is cleared.

Build the map panel with these elements, with these IDs:

```html
<div id="mapPanel" class="map-panel">
  <div id="mapTip" class="map-tip"></div>
  <div id="dotCard" class="dot-card" style="display:none">
    <button id="dotCardClose" type="button" aria-label="Close country details">×</button>
    <div id="dotCardContent"></div>
  </div>
  <div id="mapDetail" class="map-detail">Click a dot or country row to explore.</div>
  <div id="mapLegend" class="map-legend">…</div>
</div>
```

After Excel data is parsed, dynamically add a real
`<button type="button" class="signal">` for every filtered country which has a
coordinate in `countryPositions`. Do not use pseudo-elements alone for the click
target. Every dot must have all three data attributes below:

```html
<button
  type="button"
  class="signal"
  id="sig-us"
  data-country="United States"
  data-sales=""
  data-growth=""
  aria-label="Explore United States">
</button>
```

Map country selection must be state-driven. Use one state value only:

```js
const state = {
  period: 'thisYear',
  category: 'All',
  selectedCountry: null
};
```

Every `render()` must do these things in this order:

```js
const model = calculateFilteredModel();
renderKpis(model);
renderCharts(model);
renderSignals(model);
renderCountryRankings(model);
renderMapDots(model);             // creates or refreshes real buttons
bindMapInteractionsOnce();        // adds events once, never duplicates them
if (state.selectedCountry) selectCountry(state.selectedCountry, model, false);
```

### Required event wiring

Use this exact interaction pattern. The country-name-to-dot relationship must be
created from `data-country`; do not use list index, rank or a hard-coded
selected country.

```js
function bindMapInteractionsOnce() {
  const panel = document.getElementById('mapPanel');
  const rankings = document.getElementById('rankings');
  const reset = document.getElementById('mapReset');
  const close = document.getElementById('dotCardClose');

  if (!panel.dataset.bound) {
    panel.dataset.bound = 'true';

    panel.addEventListener('pointerover', (event) => {
      const dot = event.target.closest('.signal[data-country]');
      if (!dot || !panel.contains(dot)) return;
      showMapTooltip(dot, event);
    });

    panel.addEventListener('pointermove', (event) => {
      const dot = event.target.closest('.signal[data-country]');
      if (!dot || !panel.contains(dot)) return;
      moveMapTooltip(event);
    });

    panel.addEventListener('pointerout', (event) => {
      const dot = event.target.closest('.signal[data-country]');
      if (!dot || !panel.contains(dot)) return;
      if (dot.contains(event.relatedTarget)) return;
      document.getElementById('mapTip').style.display = 'none';
    });

    panel.addEventListener('click', (event) => {
      const dot = event.target.closest('.signal[data-country]');
      if (!dot || !panel.contains(dot)) return;
      selectCountry(dot.dataset.country, calculateFilteredModel(), true);
    });
  }

  if (!rankings.dataset.bound) {
    rankings.dataset.bound = 'true';
    rankings.addEventListener('click', (event) => {
      const row = event.target.closest('.rank-row[data-country]');
      if (!row) return;
      selectCountry(row.dataset.country, calculateFilteredModel(), true);
    });
  }

  reset.onclick = () => clearCountrySelection();
  close.onclick = () => clearCountrySelection();
}
```

Each ranking row must be created with a country key, not a region key, and must
be a button or keyboard-accessible interactive element:

```html
<button type="button" class="rank-row" data-country="United States">
  …
</button>
```

### Required selection function

Implement `selectCountry()` so that it is the single source of truth for row
clicks and dot clicks:

```js
function selectCountry(country, model, scrollIntoView) {
  const countryData = model.countries[country];
  if (!countryData) return;

  state.selectedCountry = country;

  document.querySelectorAll('.signal.active').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.rank-row.is-selected').forEach(el => el.classList.remove('is-selected'));

  const dot = document.querySelector(`.signal[data-country="${CSS.escape(country)}"]`);
  const row = document.querySelector(`.rank-row[data-country="${CSS.escape(country)}"]`);

  if (dot) dot.classList.add('active');
  if (row) {
    row.classList.add('is-selected');
    if (scrollIntoView) row.focus({preventScroll:true});
  }

  renderCountryDetailCard(countryData, dot);
  renderMapDetail(countryData);
}
```

Selection CSS must be real and visible:

```css
.signal { position:absolute; z-index:10; cursor:pointer; }
.signal.active {
  --signal:#4D2CFA;
  border-color:#fff;
  transform:translate(-50%,-50%) scale(1.25);
  box-shadow:0 0 0 6px rgba(77,44,250,.20),0 0 36px #4D2CFA,0 0 60px #4D2CFA;
}
.signal.active::before,
.signal.active::after {
  content:"";
  position:absolute;
  inset:-9px;
  border:2px solid #F6C453;
  border-radius:50%;
  animation:signalPulse 2.2s ease-out infinite;
}
.signal.active::after { animation-delay:1.1s; }
.rank-row.is-selected {
  background:#18233A;
  border-left:2px solid #2B78FE;
}
.rank-row.is-selected .country { color:#4D2CFA; }
```

`renderMapDots(model)` must update default dot colour, country values and
`data-sales` / `data-growth` on every filter change. It must not delete click
handlers or overlay an invisible element above the dots. The map background must
have `pointer-events:none`; dots, tooltips, card and Reset button must have
`pointer-events:auto`.

```js
function renderMapDots(model) {
  const panel = document.getElementById('mapPanel');
  Object.entries(countryPositions).forEach(([country, [x, y]]) => {
    const metrics = model.countries[country];
    let dot = panel.querySelector(`.signal[data-country="${CSS.escape(country)}"]`);

    if (!metrics) {
      if (dot) dot.remove();
      return;
    }
    if (!dot) {
      dot = document.createElement('button');
      dot.type = 'button';
      dot.className = 'signal';
      dot.dataset.country = country;
      dot.setAttribute('aria-label', `Explore ${country}`);
      panel.appendChild(dot);
    }
    const colour = metrics.growth > 5 ? '#05DF96' : metrics.growth < -5 ? '#FA5A5A' : '#2B78FE';
    dot.style.left = `${x}%`;
    dot.style.top = `${y}%`;
    dot.style.setProperty('--signal', state.selectedCountry === country ? '#4D2CFA' : colour);
    dot.dataset.sales = formatCurrency(metrics.sales);
    dot.dataset.growth = formatGrowth(metrics.growth);
    dot.dataset.flag = metrics.flag;
    dot.classList.toggle('active', state.selectedCountry === country);
  });
}
```

Map tooltip must not be empty. It must show these values:

```js
function showMapTooltip(dot, event) {
  const tip = document.getElementById('mapTip');
  tip.innerHTML = `<b>${dot.dataset.flag} ${dot.dataset.country}</b><span>${dot.dataset.sales} · ${dot.dataset.growth} growth</span>`;
  tip.style.display = 'block';
  moveMapTooltip(event);
}

function moveMapTooltip(event) {
  const panel = document.getElementById('mapPanel');
  const tip = document.getElementById('mapTip');
  const r = panel.getBoundingClientRect();
  const x = Math.min(r.width - 170, Math.max(8, event.clientX - r.left + 14));
  const y = Math.min(r.height - 60, Math.max(8, event.clientY - r.top - 44));
  tip.style.left = `${x}px`;
  tip.style.top = `${y}px`;
}
```

Detail-card placement must use the selected dot's bounding rectangle and clamp
to map panel width/height. It must not be permanently hidden after rendering:

```js
function renderCountryDetailCard(metrics, dot) {
  const panel = document.getElementById('mapPanel');
  const card = document.getElementById('dotCard');
  const content = document.getElementById('dotCardContent');
  if (!dot) { card.style.display = 'none'; return; }

  content.innerHTML = `
    <div class="dot-card-region">${metrics.flag} ${metrics.country}</div>
    <div class="dot-card-grid">
      <div><div class="dot-card-label">Sales</div><div class="dot-card-value blue">${formatCurrency(metrics.sales)}</div></div>
      <div><div class="dot-card-label">Growth</div><div class="dot-card-value ${metrics.growth >= 0 ? 'mint' : 'coral'}">${formatGrowth(metrics.growth)}</div></div>
      <div><div class="dot-card-label">Profit</div><div class="dot-card-value pink">${formatCurrency(metrics.profit)}</div><div class="dot-card-sub">${metrics.margin.toFixed(1)}% margin</div></div>
      <div><div class="dot-card-label">Top Category</div><div class="dot-card-value category">${metrics.topCategory}</div></div>
    </div>`;
  card.style.display = 'block';
  const pr = panel.getBoundingClientRect();
  const dr = dot.getBoundingClientRect();
  const cardWidth = 188;
  let left = dr.left - pr.left + 18;
  if (left + cardWidth > pr.width - 8) left = dr.left - pr.left - cardWidth - 18;
  left = Math.max(6, left);
  const top = Math.min(pr.height - card.offsetHeight - 6, Math.max(6, dr.top - pr.top - 52));
  card.style.left = `${left}px`;
  card.style.top = `${top}px`;
}
```

Reset must execute exactly:

```js
function clearCountrySelection() {
  state.selectedCountry = null;
  document.querySelectorAll('.signal.active').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.rank-row.is-selected').forEach(el => el.classList.remove('is-selected'));
  document.getElementById('dotCard').style.display = 'none';
  document.getElementById('mapTip').style.display = 'none';
  document.getElementById('mapDetail').textContent = 'Click a dot or country row to explore.';
  renderMapDots(calculateFilteredModel());
}
```

Add keyboard support: Enter and Space on a focused country row or dot must call
`selectCountry()` for that country.

### Non-negotiable verification

Before returning the HTML, test it and fix every failure. Verify:

- no browser console error;
- no NaN, Infinity, undefined, hard-coded metric, broken tooltip or missing
  label;
- displayed totals reconcile to the workbook for default view;
- orders are distinct `Order ID` values;
- dynamic date range produces dynamic and accurate month labels;
- line/sparkline paths are smooth and monthly order bars are rounded;
- category and period filters re-render every data-driven element;
- every ranking row and every available dot select the correct country; test one
  dot and one row for at least United States, Canada, Germany and Australia;
- map image is visible, fully fitted and has no distortion, crop or scrollbar;
- flags are visible;
- hover every available map dot: tooltip must contain correct country, sales and
  growth;
- select a country from the list and then the map: in both cases, confirm that
  the exact same country dot becomes violet and the exact same two golden rings
  pulse around it;
- change the period dropdown from This Year to Last Year and back: confirm every
  period-dependent value, chart, country ranking and map metric re-renders
  accurately with no stale selection;
- confirm that the sidebar contains only the logo and `GLOBAL` label, with no
  menu or dead buttons;
- Reset clears selection, hides card and restores default map message;
- no alignment, clipping, collision or overflow occurs at desktop, tablet or
  mobile sizes.

Return the working `global_commerce_dashboard.html` file only.
