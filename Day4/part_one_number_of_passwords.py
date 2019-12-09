INPUT = "136760-595730"


def main():
    potential_passwords = find_potential_passwords(INPUT)
    print(len(potential_passwords)) # this gives 1873


def find_potential_passwords(input):
    valid_passwords = []
    min_number = int(input.split('-')[0])
    max_number = int(input.split('-')[1])
    for number in range(min_number,max_number):
        if matches_criteria(str(number)):
            valid_passwords.append(str(number))
    return valid_passwords        
    

def matches_criteria(number):
    adjacency = False
    for i in range(len(number)):
        if i > 0 and number[i] < number[i-1]:
            return False
        if i > 0 and number[i] == number[i-1]:
            adjacency = True    
    return adjacency 

if __name__ == '__main__':
    main()    