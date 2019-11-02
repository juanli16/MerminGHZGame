import random
# from mermin_ghz import generate_input, verify, pre_run, post_run
from mermin_ghz import MerminGHZ

class MerminGHZ_random(MerminGHZ):
    def __init__(self):
        super().__init__(self)
        self.strategy = "classical_random"

    def run(self):
        inputs = self.generate_input()
        answers = [0, 1]
        alice = random.choice(answers)
        bob = random.choice(answers)
        charlie = random.choice(answers)
        return inputs, [alice, bob, charlie]


def main():
    game = MerminGHZ_random()
    inputs, outputs = game.run()
    game.pre_run()
    game.post_run(inputs, outputs)

if __name__ == "__main__":
    main()
