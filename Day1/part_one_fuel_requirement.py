import math
from shared import get_module_masses, fuel_required

def main():
    #this gives a value of 3342050
    print(get_fuel_requirement())

def get_fuel_requirement():
    total_fuel_requirement = 0
    masses = get_module_masses()
    for mass in masses:
        fuel_requirement = fuel_required(mass)
        total_fuel_requirement += fuel_requirement
    return total_fuel_requirement    



if __name__ == "__main__":
    main()