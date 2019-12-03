def get_gravity_assist_program():
    f = open("data.txt", mode= "r")
    if f.mode == "r":
        content = f.read()
        return [int(value) for value in content.split(',')]
    else:
        return []


def computer(gravity_assist_program):
    for i in range(0, len(gravity_assist_program) - 3, 4):
        opcode = gravity_assist_program[i]
        if opcode == 99:
            break
        index_a, index_b, index_result = gravity_assist_program[i + 1], gravity_assist_program[i + 2], gravity_assist_program[i + 3]
        value_a, value_b = gravity_assist_program[index_a], gravity_assist_program[index_b]
        if index_result <= len(gravity_assist_program) - 1:
            if opcode == 1:
                gravity_assist_program[index_result] = value_a + value_b
            elif opcode == 2:
                gravity_assist_program[index_result] = value_a * value_b
    return gravity_assist_program        