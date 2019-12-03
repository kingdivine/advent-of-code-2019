import math

def get_module_masses():
    f = open("data.txt", "r")
    if f.mode == 'r':
        masses = f.readlines()
        f.close()
        return masses
    else: 
        return []    

def fuel_required(mass):
    return math.floor((int(mass)/3)) - 2
