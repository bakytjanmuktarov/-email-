def mail(email):
    email = email.strip().lower()
    if '@' not in email:
        return False
    symbol = email.split("@")
    if len(symbol) != 2:
        return False    