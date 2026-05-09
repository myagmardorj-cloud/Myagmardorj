"""
run_all.py — One-command reproduction entry point
===================================================
Runs the full analysis pipeline in order:
  1. Main BK amplitude test (analyze.py)
  2. Null control suite (controls/run_all.py)
  3. Negative controls (controls/07_negative_controls.py)
  4. Robustness tests (controls/08_robustness_tests.py)
  5. Summary report

Usage:
  python scripts/run_all.py zeros3.txt

  If no file is given, attempts zeros3.txt, zeros2.txt, zeros4.txt
  in that order. Falls back to synthetic GUE data if none found.

Expected output (zeros3.txt):
  Main r  ≈ 0.9992
  Null r  ≈ 0.0 ± 0.2
  Negative controls: composite/random/GUE → r ≈ 0
  Robustness: r stable across N, prime cutoff variants

Computational observation only. Not a confirmed result.
Independent replication required.
"""

import sys
import os
import time
import subprocess

ZEROS_FILE = sys.argv[1] if len(sys.argv) > 1 else "zeros3.txt"

SEP  = "=" * 60
STAR = "✦"

def run(label, cmd, cwd=None):
    print(f"\n{SEP}")
    print(f"{STAR} {label}")
    print(SEP)
    t0 = time.time()
    result = subprocess.run(
        cmd, shell=True, cwd=cwd,
        capture_output=False, text=True
    )
    elapsed = time.time() - t0
    status = "OK" if result.returncode == 0 else f"EXIT {result.returncode}"
    print(f"\n[{status}] {elapsed:.1f}s")
    return result.returncode == 0


def main():
    print(SEP)
    print("BK Prime Correlation Study — Full Reproduction Pipeline")
    print("Experimental computational study — not a confirmed result")
    print(SEP)
    print(f"Zero file: {ZEROS_FILE}")
    print(f"Python:    {sys.version.split()[0]}")
    print()

    # Resolve zero file path for sub-scripts
    zf = os.path.abspath(ZEROS_FILE) if os.path.exists(ZEROS_FILE) else ZEROS_FILE

    results = {}
    controls_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..", "controls"
    )
    scripts_dir = os.path.dirname(os.path.abspath(__file__))

    # 1. Main analysis
    results["main"] = run(
        "Step 1 / 4 — Main BK Amplitude Test",
        f"python {os.path.join(scripts_dir, 'analyze.py')} {zf}"
    )

    # 2. Null controls (existing 01–06)
    results["controls"] = run(
        "Step 2 / 4 — Null Control Suite (01–06)",
        f"python run_all.py {zf}",
        cwd=controls_dir
    )

    # 3. Negative controls
    results["negative"] = run(
        "Step 3 / 4 — Negative Controls (composite, random phase, GUE)",
        f"python 07_negative_controls.py {zf}",
        cwd=controls_dir
    )

    # 4. Robustness
    results["robustness"] = run(
        "Step 4 / 4 — Robustness Tests (N, prime cutoff, normalization)",
        f"python 08_robustness_tests.py {zf}",
        cwd=controls_dir
    )

    # Summary
    print(f"\n{SEP}")
    print("REPRODUCTION SUMMARY")
    print(SEP)
    for name, ok in results.items():
        mark = "✓" if ok else "✗"
        print(f"  [{mark}] {name}")

    all_ok = all(results.values())
    print()
    if all_ok:
        print("All steps completed.")
        print("Compare r values against docs/REPRODUCIBILITY.md expected outputs.")
        print("Discrepancies? Open a GitHub Issue.")
    else:
        failed = [k for k, v in results.items() if not v]
        print(f"Steps with errors: {failed}")
        print("Check zero file path and Python environment.")
        print("See docs/REPRODUCIBILITY.md §Troubleshooting")

    print()
    print("CAVEATS:")
    print("  Computational observations only — not a confirmed result.")
    print("  Naive p-values assume independence (violated).")
    print("  Normalization choice is a known confound.")
    print("  Independent replication required before any strong claim.")
    print(SEP)


if __name__ == "__main__":
    main()
