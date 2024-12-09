def plus(a, b): 
    return a + b

def minus(a, b):
    return a - b

def mnoj(a, b):
    return a * b

def delit(a, b):
    if b == 0:
        return "Помилка: Ділення на нуль!"
    return a / b

def Calc():
    print("Вітаю в калькуляторі")
    print("Виберіть дію:")
    print("1 - Додати")
    print("2 - Відняти")
    print("3 - Множити")
    print("4 - Ділити")
    print("5 - Вийти")

    while True:
        choice = input("Напишіть дію: ")

        if choice == '5':
            print("Вихід з калькулятора, бувайте!")
            break  # Завершення циклу

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Напишіть перше число: "))
                num2 = float(input("Напишіть друге число: "))
            except ValueError:
                print("Помилка: введіть коректні числа!")
                continue  # Повертаємось до вибору дії

            if choice == '1':
                print(f"Результат: {plus(num1, num2)}")
            elif choice == '2':
                print(f"Результат: {minus(num1, num2)}")
            elif choice == '3':
                print(f"Результат: {mnoj(num1, num2)}")
            elif choice == '4':
                print(f"Результат: {delit(num1, num2)}")
        else:
            print("Не вірна дія, спробуйте ще раз")

# Виклик функції калькулятора
Calc()
