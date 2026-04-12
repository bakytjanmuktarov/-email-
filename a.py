def mail(email):
    email = email.strip().lower()
    if '@' not in email:
        return False