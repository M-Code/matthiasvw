"""
build_alphabet.py
─────────────────
Reads all PNGs from the PNGS/ folder, embeds them as base64 into alphabet.html.

PNG NAMING CONVENTION:
  Name each file after the word you want displayed, e.g.:
    apple.png   → letter A, label "Apple"
    ball.png    → letter B, label "Ball"
    cat.png     → letter C, label "Cat"

  The first letter of the filename determines which alphabet letter it belongs to.
  If multiple PNGs share the same starting letter, the script picks the first
  one alphabetically. Only one image per letter is embedded.

USAGE:
  Run from inside the alphabet/ directory:
    python3 build_alphabet.py

  Or from the project root:
    python3 alphabet/build_alphabet.py
"""

import base64, os, re, sys

# Resolve paths relative to this script's location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PNG_DIR    = os.path.join(SCRIPT_DIR, 'PNGS')
HTML_FILE  = os.path.join(SCRIPT_DIR, 'alphabet.html')

# ── Collect PNGs ──────────────────────────────────────────────────────────────
png_files = sorted(
    f for f in os.listdir(PNG_DIR)
    if f.lower().endswith('.png') and not f.startswith('.')
)

# Map first letter → (filename, word)
letter_map = {}
for f in png_files:
    name   = os.path.splitext(f)[0]          # e.g. "apple"
    letter = name[0].lower()                  # e.g. "a"
    word   = name.capitalize()                # e.g. "Apple"
    if letter not in letter_map:              # first match wins (alphabetical)
        letter_map[letter] = (f, word)

print(f'Found {len(letter_map)} letter(s) with images: '
      f'{", ".join(sorted(letter_map)).upper()}')

# ── Build JS object entries ───────────────────────────────────────────────────
entries = []
for letter in sorted(letter_map):
    filename, word = letter_map[letter]
    path = os.path.join(PNG_DIR, filename)
    with open(path, 'rb') as fh:
        b64 = base64.b64encode(fh.read()).decode()
    entries.append(
        f"  '{letter}': {{ src: 'data:image/png;base64,{b64}', word: '{word}' }}"
    )

if entries:
    images_js = 'const images = {\n' + ',\n'.join(entries) + '\n  };'
else:
    images_js = 'const images = {};'

# ── Inject into HTML ──────────────────────────────────────────────────────────
with open(HTML_FILE, 'r', encoding='utf-8') as fh:
    html = fh.read()

new_block = f'/* BEGIN_IMAGES */\n  {images_js}\n  /* END_IMAGES */'
html, count = re.subn(
    r'/\* BEGIN_IMAGES \*/.*?/\* END_IMAGES \*/',
    new_block,
    html,
    flags=re.DOTALL
)

if count == 0:
    print('ERROR: BEGIN_IMAGES / END_IMAGES markers not found in alphabet.html.')
    print('Make sure the markers are present and have not been edited.')
    sys.exit(1)

# Safety check
assert 'stage' not in html or True  # placeholder; real checks below
assert '/* BEGIN_IMAGES */' in html, 'marker missing after write!'
assert '</html>' in html, 'HTML truncated!'

with open(HTML_FILE, 'w', encoding='utf-8') as fh:
    fh.write(html)

size_kb = os.path.getsize(HTML_FILE) / 1024
print(f'Done. {len(entries)} image(s) embedded. File size: {size_kb:.0f} KB')
