# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.

def count_valid_emails(emails):
    if not emails:
        return 0

    count = 0

    for email in emails:
        if not isinstance(email, str):
            continue
        if email.count("@") != 1:
            continue
            
        try:
            user_part, domain_part = email.split("@")
        except ValueError:
            continue

        if not user_part or not domain_part:
            continue
        if "." not in domain_part or domain_part.startswith(".") or domain_part.endswith("."):
            continue

        count += 1

    return count