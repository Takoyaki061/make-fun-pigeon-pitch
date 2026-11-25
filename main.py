"""Pigeon Pitch, One Line — entry for make.fun competition
u-donrulezz-pigeon-pitch-one-line-af06c6cf.

Writes one line (<= 200 chars, English): the elevator pitch a city
pigeon gives to investors for its startup. Stdlib only.
"""

import os

PITCH = (
    "Investors, CrumbCoin is the only currency backed by real "
    "breadcrumbs \u2014 inflationary by design, because I eat the reserve. "
    "Burn rate: one crust a week. "
    "Our Series A is a bagel I haven't found yet."
)


def main() -> None:
    text = PITCH.strip()
    assert text, "pitch must not be blank"
    assert "\n" not in text, "pitch must be a single line"
    assert 1 <= len(text) <= 200, f"pitch must be 1-200 chars, got {len(text)}"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
