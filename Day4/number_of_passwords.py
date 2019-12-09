from collections import defaultdict

INPUT = "136760-595730"

def main():
    part_one_potential_passwords = find_potential_passwords(INPUT, matches_part_one_criteria)
    print(len(part_one_potential_passwords)) # this gives 1873

    part_two_potential_passwords = find_potential_passwords(INPUT, matches_part_two_criteria)
    print(len(part_two_potential_passwords))  #this gives 1264

def find_potential_passwords(input, criteria):
    valid_passwords = []
    min_number = int(input.split('-')[0])
    max_number = int(input.split('-')[1])
    for number in range(min_number,max_number):
        if criteria(str(number)):
            valid_passwords.append(str(number))
    return valid_passwords        
    
def matches_part_one_criteria(number):
    adjacency = False
    for i in range(len(number)):
        if i > 0 and number[i] < number[i-1]:
            return False
        if i > 0 and number[i] == number[i-1]:
            adjacency = True    
    return adjacency 

def matches_part_two_criteria(number):
    adjacencies = defaultdict(int)
    for i in range(len(number)):
        if i > 0 and number[i] < number[i-1]:
            return False
        adjacencies[number[i]] += 1
    for entry in adjacencies:
        if adjacencies[entry] == 2:
            return True
    return False 


if __name__ == '__main__':
    main()    