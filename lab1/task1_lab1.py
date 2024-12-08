import doctest


class Book:
    """Класс, описывающий книгу."""

    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка объекта "Книга".

        :param title: Название книги (должно быть строкой).
        :param author: Автор книги (должен быть строкой).
        :param pages: Количество страниц (должно быть положительным целым числом).

        :raises ValueError: Если количество страниц некорректно.

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        """
        if not isinstance(title, str) or not isinstance(author, str):
            raise TypeError("Название и автор книги должны быть строками.")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом.")

        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0

    def read_pages(self, pages_to_read: int) -> int:
        """
        Чтение указанного количества страниц.

        :param pages_to_read: Количество страниц для чтения (должно быть положительным числом).
        :raises ValueError: Если количество страниц для чтения некорректно.
        :return: Количество страниц, которые удалось прочитать.

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read_pages(50)
        50
        >>> book.read_pages(300)
        278
        """
        if pages_to_read <= 0:
            raise ValueError("Количество страниц для чтения должно быть положительным.")

        remaining_pages = self.pages - self.current_page
        pages_read = min(pages_to_read, remaining_pages)
        self.current_page += pages_read
        return pages_read

    def is_finished(self) -> bool:
        """
        Проверяет, завершено ли чтение книги.

        :return: True, если книга полностью прочитана, иначе False.

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.is_finished()
        False
        >>> book.read_pages(328)
        328
        >>> book.is_finished()
        True
        """
        return self.current_page >= self.pages


if __name__ == "__main__":
    doctest.testmod()


class Tree:
    """Класс, описывающий дерево."""

    def __init__(self, species: str, height: float, age: int):
        """
        Создание объекта "Дерево".

        :param species: Вид дерева.
        :param height: Высота дерева (в метрах, положительное число).
        :param age: Возраст дерева (в годах, положительное число).

        Примеры:
        >>> tree = Tree("Oak", 15.5, 50)
        """
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Возраст дерева должен быть положительным числом.")

        self.species = species
        self.height = height
        self.age = age

    def grow(self, years: int = 1) -> None:
        """
        Увеличивает возраст и высоту дерева.

        :param years: Количество лет роста (по умолчанию 1).
        :raises ValueError: Если количество лет некорректно.

        Примеры:
        >>> tree = Tree("Oak", 15.5, 50)
        >>> tree.grow(5)
        >>> tree.height
        20.5
        >>> tree.age
        55
        """
        if years <= 0:
            raise ValueError("Количество лет должно быть положительным.")

        self.age += years
        self.height += years * 1.0  # Увеличиваем на 1 метр в год

    def is_old(self) -> bool:
        """
        Проверяет, является ли дерево старым (возраст больше 100 лет).

        :return: True, если дерево старое, иначе False.

        Примеры:
        >>> tree = Tree("Oak", 15.5, 120)
        >>> tree.is_old()
        True
        """
        return self.age > 100


if __name__ == "__main__":
    doctest.testmod()


class BankAccount:
    """Класс, описывающий банковский счет."""

    def __init__(self, account_number: str, balance: float):
        """
        Создание объекта "Банковский счет".

        :param account_number: Номер счета.
        :param balance: Начальный баланс (должен быть неотрицательным).

        Примеры:
        >>> account = BankAccount("12345678", 1000.0)
        """
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным.")

        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Пополнение счета.

        :param amount: Сумма пополнения (должна быть положительным числом).
        :raises ValueError: Если сумма пополнения отрицательна.

        Примеры:
        >>> account = BankAccount("12345678", 1000.0)
        >>> account.deposit(500.0)
        >>> account.balance
        1500.0
        """
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")

        self.balance += amount

    def withdraw(self, amount: float) -> float:
        """
        Снятие денег со счета.

        :param amount: Сумма снятия (должна быть положительным числом).
        :raises ValueError: Если сумма снятия превышает баланс.
        :return: Реально снятая сумма.

        Примеры:
        >>> account = BankAccount("12345678", 1000.0)
        >>> account.withdraw(500.0)
        500.0
        >>> account.balance
        500.0
        """
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете.")

        self.balance -= amount
        return amount


if __name__ == "__main__":
    doctest.testmod()

