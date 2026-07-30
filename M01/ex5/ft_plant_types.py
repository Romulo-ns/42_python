class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        days_old: int,
    ) -> None:
        self.name = name
        self._height = height
        self._days_old = days_old

    # Getter
    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._days_old

    # Setter
    def set_height(self, height: float) -> None:
        if height < 0:
            print(
                f"{self.name}: "
                "Error, height can't be negative\n"
                "Height update rejected"
            )
            return
        else:
            self._height = height
            print(
                "Height updated: "
                f"{self.get_height()}cm"
            )

    def set_age(self, days_old: int) -> None:
        if days_old < 0:
            print(
                f"{self.name}: "
                "Error, age can't be negative\n"
                "Age update rejected"
            )
            return
        else:
            self._days_old = days_old
            print(
                "Age updated: "
                f"{self.get_age()} days"
            )

    def grow(self) -> None:
        self._height += 0.8

    def age(self) -> None:
        self._days_old += 1

    def show(self) -> None:
        print(
            f"{self.name}: "
            f"{self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days_old: int,
            color: str,
    ) -> None:
        super().__init__(name, height, days_old)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def flower_show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.bloomed:
            print(" Rose is blooming beautifully!")
        else:
            print(" Rose has not bloomed yet")
            print(" [asking the rose to bloom]")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days_old: int,
            trunk_diameter: float
    ) -> None:
        super().__init__(name, height, days_old)
        self.trunk_diameter = trunk_diameter

    def tree_show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} "
            f"now produces a shade of {self.get_height():.1f}cm "
            f"long and {self.trunk_diameter:.1f}cm wide."
        )


class Vegetable(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days_old: int,
            harvest_season: str,
            nutritional_value: float
    ) -> None:
        super().__init__(name, height, days_old)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def vegetable_show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def vegetable_grow(self) -> None:
        self._height += 2.1

    def time(self, days: int) -> None:
        for _ in range(days):
            self.vegetable_grow()
            self.age()
            self.nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.flower_show()

    rose.bloom()
    rose.flower_show()

    print("")
    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.tree_show()

    print("[asking the oak to produce shade]")
    oak.produce_shade()

    print("")
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April", 0)
    tomato.vegetable_show()

    print("[make tomato grow and age for 20 days]")

    tomato.time(20)
    tomato.vegetable_show()
