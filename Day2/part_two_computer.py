from shared import get_gravity_assist_program, computer

OUTPUT_TO_MATCH = 19690720

def main():
    gravity_assist_program = get_gravity_assist_program()
    noun_and_verb = find_noun_and_verb(gravity_assist_program)
    print(noun_and_verb) #this gives [72,64]

def find_noun_and_verb(gravity_assist_program):
    original_gravity_assist_program = gravity_assist_program.copy()
    noun = verb = 0
    for noun in range(99):
        for verb in range(99):
            gravity_assist_program[1] = noun
            gravity_assist_program[2] = verb
            output = computer(gravity_assist_program)[0]
            if output == OUTPUT_TO_MATCH:
                return [noun, verb]
            gravity_assist_program = original_gravity_assist_program.copy()
    return []        

if __name__ == "__main__":
    main()