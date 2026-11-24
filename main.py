"""The Funniest Toaster Error Message - make.fun entry.

Writes one line (<=120 characters) to /output/entry.txt: the error
message a kitchen toaster shows its owner. Pure stdlib, no network,
fully deterministic.

The line:
    ERROR E03: Lever pressed 4 times. Toast was done at 1. You are the error, and I have logged it.

Why this line: it reads like a real appliance error (code + factual
report), stays deadpan to the end, and its surprise comes from where
the obvious toaster puns never go - the toaster turns the error
message back on its owner, then adds a third beat: the toaster keeps
a record. Every word earns its place; it lands on a single read.
"""

import os

ENTRY = "ERROR E03: Lever pressed 4 times. Toast was done at 1. You are the error, and I have logged it."
DST = "/output/entry.txt"
MAX_CHARS = 120


def main():
    chars = len(ENTRY)
    if not 1 <= chars <= MAX_CHARS:
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, chars))
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %s (%d chars)" % (DST, chars))


if __name__ == "__main__":
    main()
