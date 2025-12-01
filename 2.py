class Name:
    def __init__(self, name, hobby) -> None:
        allowed_names = ["Богдан", "Анонім", "Бодько", "Роман"]

        if name not in allowed_names:
            raise ValueError(f"Дозволені імена: {', '.join(allowed_names)}")

        if not hobby or hobby.strip() == "":
            raise ValueError("Хобі має бути непорожнім!")

        self.name = name
        self.hobby = hobby

try:
    a = Name("Бодько", "футбол")
    print(f"a: ім'я = {a.name}, хобі = {a.hobby}")
except ValueError as e:
    print(f"a: помилка - {e}")

try:
    b = Name("Анонім", "читання")
    print(f"b: ім'я = {b.name}, хобі = {b.hobby}")
except ValueError as e:
    print(f"b: помилка - {e}")

try:
    c = Name("Іван", "плавання")
    print(f"c: ім'я = {c.name}, хобі = {c.hobby}")
except ValueError as e:
    print(f"c: помилка - {e}")

try:
    d = Name("Богдан", "")
    print(f"d: ім'я = {d.name}, хобі = {d.hobby}")
except ValueError as e:
    print(f"d: помилка - {e}")

      



