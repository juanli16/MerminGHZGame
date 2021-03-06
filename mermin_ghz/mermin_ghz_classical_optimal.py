from mermin_ghz import MerminGHZ

class MerminGHZOptimal(MerminGHZ):
    def __init__(self):
        super().__init__(self)
        self.strategy = "classical_optimal"

    def run(self, inputs=None):
        answers = {'0': 1, '1':0}
        if inputs is None:
            inputs = self.generate_input()
        alice = answers[str(inputs[0])]
        bob = answers[str(inputs[1])]
        charlie = answers[str(inputs[2])]
        return inputs, [alice, bob, charlie]

def main():
    game = MerminGHZOptimal()
    inputs, outputs = game.run()
    game.pre_run()
    print("Here, we have a fixed deterministic strategy that is optimal and can win 3/4 of the time")
    game.post_run(inputs, outputs)
    counts, stats = game.multi_play(1000,[0,0,0])
    print(counts)
    print(stats)

if __name__ == "__main__":
    main()
