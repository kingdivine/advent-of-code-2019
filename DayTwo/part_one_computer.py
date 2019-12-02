def main():
    gravity_assist_program = get_gravity_assist_program()
    gravity_assist_program_restored_state = restore_to_1202(gravity_assist_program)
    gravity_assist_program_computed =  computer(gravity_assist_program_restored_state)
    #this gives a value of 4138658
    print(gravity_assist_program_computed)


def get_gravity_assist_program():
    f = open("data.txt", mode= "r")
    if f.mode == "r":
        content = f.read()
        return [int(value) for value in content.split(',')]
    else:
        return []

def restore_to_1202(gravity_assist_program):
    gravity_assist_program[1] = 12
    gravity_assist_program[2] = 2
    return gravity_assist_program        

def computer(gravity_assist_program):
    for i in range(0, len(gravity_assist_program) - 3, 4):
        opcode = gravity_assist_program[i]
        if opcode == 99:
            break
        index_a, index_b, index_result = gravity_assist_program[i + 1], gravity_assist_program[i + 2], gravity_assist_program[i + 3]
        value_a, value_b = gravity_assist_program[index_a], gravity_assist_program[index_b]
        if opcode == 1:
            gravity_assist_program[index_result] = value_a + value_b
        elif opcode == 2:
            gravity_assist_program[index_result] = value_a * value_b
    return gravity_assist_program



if __name__ == "__main__":
    main()        