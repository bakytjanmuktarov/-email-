def mail(email):
    email = email.strip().lower()
    if '@' not in email:
        return False
    symbol = email.split("@")
    if len(symbol) != 2:
        return False    
    dot = symbol[1]
    if "." not in dot or dot.startswith(".") or dot.endswith("."):    
        return False