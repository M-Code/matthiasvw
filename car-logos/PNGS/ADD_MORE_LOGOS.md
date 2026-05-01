# How to Add More Car Logos to car-logos.html

This file explains how to add new PNG logos to the standalone `car-logos.html` slideshow.

## How the HTML works

All images are embedded directly inside `car-logos.html` as base64-encoded data URIs stored in a JavaScript array called `logos`. There are no external image references — the HTML file is fully self-contained. Tapping anywhere on the page randomly advances to a different logo.

---

## Steps to add a new PNG

### 1. Place the new PNG in this folder

Drop the new `.png` file into this directory (`Matts_Car_Logos/`).

### 2. Convert it to base64

Run this in a terminal from this folder:

**macOS / Linux / Git Bash (Windows):**
```bash
base64 -w 0 your-new-logo.png
```

**Python (cross-platform):**
```python
import base64
with open("your-new-logo.png", "rb") as f:
    print(base64.b64encode(f.read()).decode())
```

Copy the output string.

### 3. Add it to the logos array in car-logos.html

Open `car-logos.html` in a text editor. Find the `logos` array near the bottom of the file — it looks like this:

```js
const logos = [
  "data:image/png;base64,iVBORw0KGgo...",
  "data:image/png;base64,iVBORw0KGgo...",
  ...
];
```

Add a new entry at the end of the array (before the closing `]`):

```js
const logos = [
  "data:image/png;base64,<existing data>",
  ...
  "data:image/png;base64,<paste your new base64 string here>"
];
```

Make sure each entry is separated by a comma except the last one.

### 4. Save and test

Open `car-logos.html` in a browser and tap/click to verify the new logo appears in rotation.

---

## Doing it all at once with Python (recommended for bulk adds)

If you have multiple new PNGs, use this script from inside the `Matts_Car_Logos/` folder. It reads every PNG in the folder and rewrites the entire `car-logos.html` from scratch:

```python
import base64, os, re

png_files = sorted(f for f in os.listdir('.') if f.lower().endswith('.png'))

entries = []
for f in png_files:
    with open(f, 'rb') as fh:
        data = base64.b64encode(fh.read()).decode()
    entries.append(f'"data:image/png;base64,{data}"')

logos_js = 'const logos = [\n  ' + ',\n  '.join(entries) + '\n];'

with open('car-logos.html', 'r') as fh:
    html = fh.read()

html = re.sub(r'const logos = \[.*?\];', logos_js, html, flags=re.DOTALL)

with open('car-logos.html', 'w') as fh:
    fh.write(html)

print(f'Done — {len(png_files)} logos embedded.')
```

Run it whenever you add or remove PNGs and it will keep the HTML in sync automatically.

---

## Notes

- PNG files with transparency work best against the black background.
- There is no maximum number of logos, but file size grows with each addition (~50–200 KB per logo is typical).
- The slideshow never shows the same logo twice in a row.
- The HTML file can be opened directly in any browser or sent to a phone — no server needed.
