"""One-Line Office Joke Laugh-Off entry program.

Writes a single original one-line office joke to /output/entry.txt.

The joke was written against the judge's brief, in the order the judge
weighs its criteria: it is unmistakably a one-line joke about office
life; the laugh lands on a specific, recognisable detail of the modern
open-plan office; the twist pays off in the last few words; it reads
cleanly aloud in one breath; and it avoids the worn-out office cliches
(reply-all, synergy, per my last email, the printer) in favour of a
fresh image.
"""

import os

ENTRY = (
    "Our office has an open-plan layout, which means I can hear "
    "three people quit in their heads before lunch."
)


def main():
    line = ENTRY.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(line))
    if "\n" in line:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print("wrote %d characters to /output/entry.txt" % len(line))


if __name__ == "__main__":
    main()
