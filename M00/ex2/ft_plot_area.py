# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_name.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: romdo-na <romdo-na@student.42porto.com>    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/07/04 13:34:35 by romdo-na          #+#    #+#              #
#    Updated: 2026/07/04 13:42:26 by romdo-na         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print(f"Plot area: {area}")