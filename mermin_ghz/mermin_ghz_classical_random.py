import random
from mermin_ghz import generate_input, verify, pre_run, post_run


def mermin_ghz_game():
    inputs = generate_input()
    answers = [0, 1]
    alice = random.choice(answers)
    bob = random.choice(answers)
    charlie = random.choice(answers)
    return inputs, [alice, bob, charlie]

def main():
    inputs, outputs = mermin_ghz_game()
    pre_run()
    post_run(inputs, outputs)

if __name__ == "__main__":
    main()
