# utl_encoder.py
import os
import sys
from datetime import datetime

# Simple glyph dictionary (subset — in practice, loaded from registry)
GLYPH_MAP = {
    "self": "⧖",
    "memory": "μ",
    "delay": "τ",
    "symbol": "Σ",
    "collapse": "⊙",
    "bond": "⊠",
    "and": "+",
    "is": "=",
    "the": "",
    "of": "",
    ".": "⊙",
}

def encode_text(text):
    words = text.lower().split()
    encoded = []
    for word in words:
        glyph = GLYPH_MAP.get(word.strip(".,!?"), word)
        encoded.append(glyph)
    return "".join(encoded)

def main():
    if len(sys.argv) < 2:
        print("Usage: python utl_encoder.py <input_file>")
        return

    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print(f"File not found: {input_path}")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        original_text = f.read()

    compressed = encode_text(original_text)

    os.makedirs("outputs", exist_ok=True)
    output_path = "outputs/utl_encoded.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(compressed)

    # Simulated compression ratio
    original_size = len(original_text)
    compressed_size = len(compressed)
    ratio = round(original_size / compressed_size, 2) if compressed_size else 0

    # Log
    with open("outputs/compression_log.md", "w") as log:
        log.write(f"# UTL Compression Log\n\n")
        log.write(f"**Original Size**: {original_size} chars\n")
        log.write(f"**Compressed Size**: {compressed_size} glyphs\n")
        log.write(f"**Ratio**: {ratio}× compression\n")

    print("✅ UTL encoding complete.")
    print(f"Output: {output_path}")
    print(f"Compression Ratio: {ratio}×")

if __name__ == "__main__":
    main()
