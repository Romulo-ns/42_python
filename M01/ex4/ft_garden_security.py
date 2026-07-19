# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: romdo-na <romdo-na@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/08 14:16:31 by romdo-na          #+#    #+#              #
#    Updated: 2026/07/19 18:34:15 by romdo-na         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# print(), range(), round()

# Requirements:
# • Improve your Plant class in order to protect its data from corruption
# • Provide controlled ways to modify plant data: set_height(), set_age()
# • Provide safe ways to access plant data: get_height(), get_age()
# • Ensure plant height cannot be negative through validation
# • Ensure plant age cannot be negative through validation
# • Print error messages from the class when invalid values are provided, leaving data
# unchanged or creating the plant with default values
# • Use encapsulation: prevent your class attributes from being used directly by using
# the “protected” convention (not the mangling)

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
				"Error, height can't be negative"
			)
			return
		else:
			self._height = height

	def set_age(self, days_old: int) -> None:
		if days_old < 0:
			print(
				f"{self.name}: "
				"Error, age can't be negative"
			)
			return
		else:
			self._days_old = days_old

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

	rose.set_height(25)
	rose.set_age(30)

	rose.set_height(-5)
	print("Height update rejected")

	rose.set_age(-20)
	print("Age update rejected")

	print("Current state:", end=" ")
	rose.show()
