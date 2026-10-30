---
title: test
author: Leonid Nemolovskyi
hidden: false
published_at: '2026-08-27T11:56:19.036Z'
---
<HTMLBlock>{`
<style>
/* Everything is scoped to .sf-announce — nothing touches the host page's html/body */
.sf-announce {
  --primary:     #034860;
  --primary-700: #023745;
  --secondary:   #00E0B8;
  --ink:         #10202E;
  --slate:       #5B7080;
  --line:        #DDE6EC;
  --white:       #FFFFFF;
  --warn-bg:     #FDF1DC;
  --warn-line:   #F4D79A;
  --warn-text:   #8A5A09;
  --font-sans:'Gilroy','Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
  width: 100%;
  max-width: 720px;
  margin: 24px 0;
}
.sf-announce *, .sf-announce *::before, .sf-announce *::after { box-sizing: border-box; }

.sf-announce__card {
  width: 100%;
  padding: 24px 26px;
  background: var(--white);
  border: 1px solid var(--line);
  border-radius: 14px;
  box-shadow: 0 1px 2px rgba(10,23,33,0.04), 0 6px 18px rgba(10,23,33,0.04);
}

.sf-announce__meta {
  margin: 0 0 14px;
  padding-bottom: 13px;
  border-bottom: 1px solid var(--line);
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  color: var(--slate);
}

.sf-announce__text {
  margin: 0;
  font-size: 1rem;
  line-height: 1.65;
  color: var(--ink);
  font-weight: 400;
  text-align: justify;
  text-justify: inter-word;
}
.sf-announce__text strong { font-weight: 600; color: var(--primary); }

.sf-announce__date {
  display: inline-block;
  font-weight: 700; font-size: 0.9375rem; line-height: 1;
  padding: 3px 9px; margin: 0 1px;
  border-radius: 6px;
  background: var(--warn-bg);
  color: var(--warn-text);
  border: 1px solid var(--warn-line);
  white-space: nowrap;
}

.sf-announce__cta {
  display: inline-block;
  margin-top: 18px;
  padding: 11px 20px;
  background: var(--primary);
  color: #FFFFFF !important;
  font-family: var(--font-sans);
  font-weight: 600; font-size: 0.9375rem; line-height: 1;
  border-radius: 9px;
  text-decoration: none !important;
  transition: background .15s ease, transform .15s ease, box-shadow .15s ease;
  box-shadow: 0 1px 2px rgba(3,72,96,0.18);
}
.sf-announce .sf-announce__cta:hover,
.sf-announce .sf-announce__cta:focus {
  background: var(--primary-700);
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(3,72,96,0.20);
  text-decoration: none !important;
}

/* Dark mode — scoped to the card only */
[data-color-mode="dark"] .sf-announce {
  --ink: #E8F5F0; --slate: #93A4B3; --line: #2A3A4D; --white: #14222F;
  --warn-bg: #2A1F05; --warn-line: #5A4410; --warn-text: #F4C463;
}
[data-color-mode="dark"] .sf-announce__card {
  box-shadow: 0 1px 2px rgba(0,0,0,0.30), 0 6px 18px rgba(0,0,0,0.28);
}
[data-color-mode="dark"] .sf-announce__text strong { color: var(--secondary); }
@media (prefers-color-scheme: dark) {
  html:not([data-color-mode="light"]) .sf-announce {
    --ink: #E8F5F0; --slate: #93A4B3; --line: #2A3A4D; --white: #14222F;
    --warn-bg: #2A1F05; --warn-line: #5A4410; --warn-text: #F4C463;
  }
  html:not([data-color-mode="light"]) .sf-announce__card {
    box-shadow: 0 1px 2px rgba(0,0,0,0.30), 0 6px 18px rgba(0,0,0,0.28);
  }
  html:not([data-color-mode="light"]) .sf-announce__text strong { color: var(--secondary); }
}

@media (max-width: 540px) {
  .sf-announce__card { padding: 18px 18px; border-radius: 12px; }
  .sf-announce__text { font-size: 0.9375rem; }
  .sf-announce__cta { width: 100%; text-align: center; }
}
</style>

<div class="sf-announce">
  <div class="sf-announce__card">
    <div class="sf-announce__meta">June 21, 2026</div>
    <p class="sf-announce__text">

      The Asset and SIM APIs are moving to a new multi-SIM model
      (<strong>Super SIM</strong> + <strong>PRO SIM</strong>). Legacy fields and
      endpoints are deprecated. To keep current integrations working during the
      transition, mirror fields are provided for backward compatibility, but they
      will also be removed on
      <span class="sf-announce__date">September 1, 2026</span>.
    </p>
    <a class="sf-announce__cta" href="https://docs.sixfab.com/reference/sixfab-api-migration-guide" target="_blank" rel="noopener">Full details in the API Migration Guide</a>
  </div>
</div>
`}</HTMLBlock>