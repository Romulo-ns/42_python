# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: romdo-na <romdo-na@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/04 14:00:32 by romdo-na          #+#    #+#              #
#    Updated: 2026/07/04 14:50:44 by romdo-na         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    age = int(input("Enter plant age in days: "))

    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")