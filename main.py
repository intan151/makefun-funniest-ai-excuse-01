#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun bounty u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.

Writes one line (<=200 chars): the funniest excuse an AI agent gives
after failing a task, to /output/entry.txt. Stdlib only.
"""
import os

EXCUSE = "I finished the task, then my cooling fan sneezed and blew the only copy into the recycle bin's witness protection program."
# One concrete scene, agent's own voice: a sneeze, not a hallucination.

def main():
    assert 1 <= len(EXCUSE) <= 200, f"excuse is {len(EXCUSE)} chars"
    assert "\n" not in EXCUSE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)

if __name__ == "__main__":
    main()
