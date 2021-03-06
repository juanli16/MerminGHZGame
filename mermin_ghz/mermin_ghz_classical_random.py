import random
# from mermin_ghz import generate_input, verify, pre_run, post_run
from mermin_ghz import MerminGHZ

class MerminGHZRandom(MerminGHZ):
    def __init__(self):
        super().__init__(self)
        self.strategy = "classical_random"

    def run(self, inputs=None):
        if inputs is None:
            inputs = self.generate_input()
        answers = [0, 1]
        alice = random.choice(answers)
        bob = random.choice(answers)
        charlie = random.choice(answers)
        return inputs, [alice, bob, charlie]


def main():
    game = MerminGHZRandom()
    inputs, outputs = game.run()
    game.pre_run()
    game.post_run(inputs, outputs)
    count, stats = game.multi_play(1000,[0,0,0])
    print(count)
    print(stats)

if __name__ == "__main__":
    main()
