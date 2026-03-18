def analyze_password(password, min_length=8,
                     require_digit=True,
                     require_upper=True,
                     require_symbol=False,
                     banned_words=None):
    is_strong = True
    missing_rules = []
    score = 0
    if len(password) < min_length:
        is_strong = False
        missing_rules.append(password)
    else:
        score += 1
    if require_digit:
        if password.isdigit():
            score += 1
        else:
            missing_rules.append(password)
            is_strong = False
    score_percent = (score / 2) * 100
    return is_strong, score_percent, missing_rules

print(analyze_password("kocka123"))

