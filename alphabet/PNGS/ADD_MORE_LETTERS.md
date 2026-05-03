# How to Add Letter Images to alphabet.html

## Naming convention

Name each PNG after the **word you want displayed**, e.g.:

| File | Letter | Label shown |
|------|--------|-------------|
| `apple.png` | A | Apple |
| `ball.png` | B | Ball |
| `cat.png` | C | Cat |

- The **first letter of the filename** determines which alphabet letter it maps to.
- If you add multiple PNGs for the same letter (e.g. `ant.png` and `apple.png`),
  the script picks the first one alphabetically. Only one image per letter is embedded.
- Filenames must start with a lowercase letter a–z.

## Steps

### 1. Drop your PNG(s) into this folder (PNGS/)

### 2. Run the build script from the `alphabet/` directory:

```bash
python3 build_alphabet.py
```

Or from the project root:

```bash
python3 alphabet/build_alphabet.py
```

### 3. Open `alphabet.html` in a browser to verify

### 4. Commit and push

```bash
git add alphabet/
git commit -m "Add letter images: A, B, C"
git push origin main
```

## Notes

- Letters without a PNG show a large placeholder letter instead — no action needed.
- The HTML file grows ~1.3× the total size of your PNGs (base64 overhead).
- PNG files with transparency look best against the dark background.
- For best results on mobile, use square or portrait images (at least 400×400 px).
