"""One funny one-line review a dog gives the mailman.

Writes exactly one line to entry.txt in the output dir read from
MAKEFUN_OUTPUT_DIR (fallback /output). The review is a single line of
under 200 characters, in the dog's own voice.
"""

import os

LINE = (
    "One star. He comes every day, teases me through the fence, and still "
    "has never once brought me a single treat \u2014 I have barked at the door "
    "for three years and he acts like I'm the rude one."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
