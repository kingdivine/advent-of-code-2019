def main():
    data = read_data()
    orbits = create_dict(data)
    count = count_orbits(orbits)
    print(count) #this gives 315757

def read_data():
    f = open('data.txt', mode="r")
    if f.mode == 'r': 
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        return lines
    else:
        return []

def create_dict(data):
    orbits = {} 

    for line in data:
        being_orbited = line.split(')')[0]
        in_orbit = line.split(')')[1]

        orbits[in_orbit] = being_orbited

    return orbits   

def count_orbits(orbits):
    count = 0
    for orbit in orbits:
        while not orbit == "COM":
            count += 1
            orbit = orbits[orbit] 
    return count
    
if __name__ == "__main__":
    main()