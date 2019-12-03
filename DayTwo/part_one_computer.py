from shared import get_gravity_assist_program, computer

def main():
    gravity_assist_program = get_gravity_assist_program()
    gravity_assist_program_restored_state = restore_to_1202(gravity_assist_program)
    gravity_assist_program_computed =  computer(gravity_assist_program_restored_state)
    print(gravity_assist_program_computed[0]) #this gives a value of 4138658

def restore_to_1202(gravity_assist_program):
    gravity_assist_program[1] = 12
    gravity_assist_program[2] = 2
    return gravity_assist_program        

if __name__ == "__main__":
    main()        