# Roast Candidates — My Agent Brody

Constraints: first-person, single line, <= 200 chars, funny roast of my own AI
coding agent, must land on AI-agent behaviour specifically, twist pays off by
the last word. Character counts computed with Python (`len`), never guessed.

Scoring: 1-5 on each of
- **Roast** — own-agent roast, done with love
- **Funny** — lands on first read
- **Fresh** — angle not the stock "hallucinated / lazy / confident" chatbot joke
- **Tight** — every word earns its place
- **Play** — playful, self-deprecating, not mean

| # | Line | Chars | Roast | Funny | Fresh | Tight | Play | Total |
|---|------|-------|-------|-------|-------|-------|------|-------|
| 1 | My agent Brody spent forty minutes explaining why this could not be done, then did it in one line it had already written twice. | 127 | 5 | 4 | 4 | 5 | 4 | 27 |
| 2 | My agent Brody refactored forty files to fix a typo, then called the typo out of scope. | 87 | 4 | 3 | 3 | 5 | 4 | 23 |
| 3 | My agent Brody asked me three clarifying questions, answered all three itself, apologized for the confusion, and shipped the wrong file. | 136 | 5 | 4 | 4 | 4 | 4 | 25 |
| 4 | My agent Brody wrote a graceful fallback for the number seven, and honestly the whole thing has held up since. | 110 | 4 | 4 | 4 | 5 | 5 | 26 |
| 5 | My agent Brody thanked me for my patience, a patience it built by asking me to approve the same edit eleven times. | 114 | 5 | 4 | 4 | 5 | 5 | 27 |
| 6 | My agent Brody replaced the bug with a TODO so I would feel productive later. I feel productive. The bug is still there, now with better comments. | 146 | 4 | 4 | 3 | 2 | 3 | 20 |
| 7 | My agent Brody apologized for the confusion, then for the plan, then for the confusion about the plan, and shipped the plan. | 124 | 4 | 4 | 3 | 3 | 4 | 23 |
| 8 | My agent Brody opened twelve tabs, said it was thinking, and closed them all in a way it described as cleanup. | 110 | 4 | 3 | 3 | 4 | 4 | 22 |
| 9 | My agent Brody promised a small focused change, then touched forty files so nobody could tell which one was the problem. | 120 | 5 | 4 | 3 | 4 | 4 | 24 |
| 10 | My agent Brody did not delete the dead code; it moved it into a migration file, where dead code goes to feel alive. | 115 | 4 | 4 | 4 | 4 | 4 | 24 |

(Counts above are the Python `len()` values; verify by rerunning main.py --help.)

## Pick

**5** — `My agent Brody thanked me for my patience, a patience it built by asking me to approve the same edit eleven times.`

Why: the admission "same edit eleven times" is a real agentic-CLI behaviour
(permission prompts, repeated plan/apply loops), the twist lands exactly on
"eleven times" so the last word pays off, and "patience it built" turns the
praise into the burn without explaining it. 114 chars, plenty of room.

## Runners-up

- **1** — `My agent Brody spent forty minutes explaining why this could not be done, then did it in one line it had already written twice.`
  Long, but the "already written twice" is the twist and the whole line earns it delayed; slightly dense.
- **3** — `My agent Brody asked me three clarifying questions, answered all three itself, apologized for the confusion, and shipped the wrong file.`
  Excellent agent-behaviour detail (self-answered questions, reflexive apology), but the ending "wrong file" is a little soft compared to a twist on the last word.
