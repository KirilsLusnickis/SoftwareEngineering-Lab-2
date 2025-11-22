# Equivalence Class & Boundary Value Analysis Test Report

## Task
Create a black‑box test harness that demonstrates **Equivalence Class (EC) Partitioning** and **Boundary Value Analysis (BVA)**. The subject program must read test inputs from a file, produce real outputs to a file, and compare them against expected results.

## Subject Under Test
- File: `bva_ec_subject.py`
- Behavior: `shipping_quote(weight: float) -> str` maps package weights (kg) into tariff categories and costs.
- Input domain classes & boundaries:
  - invalid: `weight < 0`
  - small: `0 ≤ weight ≤ 1`
  - standard: `1 < weight ≤ 5`
  - heavy: `5 < weight ≤ 20`
  - oversized: `weight > 20`

## Test Design (EC + BVA)
- Equivalence classes: the five intervals above, plus the invalid class.
- Boundary values exercised: `-1, 0, 0.5, 1, 1.1, 5, 5.1, 20, 20.1` (covers both sides of each boundary at 0, 1, 5, 20).
- Each test case asserts the full formatted output string `"<weight>:<class>:<outcome>"`.

### Sample Equivalence Classes and Boundary Value Analysis
Breaking the input domain (weight in kg) into ECs and probing their borders:

```
![Runner output](SoftwareEngineering-Lab-2/Lab2Graph.png)
Boundaries hit: -1 | 0 | 1 | 5 | 20 | 20.1
Representative interiors: 0.5 (small), 1.1 (standard), 5.1 (heavy)
```

Test case mapping (EC/BVA coverage):
- `-1` → invalid class, below lower bound.
- `0` → lower boundary of small.
- `0.5` → interior of small.
- `1` → upper boundary of small.
- `1.1` → just above boundary into standard.
- `5` → upper boundary of standard.
- `5.1` → just above boundary into heavy.
- `20` → upper boundary of heavy.
- `20.1` → just above boundary into oversized.

## Test Assets
- `bva_input_data.txt` – weights to feed the program.
- `bva_expected_results.txt` – oracle outputs for each input.
- `bva_ec_tester.py` – reads inputs, runs the subject, writes `bva_actual_results.txt`, and produces `bva_comparison_report.txt`.

## Running the Tests
From the repository root:

```bash
python3 bva_ec_tester.py
```

Outputs produced:
- `bva_actual_results.txt` – real outputs.
- `bva_comparison_report.txt` – per‑case verdicts and summary.

## Results (run on 2025-11-22)
Summary: **9/9 test cases passed.**
Example lines:
```
#1 input=-1.0 expected='-1.0:invalid:rejected' actual='-1.0:invalid:rejected' -> PASS
#8 input=20.0 expected='20.0:heavy:cost=20' actual='20.0:heavy:cost=20' -> PASS
Summary: 9/9 passed.
```

## Conclusions
- Advantages: minimal test set achieves wide coverage of input domain; boundaries explicitly checked; fully black‑box (no code introspection needed).
- Disadvantages: does not reveal internal path issues unrelated to input partitions; expanding domains adds more boundary cases; still requires a reliable oracle file.

## Files Overview
- Subject: `bva_ec_subject.py`
- Harness: `bva_ec_tester.py`
- Input: `bva_input_data.txt`
- Expected: `bva_expected_results.txt`
- Actual run: `bva_actual_results.txt`
- Report: `bva_comparison_report.txt`
