# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_analytics.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: romdo-na <romdo-na@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/29 10:45:50 by romdo-na          #+#    #+#              #
#    Updated: 2026/07/29 12:53:02 by romdo-na         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Authorized: super(), print(), range(), round(), staticmethod(),
# classmethod()

# Requirements:
# • Create a static method for the Plant class that checks if a specific age given as a
# parameter is older than a year.
# • Create a class method that allows you to create an “anonymous” plant directly
# when you do not yet have all the information.
# • Create a Seed class that inherits from Flower, and holds the number of seeds once
# the flower has bloomed. The show() method must be improved accordingly.
# • Each Plant has an internal system, implemented as a nested class, that holds
# statistical data: number of grow() calls, number of age() calls, number of show()
# calls. Encapsulation is required, as well as a display function.
# • Trees need an extra piece of statistical data: number of produce_shade() calls.
# • Finally, create a unique function, not part of any class, that displays statistics for
# any kind of plant.

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
		self._height += 0.8
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
		return cls("Unknown plant", 0.0, 0, 0.0)
	
	class Stats:
		def __init__(self):
			self.grow_calls = 0
			self.age_calls = 0
			self.show_calls = 0
		
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

	def show(self) -> None:
		super().show()
		print(f" Color: {self.color}")
		
		if self.bloomed:
			print(" Rose is blooming beautifully!")
		else:
			print(" Rose has not bloomed yet")


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
	rose = Flower("Rose", 15.0, 10, "red")
	rose.show()

	print("[asking the rose to grow and bloom]")

	rose.bloom()
	rose.show()


	# print("")
	# print("=== Tree")
	# oak = Tree("Oak", 200, 365, 5)
	# oak.show()

	# print("[asking the oak to produce shade]")	
	# oak.produce_shade()

	# print("")
	# print("=== Vegetable")
	# tomato = Vegetable("Tomato", 5, 10, "April", 0)
	# tomato.show()

	# print("[make tomato grow and age for 20 days]")

	# tomato.time(20)
	# tomato.show()