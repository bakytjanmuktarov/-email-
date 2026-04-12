def mail(email):
    email = email.strip().lower()
    if '@' not in email:
        return False
    a = email.split("@")
    if len(a) != 2:
        return False
    b = a[1]
    if "." not in b or b.startswith(".") or b.endswith("."):
        return False
    return True
    print("ПРОВЕРКА EMAIL")
    while True:
        x = input("Введите email (или 'выход' для того что бы выйти): ")