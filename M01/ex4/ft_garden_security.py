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


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = Plant("Rose", 15.0, 10)
    print("Plant created:", end=" ")
    rose.show()
    print("")

    rose.set_height(25)
    rose.set_age(30)
    print("")

    rose.set_height(-25)
    rose.set_age(-30)
    print("")

    print("Current state:", end=" ")
    rose.show()
