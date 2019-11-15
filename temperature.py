#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: November 2019
# This program coverts celcius to fahrenheit


def temp():
    # input
    celsius = int(input("Enter a degree in celsius: "))

    # process
    Fahrenheit = (celsius * 1.8) + 32

    # output
    print("{} celsius is {} fahrenheit.".format(celsius, round(Fahrenheit, 1)))


def main():
    # call function
    temp()


if __name__ == "__main__":
    main()
