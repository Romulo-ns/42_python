# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_growth.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: romdo-na <romdo-na@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/08 12:07:07 by romdo-na          #+#    #+#              #
#    Updated: 2026/07/08 13:18:28 by romdo-na         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Plant:
    name: str
    height: float
    days_old: int

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days_old += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days_old} days old")

if __name__ == "__main__":

    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.days_old = 30
    
    print("=== Garden Plant Registry ===")
    rose.show()

    initial_height = rose.height

    for day in range(1, 8):
        print(f"=== Day {day} ===")
        rose.age()
        rose.grow()
        rose.show()

    growth = rose.height - initial_height

    print(f"Grpwth this week: {growth:.1f}cm")
