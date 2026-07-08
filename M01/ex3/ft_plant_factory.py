# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_factory.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: romdo-na <romdo-na@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/08 13:25:20 by romdo-na          #+#    #+#              #
#    Updated: 2026/07/08 14:10:07 by romdo-na         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    def __init__(
        self, 
        name: str, 
        height: float, 
        days_old: int
    ) -> None:
        self.name = name
        self.height = height
        self.days_old = days_old

    def show(self) -> None:
        print(
            f"{self.name}: "
            f"{self.height:.1f}cm, "
            f"{self.days_old} days old"
        )
    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days_old += 1

if __name__ == "__main__":
    print("=== Plant Factory Output ===")

    plants = [
        Plant("Rose", 25.0, 30),
        Plant("Oak", 200.0, 365),
        Plant("Cactus", 5.0, 90),
        Plant("Sunflower", 80.0, 45),
        Plant("Fern", 15.0, 120),
    ]

    for plant in plants:
        print("Created:", end=" ")
        plant.show()
