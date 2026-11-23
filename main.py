"""One Letter: Coffee or Tea (burn entry).

Writes exactly one letter to /output/entry.txt: "A" for coffee.
Coffee is the vivid choice: the morning ritual that turns a person
back on, the "don't talk to me before coffee" stance — alive,
desperate, honest. Tea is calm; coffee has a personality.
"""

import os

LETTER = "A"  # A = coffee, B = tea


def main():
    # Gate: entry must be exactly 1 character, A or B, not whitespace.
    assert len(LETTER) == 1, "entry must be exactly one letter"
    assert LETTER in ("A", "B"), "letter must be A (coffee) or B (tea)"
    assert not LETTER.isspace(), "entry must not be whitespace only"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Read-back: byte-identical, no trailing newline.
    with open(path, "rb") as f:
        data = f.read()
    assert data == LETTER.encode("utf-8"), "read-back mismatch"
    assert len(data) == 1, "entry must be exactly 1 byte"
    print(f"wrote {len(data)} byte")


if __name__ == "__main__":
    main()
