from mermin_ghz import generate_input, verify, pre_run, post_run


def mermin_ghz_game():
    answers = {'0': 1, '1':0}
    inputs = generate_input()
    alice = answers[str(inputs[0])]
    bob = answers[str(inputs[1])]
    charlie = answers[str(inputs[2])]
    return inputs, [alice, bob, charlie]

def main():
    inputs, outputs = mermin_ghz_game()
    pre_run()
    print("Here, we have a fixed deterministic strategy that is optimal and can win 3/4 of the time")
    post_run(inputs, outputs)

if __name__ == "__main__":
    main()
