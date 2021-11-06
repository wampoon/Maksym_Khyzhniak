def first_non_repeating_letter(s):
    for c in s:
        if s.index(c.upper()) == s.rindex(c.upper()):
            return c
    return None