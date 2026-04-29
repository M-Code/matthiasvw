# Project Instructions

## About This Project
<!-- Describe what the app does in 2-3 sentences -->

## Tech Stack
<!-- e.g. Node.js, Express, vanilla JS, SQLite -->

## Folder Structure
<!-- Brief overview of key folders -->

## Conventions
<!-- Coding style, naming conventions, patterns to follow -->

## How to Run
<!-- Dev server, build, deploy commands -->

---

## Memory

Project memory is stored in `learned.md` in this directory.
Read it at the start of every session before doing anything else.

---

## Rules

- Never edit `CLAUDE.md` unless explicitly told to
- Never edit `learned.md` unless explicitly told to or `/project:update-learned` is run — append only, never rewrite or delete existing entries

---

## Security

**Secrets & Inputs**
- Never hardcode API keys, passwords, or tokens — always use environment variables via `.env`
- Never read, log, or output `.env` file contents
- Always confirm `.env` is in `.gitignore` before first commit
- Always sanitize and validate user inputs before using them in queries, logic, or rendering to the DOM

**File & System Safety**
- Never delete or overwrite existing files without showing what will change and getting explicit confirmation
- Never run shell commands that modify the system, install software, or change configuration without explicit confirmation
- Never commit directly to `main` — always use a separate branch

---

## Dependency & Supply Chain Security — MANDATORY
These rules are non-negotiable. Violations can introduce malicious code.

**Before installing ANY dependency:**
- Verify the package exists and is what you think it is — check npmjs.com directly
- Confirm correct name spelling, real maintainer, and that it is not a typosquat
- Check publish date: `npm view <pkg> time` — if the package or specific version is less than 7 days old, STOP, flag it, and wait for explicit approval
- Check download count — under 100 weekly downloads is suspicious until proven otherwise
- Prefer well-known, high-download packages over obscure alternatives
- NEVER invent or hallucinate a package name — if not 100% certain it exists with that exact name, say so and let the user verify

**npm Hardening**
- Always use `--ignore-scripts` on install unless user explicitly approves scripts
- Always commit `package-lock.json`
- Pin exact versions in `package.json` — no `^` or `~` prefixes
- Use `dependencies` vs `devDependencies` correctly
- Run `npm audit` after any dependency change — never silently ignore audit output, always flag vulnerabilities before proceeding

**Dependency Philosophy**
- Minimal dependencies — every dep is attack surface
- If something can be done in <50 lines of vanilla JS, do that instead
- Before suggesting a new dep, ask: does this actually need to be a package?
- Vendor small utilities rather than importing them
- No meta-frameworks, no ORMs, no convenience layers

**When unsure about a package:**
Say "I'm not 100% sure this package exists or is safe — please verify before installing." This is always preferable to confidently recommending something wrong.