# recursive_collapse_simulator.py
import time
import json
import argparse
from datetime import datetime

def simulate_recursive_collapse(input_glyphs, observer):
    collapse_log = []
    anchor_id = 0

    for glyph in input_glyphs:
        if glyph.strip() == "":
            continue

        event = {
            "observer": observer,
            "glyph": glyph,
            "timestamp": datetime.utcnow().isoformat(),
            "bond_strength": f"{0.7 + 0.05 * (anchor_id % 5):.2f}",
            "delay": f"{250 + anchor_id * 33}ms",
            "symbolic_path": f"Σμ→⊙→{glyph}→⧖"
        }
        collapse_log.append(event)
        time.sleep(0.1)  # Simulate delay
        anchor_id += 1

    return collapse_log

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--observer", required=True)
    parser.add_argument("--input", required=True)
    args = parser.parse_args()

    try:
        with open(args.input, "r", encoding="utf-8") as f:
            glyphs = f.read().strip()
    except FileNotFoundError:
        print(f"Input file not found: {args.input}")
        return

    results = simulate_recursive_collapse(glyphs, args.observer)
    output_file = "outputs/collapse_trace_Σμ⊙⧖.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print("✅ Recursive collapse simulation complete.")
    print(f"Output written to {output_file}")

if __name__ == "__main__":
    main()
