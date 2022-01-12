"""
Program: CS 115 Project 1
Author: Diana Arce-Hernandez
"""


import sys

def main():
    print("==> Rabbits and Foxes Population Simulator <==")
    print()
    print("--- Model Parameters ---")
    r_birth = float(input("Rabbits birth rate: "))
    r_death = float(input("Rabbits death rate: "))
    f_birth = float(input("Foxes birth rate: "))
    f_death = float(input("Foxes death rate: "))

    print()
    print("--- Initial Population ---")
    r = float(input("Number of rabbits (in thousands) at t = 0: "))
    f = float(input("Number of foxes (in thousands) at t = 0: "))
    t = int(input("Timescale: "))
    print()
    sum_r = 0
    sum_f = 0
    min_r = r
    max_f = 0
    t_r = 0
    t_f = 0

    if t >=0 and f_birth >= 0 and r_death >= 0:
        if r >= 0 and f >= 0:
            for i in range(t + 1):
                print("Time t = ", i, ": ", r, "k rabbits, ", f, "k foxes", sep="")
                r_total = r
                f_total = f
                r = round(r + (r_birth * r) - (r_death * r * f_total), 3)
                f = round(f + (f_birth * f * r_total) - (f_death * f), 3)
                sum_r = sum_r + r_total
                sum_f = sum_f + f_total

                if f_total >= max_f:
                    max_f = f_total
                    t_f = i
                if r_total < min_r:
                    min_r = r_total
                    t_r = i

        elif f >= 0 and r <= 0:
            r = 0.0
            for i in range(t + 1):
                print("Time t = ", i, ": ", r, "k rabbits, ", f, "k foxes", sep="")
                r_total = r
                f_total = f
                r = round(r + (r_birth * r) - (r_death * r * f_total), 3)
                f = round(f + (f_birth * f * r_total) - (f_death * f), 3)
                sum_r = sum_r + r_total
                sum_f = sum_f + f_total

                if f_total >= max_f:
                    max_f = f_total
                    t_f = i
                if r_total < min_r:
                    min_r = r_total
                    t_r = 0


        elif r >= 0 and f <= 0:
            f = 0.0
            for i in range(t + 1):
                print("Time t = ", i, ": ", r, "k rabbits, ", f, "k foxes", sep="")
                r_total = r
                f_total = f
                r = round(r + (r_birth * r) - (r_death * r * f_total), 3)
                f = round(f + (f_birth * f * r_total) - (f_death * f), 3)
                sum_r = sum_r + r_total
                sum_f = sum_f + f_total

                if f_total >= max_f:
                    max_f = f_total
                    t_f = 0
                if r_total < min_r:
                    min_r = r_total
                    t_r = i



        average_r = (sum_r / (t+1))
        average_f = (sum_f / (t+1))

        print()
        print("--- Simulation Statistics ---")
        print("Average rabbit population: ", round(average_r, 3), "k",sep="")
        print("Average fox population: ", round(average_f, 3), "k", sep="")
        print("Min rabbit population was ", min_r, "k at t=", t_r, sep="")
        print("Max fox population was ", max_f, "k at t=", t_f, sep="")

    else:
        if t <= 0:
            print("Error: cannot have a negative timescale")
            sys.exit(-1)
        elif f_birth <= 0:
            print("Error: Cannot have a negative birth rate for foxes")
            sys.exit(-1)
        elif r_death <= 0:
            print("Error: Cannot have a negative death rate for rabbits")
            sys.exit(-1)

main()