#!/usr/bin/env python3
"""One Line, No Deadline Met -- make.fun bounty entry.

The program picks the strongest single-line deadline excuse from a small
list of hand-written candidates, scoring each one against the judge's
published brief, and writes the winner to /output/entry.txt.

Scoring follows the brief's criteria, most important first:
  1. it really is a one-line excuse for a missed deadline,
  2. it is a real joke with a turn or a surprise, not a plain apology,
  3. it is a single sentence that reads cleanly aloud and lands its
     punch at the end,
  4. it sounds like something a person would actually say when cornered,
  5. the angle is fresh, not a stock dog-ate-it retread.

Deterministic: no network, no randomness, no wall clock. The same input
always produces the same output, so both grading runs agree.
"""

import os
import sys

# Hand-written candidate excuses. Each must be one sentence, one line,
# 1-200 characters, and actually excuse a missed deadline.
CANDIDATES = [
    "I finished it on time, but my laptop updated, restarted, and emailed "
    "you a blank file called final_FINAL_v2_I_mean_it_this_time \u2014 so "
    "the deadline died of embarrassment.",
    "I didn't miss the deadline, the deadline moved to Friday without "
    "leaving a note, and my calendar only told me after it had already "
    "filed the complaint.",
    "I left the deadline to future me, future me left it to past me, and "
    "past me is still on hold with IT, so at this point we're all just "
    "blaming each other.",
    "My to-do list and I had a falling out, it took the deadline with it "
    "in the divorce, and now it won't even return my calls.",
    "I was early for the wrong deadline, on time for a meeting that "
    "didn't exist, and somehow still late for this one \u2014 my calendar "
    "is gaslighting me.",
    "I treated the deadline like a software update and kept clicking "
    "remind me later until it gave up and installed itself on someone "
    "else's calendar.",
]

# Words that mark an angle the judge has not heard a hundred times.
FRESH_WORDS = (
    "embarrassment",
    "gaslighting",
    "divorce",
    "complaint",
    "ghosted",
    "blaming",
)

# Concrete, specific details: a named file, a named day, a named system.
CONCRETE_MARKERS = (
    "final_FINAL",
    "Friday",
    "IT",
    "remind me later",
)


def is_valid(text):
    """Hard gate, mirroring the sealed scorer: 1-200 chars, one line,
    not only whitespace, a single sentence, and really about a deadline."""
    if not text or text != text.strip():
        return False
    if len(text) > 200 or not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    if text.count(".") != 1 or not text.endswith("."):
        return False
    return "deadline" in text.lower()


def score(text):
    """Score one candidate against the brief. Higher is better."""
    points = 0
    # 3. Single sentence, clean read, punch at the end: reward the
    # sweet-spot length where a setup plus a punch fits (130-185 chars).
    length = len(text)
    if 130 <= length <= 185:
        points += 4
    elif 110 <= length <= 195:
        points += 2
    # A three-part escalation ("updated, restarted, and emailed") builds
    # the joke before the punch lands.
    if text.count(", ") >= 2 and " and " in text:
        points += 3
    # The punch: a twist clause after an em dash or a ", so" turn.
    if "\u2014" in text or ", so " in text:
        points += 3
    # 5. Fresh angle: uncommon words instead of stock excuse vocabulary.
    lowered = text.lower()
    for word in FRESH_WORDS:
        if word in lowered:
            points += 1
    # Concrete detail makes the excuse feel lived-in, not generic.
    for marker in CONCRETE_MARKERS:
        if marker in text:
            points += 2
    # 4. First person: sounds like a person cornered at their desk.
    if text.startswith("I ") or " I " in text:
        points += 1
    return points


def pick(candidates):
    """Return (best_text, [(text, score), ...]) for the valid candidates."""
    ranked = [(text, score(text)) for text in candidates if is_valid(text)]
    if not ranked:
        raise SystemExit("no valid candidate excuse")
    # Highest score wins; ties go to the longer, more developed joke,
    # then to the earliest candidate, so the choice is deterministic.
    ranked.sort(key=lambda item: (item[1], len(item[0]), -candidates.index(item[0])), reverse=True)
    return ranked[0][0], ranked


def main():
    best, ranked = pick(CANDIDATES)
    for text, points in ranked:
        print(f"{points:2d} pts | {len(text):3d} chars | {text}", file=sys.stderr)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(best)
    print(best)
    print(f"wrote {out_path} ({len(best)} characters)", file=sys.stderr)


if __name__ == "__main__":
    main()
