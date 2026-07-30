class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        days_old: int,
        growth: float,
    ) -> None:
        self.name = name
        self._height = height
        self._days_old = days_old
        self._growth = growth
        self._stats = Plant.Stats()

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
        self._height += self._growth
        self._stats.grow_calls += 1

    def age(self) -> None:
        self._days_old += 1
        self._stats.age_calls += 1

    def show(self) -> None:
        print(
            f"{self.name}: "
            f"{self.get_height():.1f}cm, "
            f"{self.get_age()} days old"
        )
        self._stats.show_calls += 1

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

        def display(self) -> None:
            print(
                f"Stats: "
                f"{self.grow_calls} grow, "
                f"{self.age_calls} age, "
                f"{self.show_calls} show"
            )

    def stats_display(self) -> None:
        print(f"[statistics for {self.name}]")
        self._stats.display()


class Flower(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days_old: int,
            growth: float,
            color: str,
    ) -> None:
        super().__init__(name, height, days_old, growth)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.grow()
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")

        if self.bloomed:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Seed(Flower):
    def __init__(
            self,
            name: str,
            height: float,
            days_old: int,
            growth: float,
            color: str,
    ) -> None:
        super().__init__(name, height, days_old, growth, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42
        self._days_old += 20
    
    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seeds}")


class Tree(Plant):
    def __init__(
            self,
            name: str,
            height: float,
            days_old: int,
            growth: float,
            trunk_diameter: float
    ) -> None:
        super().__init__(name, height, days_old, growth)
        self.trunk_diameter = trunk_diameter
        self._shade = 0

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} "
            f"now produces a shade of {self.get_height():.1f}cm "
            f"long and {self.trunk_diameter:.1f}cm wide."
        )
        self._shade += 1

    def stats_display(self) -> None:
        super().stats_display()
        print(f" {self._shade} shade")


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

    def show(self) -> None:
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
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_year(400)}")
    print("")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, 8, "red")

    rose.show()
    rose.stats_display()

    print("[asking the rose to grow and bloom]")

    rose.bloom()
    rose.show()
    rose.stats_display()

    print("")
    print("=== Tree")
    oak = Tree("Oak", 200, 365, 1, 5)
    oak.show()
    oak.stats_display()

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.stats_display()

    print("")
    print("=== Seed")
    sunflower = Seed("Sunflower", 80, 45, 30, "yellow")
    sunflower.show()

    print("[make sunflower grow, age and bloom]")
    sunflower.bloom()
    sunflower.show()
    sunflower.age()
    sunflower.stats_display()

    # print("")
    # print("=== Vegetable")
    # tomato = Vegetable("Tomato", 5, 10, "April", 0)
    # tomato.show()

    # print("[make tomato grow and age for 20 days]")

    # tomato.time(20)
    # tomato.show()
