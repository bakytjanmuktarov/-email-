def mail(email):
    email = email.strip().lower()
    if '@' not in email:
        return False
    symbol = email.split("@")
    if len(symbol) != 2:
        return False   
    if len(symbol[0]) == 0 or len(symbol[1]) == 0:
        return False 
    dot = symbol[1]
    if "." not in dot or dot.startswith(".") or dot.endswith(".") or ".." in dot:    
        return False
    for char in dot:
        if char.isdigit():
            return False
    rus="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    for char in email:
        if char in rus:
            return False
    return True
print("===============================ПРОВЕРКА EMAIL================================")
while True:
    user = input("Введите email (или 'выход' для того что бы выйти): ")
    if user.lower() in ['выход']: 
        print("Пока, спасибо что использовали мой код") 
        break    
    if mail(user):
        print("✅Ваш email:",user.strip(),"корректен!")
    else:   
        print("❌ОШИБКА:", user , "не является правильным email.")