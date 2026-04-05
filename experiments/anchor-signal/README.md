# anchor-signal

First live experiment for `lab`.

`anchor-signal` scans the five Class A anchors and prints a small signal map of their current local footprint.

## Why this exists

This is a real experiment, not a placeholder.
It gives `lab` an immediately runnable artifact while staying true to the repo role:
- public
- directional
- unstable-friendly
- useful for seeing the field shape as it changes

## What it measures

For each anchor repo:
- total non-git files
- executable file count
- README presence
- latest.txt presence
- a simple signal score

## Run

    python3 scan.py

## Output

- plain-text table
- JSON summary
- latest.txt snapshot

## Notes

This is not a final observability system.
It is an early experimental probe of anchor density and visible field shape.
