#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def square_root(a: float) -> float:
    a = a**(1/2)
    return a


def square(a: float) -> float:
    a = a**(2)
    return a


def average(a: float, b: float, c: float) -> float:
    average = (a+b+c)/3
    return average


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    degrees_tot = angle_degs + angle_mins/60 + angle_secs/3600
    in_rad = degrees_tot*(math.pi/180)
    return in_rad


def to_degrees(angle_rads: float) -> tuple:
    tot_deg = math.degrees(1)
    degs = math.floor(tot_deg)
    left1 = tot_deg - degs
    mins = math.floor((left1) * 60)
    left2 = tot_deg - degs - (mins / 60)
    secs = math.floor(left2 * 3600)

    return degs, mins, secs


def to_celsius(temperature: float) -> float:
    tc = round((temperature - 32)/1.8)
    return tc


def to_farenheit(temperature: float) -> float:
    tf = round((temperature * 1.8) + 32)
    return tf


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")

    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()