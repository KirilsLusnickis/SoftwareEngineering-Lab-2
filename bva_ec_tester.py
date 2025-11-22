"""
Test harness for Equivalence Class & Boundary Value Analysis.
"""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from bva_ec_subject import shipping_quote


ROOT = Path(__file__).parent
INPUT_FILE = ROOT / "bva_input_data.txt"
EXPECTED_FILE = ROOT / "bva_expected_results.txt"
ACTUAL_FILE = ROOT / "bva_actual_results.txt"
REPORT_FILE = ROOT / "bva_comparison_report.txt"


def read_lines(path: Path) -> list[str]:
    return [line.strip() for line in path.read_text().splitlines() if line.strip()]


def write_lines(path: Path, lines: Iterable[str]) -> None:
    path.write_text("\n".join(lines) + "\n")


def run_tests() -> tuple[int, int]:
    if not INPUT_FILE.exists() or not EXPECTED_FILE.exists():
        raise FileNotFoundError(
            "Missing input or expected data files. Expected bva_input_data.txt and bva_expected_results.txt."
        )

    inputs = read_lines(INPUT_FILE)
    expected = read_lines(EXPECTED_FILE)

    if len(inputs) != len(expected):
        raise ValueError(
            f"Input count ({len(inputs)}) does not match expected result count ({len(expected)})."
        )

    actual_outputs: list[str] = []
    report_lines: list[str] = []
    passed = 0

    for index, (raw_value, expected_line) in enumerate(zip(inputs, expected), start=1):
        weight = float(raw_value)
        actual = shipping_quote(weight)
        actual_outputs.append(actual)

        if actual == expected_line:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"
        report_lines.append(
            f"#{index} input={weight} expected='{expected_line}' actual='{actual}' -> {status}"
        )

    write_lines(ACTUAL_FILE, actual_outputs)
    write_lines(REPORT_FILE, report_lines + [f"Summary: {passed}/{len(inputs)} passed."])

    for line in report_lines:
        print(line)
    print(f"Summary: {passed}/{len(inputs)} passed. See {REPORT_FILE.name} for details.")

    return passed, len(inputs)


if __name__ == "__main__":
    run_tests()
