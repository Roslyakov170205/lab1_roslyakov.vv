from task_1 import Book, Tree, BankAccount  # Импортируем созданные ранее классы

if __name__ == "__main__":
    # Создаем объекты классов
    book = Book("1984", "George Orwell", 328)
    tree = Tree("Oak", 15.5, 50)
    account = BankAccount("12345678", 1000.0)

    # Проверка метода с некорректными аргументами для класса Book
    try:
        book.read_pages(-5)  # Некорректный аргумент (отрицательное число)
    except ValueError as e:
        print(f"Ошибка в классе Book: {e}")

    # Проверка метода с некорректными аргументами для класса Tree
    try:
        tree.grow(-2)  # Некорректный аргумент (отрицательное число)
    except ValueError as e:
        print(f"Ошибка в классе Tree: {e}")

    # Проверка метода с некорректными аргументами для класса BankAccount
    try:
        account.withdraw(-500.0)  # Некорректный аргумент (отрицательное число)
    except ValueError as e:
        print(f"Ошибка в классе BankAccount: {e}")

    # Проверка некорректных данных при создании экземпляра класса
    try:
        invalid_book = Book("Title", "Author", -100)  # Некорректный аргумент (отрицательные страницы)
    except ValueError as e:
        print(f"Ошибка при создании Book: {e}")

    try:
        invalid_tree = Tree("Pine", -10.0, 20)  # Некорректный аргумент (отрицательная высота)
    except ValueError as e:
        print(f"Ошибка при создании Tree: {e}")

    try:
        invalid_account = BankAccount("87654321", -500.0)  # Некорректный аргумент (отрицательный баланс)
    except ValueError as e:
        print(f"Ошибка при создании BankAccount: {e}")
