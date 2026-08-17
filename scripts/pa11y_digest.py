import json
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

if len(sys.argv) != 3:
    print("Usage: python3 pa11y_digest.py INPUT.json OUTPUT.md")
    sys.exit(1)

input_path = Path(sys.argv[1])
output_path = Path(sys.argv[2])

with input_path.open(encoding="utf-8") as file:
    report = json.load(file)

results = report.get("results", {})

if not isinstance(results, dict):
    print("Error: Expected a Pa11y CI report with a top-level 'results' object.")
    sys.exit(1)

findings_by_issue = defaultdict(list)
pages_with_findings = set()
total_findings = 0

for url, issues in results.items():
    if not isinstance(issues, list):
        continue

    for issue in issues:
        if not isinstance(issue, dict):
            continue

        code = issue.get("code", "No rule code")
        message = issue.get("message", "No message provided")
        issue_key = (code, message)

        findings_by_issue[issue_key].append({
            "url": url,
            "type": issue.get("type", "error"),
            "selector": issue.get("selector", ""),
            "context": issue.get("context", "")
        })

        pages_with_findings.add(url)
        total_findings += 1

pages_tested = report.get("total", len(results))
reported_errors = report.get("errors", total_findings)
reported_passes = report.get("passes", 0)

lines = [
    "# Pa11y Accessibility Audit Digest",
    "",
    f"- **Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
    f"- **Pages tested:** {pages_tested}",
    f"- **Pages with findings:** {len(pages_with_findings)}",
    f"- **Findings in report:** {total_findings}",
    f"- **Reported errors:** {reported_errors}",
    f"- **Reported passes:** {reported_passes}",
    f"- **Unique issue types:** {len(findings_by_issue)}",
    "",
    "> Automated findings require manual review and WCAG verification before creating or closing remediation work.",
    "",
    "## Findings by issue type",
    ""
]

if not findings_by_issue:
    lines.extend([
        "No automated findings were reported.",
        ""
    ])

for (code, message), occurrences in sorted(
    findings_by_issue.items(),
    key=lambda item: len(item[1]),
    reverse=True
):
    lines.extend([
        f"### {len(occurrences)} finding(s)",
        "",
        f"- **Rule:** `{code}`",
        f"- **Message:** {message}",
        ""
    ])

    for item in occurrences:
        lines.append(f"- **URL:** {item['url']}")

        if item["type"]:
            lines.append(f"- **Type:** {item['type']}")

        if item["selector"]:
            lines.append(f"- **Selector:** `{item['selector']}`")

        if item["context"]:
            context = " ".join(str(item["context"]).split())
            lines.append(f"- **HTML context:** `{context}`")

        lines.append("")

output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text("\n".join(lines), encoding="utf-8")

print(f"Created digest: {output_path}")
