# Notes (Optional)

This file is optional.

Use it only if you want to provide **additional context** for the reviewer that does not fit cleanly in `submission_template.md`.

Examples of appropriate use:
- Assumptions you made
- Known limitations of your solution
- Alternative approaches you considered but did not implement

Do not repeat information already included in `submission_template.md`.

Remove the contents of this file and write your notes.

## Note on Task 2(Count Valid Emails) — Average of Valid Measurements
We can use alternative Regex Simplification We can simplify the task by using the builtin regex library expression.
```py
import re

def count_valid_emails(emails):
    if not emails:
        return 0
    count = 0

    # Matches: non-whitespace + @ + non-whitespace + . + non-whitespace
    email_pattern = r"^\S+@\S+\.\S+$"
    for email in emails:
        if isinstance(email, str) and re.match(email_pattern, email):
            count += 1
    return count
```