def mail(email):
    email = email.strip().lower()
    if '@' not in email:
        return False
    a = email.split("@")
    if len(a) != 2:
        return False