import math
from shared import get_module_masses, fuel_required

def main():
    #this gives a value of 5010211
    print(get_fuel_requirement())

def get_fuel_requirement():
    total_fuel_requirement = 0
    masses = get_module_masses()
    for mass in masses:
        remaining_mass = int(mass)
        while True:
            remaining_mass = fuel_required(remaining_mass)
            if remaining_mass < 0:
                break
            total_fuel_requirement += remaining_mass
    return total_fuel_requirement    



if __name__ == "__main__":
    main()
