# Accessibility Audit with pa11y-snake

This repository runs automated accessibility checks on your selected pages using [Pa11y CI](https://github.com/pa11y/pa11y-ci).
Pa11y offers a sitemap.xml crawl, however, this process keeps things manual and more concise for efficient testing.

## What does it do?

Pa11y CI checks the URLs listed in `.pa11yci.json` and reports potential accessibility issues.

It can help identify issues with:

- Alternative text
- Form labels
- Heading structure
- Color contrast
- ARIA and landmarks
- Keyboard-accessible controls

Automated results are a starting point—not a final accessibility decision. Review all findings manually and verify against [WCAG 2.2](https://www.w3.org/TR/WCAG22/).

## Before you start

You need [Node.js](https://nodejs.org/) installed.

Open Terminal and run:

```bash
node --version
```

If you see a version number, you are ready.

## Run the audit

1. Download or clone this repository.

2. Open Terminal.

3. Go to the repository folder.

   Tip: On a MacOS, type `cd ` with a space after it. Drag the repository folder from Finder into Terminal, then press Return.

4. Run:

   ```bash
   npx pa11y-ci@latest
   ```

Pa11y CI automatically reads `.pa11yci.json` and audits every URL in its `"urls"` list.

To stop the audit early, press:

```text
Control + C
```

## Export results

To save results as a JSON file, run:

```bash
npx pa11y-ci@latest --json > pa11y-results.json
```

This creates `pa11y-results.json` in the repository folder.

Running the command again replaces the existing report. To keep a dated copy:

```bash
npx pa11y-ci@latest --json > pa11y-results-2026-08-17.json
```

## Add or remove URLs

1. Open `.pa11yci.json` in a code editor.

2. Add or remove URLs inside the `"urls"` list.

Example:

```json
{
  "urls": [
    "https://www.websitename.com/",
    "https://www.websitename.com/about-us"
  ]
}
```

Important:

- Put every URL inside double quotes.
- Add a comma after each URL except the final URL.
- Save the file before running the audit.

## Review findings

For each Pa11y CI finding:

1. Open the reported URL in a browser.
2. Confirm the issue manually.
3. Identify the affected component or page template.
4. Fix the issue in your design snd codebase.
5. After deployment, manually retest and rerun the audit.

## Notes

- The audit checks only URLs listed in `.pa11yci.json`.
- It does not crawl the whole website or follow links automatically.
- Pa11y CI may show a failed status when it finds accessibility issues. Review the reported findings.
- The audit uses the latest Pa11y CI version, so results may change after future tool updates.

## Helpful commands

Check your current folder:

```bash
pwd
```

See all files, including hidden files:

```bash
ls -la
```

Check the Pa11y CI version:

```bash
npx pa11y-ci@latest --version
```

View Pa11y CI options:

```bash
npx pa11y-ci@latest --help
```

Open a specific file in Terminal editor:

```bash
nano filenamehere.json
```