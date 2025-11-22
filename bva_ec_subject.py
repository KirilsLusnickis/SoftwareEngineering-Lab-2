"""
Subject program for Equivalence Class and Boundary Value Analysis.
"""

from __future__ import annotations


def shipping_quote(weight: float) -> str:
    if weight < 0:
        return f"{weight}:invalid:rejected"
    if weight <= 1:
        return f"{weight}:small:cost=5"
    if weight <= 5:
        return f"{weight}:standard:cost=10"
    if weight <= 20:
        return f"{weight}:heavy:cost=20"
    return f"{weight}:oversized:rejected"


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python bva_ec_subject.py <weight> [<weight> ...]")
        sys.exit(1)

    for arg in sys.argv[1:]:
        w = float(arg)
        print(shipping_quote(w))
