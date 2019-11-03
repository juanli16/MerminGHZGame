import math
import random
from collections import Counter
from functools import reduce


class MerminGHZ(object):
    def __init__(self, strategy):
        self.strategy = strategy
        self.input_bits = [[0, 0, 0],
                          [0, 1, 1],
                          [1, 0, 1],
                          [1, 1, 0]
                          ]

    # randomly choose 1 valid input
    def generate_input(self):
        # The input bits have to be divisible by 2
        return random.choice(self.input_bits)


    # verify if the winning condition is satisfied
    def verify(self, input_bits, output_bits):
        inputs = reduce(lambda x, y: x | y, input_bits)
        outputs = reduce(lambda x, y: x ^ y, output_bits)
        return inputs == outputs

    # initialize stat dictionary
    def init_stats(self, input_bits=None):
        stats = {}
        if input_bits is None:
            for bits in self.input_bits:
                stats[self.to_bitstring(bits)] = {}
        else:
            stats[self.to_bitstring(input_bits)] = {}
        return stats

    # play the game multiple times
    def multi_play(self, numruns, input_bits=None):
        cnt  = Counter()
        stats = self.init_stats(input_bits)
        results = Counter()
        for run in range(numruns):
            rawin, rawout = self.run(input_bits)
            inputs, outputs = self.to_bitstring(rawin), self.to_bitstring(rawout)
            if outputs not in stats[inputs]:
                stats[inputs][outputs] = 1
            else:
                stats[inputs][outputs] += 1
            if self.verify(rawin, rawout):
                cnt['win'] += 1
            else:
                cnt['lose'] += 1
        return cnt, stats

    def to_bitstring(self,l):
        return ''.join([str(x) for x in l])

    def to_list(self, l):
        return [int(x) for x in l]

    def pre_run(self):
        print("Mermin-GHZ Game")
        print("- 3 players Alice, Bob, Charlie, all are given an input bit x, y, z, respectively")
        print("- The input bits respect the promise that sum(x, y, z) is divisible by 2 (even parity)")
        print("- (They can't communicate, but they can have pre-shared entangled qubits.)")
        print("- Players win if the following condition is satisfied")
        print("-        a ⊕ b ⊕ c = x ∨ y ∨ z")
        print()
        print("Press enter to enter the game")
        enter = input()
        return enter == "\n"


    def post_run(self, inputs, outputs):
        print("Verifier chose input {}".format(''.join([str(x) for x in inputs])))
        """
        print("Input bits: {}, output bits: {} the result is: ".format(''.join([str(x) for x in inputs]), ''.join([str(x) for x in outputs])), end =" ")
        print("correct!" if verify(inputs, outputs) else "incorrect!")
        """
        print("Alice given {} produce output {}".format(inputs[0], outputs[0]))
        print("Bob given {} produce output {}".format(inputs[1], outputs[1]))
        print("Charlie given {} produce output {}".format(inputs[2], outputs[2]))
        print("The condition {} ⊕ {} ⊕ {} = {} ∨ {} ∨ {}".format(outputs[0], outputs[1], outputs[2], inputs[0], inputs[1], inputs[2]), end=" ")
        print("is true" if self.verify(inputs, outputs) else "is false")
        print("They win!" if self.verify(inputs, outputs) else "They lost!")
        print()
