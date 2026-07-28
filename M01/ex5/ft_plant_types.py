# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: romdo-na <romdo-na@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/28 11:22:27 by romdo-na          #+#    #+#              #
#    Updated: 2026/07/28 12:54:23 by romdo-na         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Authorized: super(), print(), range(), round()

# Requirements:
# • Start with your Plant class from the previous exercise, which holds the common
# features (name, height, and age)
# • Create specialized types: Flower, Tree, and Vegetable
# • Each specialized type should inherit the basic plant features
# • Flower needs: a color attribute and ability to bloom()
# • Tree needs: a trunk_diameter attribute and the ability to produce_shade()
# • Vegetable needs: a harvest_season and a nutritional_value attributes
# • When creating specialized plants, call the parent methods from inside your new
# class using super(). It can be applied to any method, including __init__()
# • A call to show() on a specialized class needs to print the standard Plant output
# and the extra characteristics of your specialized plant. Your method override can
# re-use the already existing code in the parent.
# • Create at least one instance of each plant type; make the flower bloom; make the
# nutritional value start from 0, then increase when the vegetable’s age() and grow()
# methods are called.
# • Avoid duplicating common plant code across different specialized types.
# • No need to validate the new attributes in the three new classes.

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
		print(f"Color: {self.color}")
		if self.bloomed:
			print("Rose is blooming beautifully!")
		else:
			print("[asking the rose to bloom]")


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
		print(f"Trunk diameter: {self.trunk_diameter}cm")

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
		self.nutritional_value = 0

	def vegetable_show(self) -> None:
		super().show()
		print(f"Harvest season: {self.harvest_season}")
		print(f"Nutritional value: {self.nutritional_value}")

	

if __name__ == "__main__":
	print("=== Garden Plant Types ===")

	print("=== Flower")
	rose = Flower("Rose", 15.0, 10, "red")
	print("Plant created:", end=" ")
	rose.flower_show()
