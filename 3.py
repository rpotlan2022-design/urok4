class Figure:
    FIGURES = ["квадрат", "прямокутник", "трикутник"]

    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in self.FIGURES, "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

    @property
    def get_figure_type(self):
        return self.type

    @property
    def get_figure_length(self):
        return self.type  


a = Figure("квадрат", 5)
b = Figure("трикутник", 3)

print(f"a: тип = {a.get_figure_type}, довжина = {a.get_figure_length}")
print(f"b: тип = {b.get_figure_type}, довжина = {b.get_figure_length}")
