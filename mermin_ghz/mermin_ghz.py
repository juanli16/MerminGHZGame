import math
import random
from functools import reduce

# randomly choose 1 valid input
def generate_input():
    # The input bits have to be divisible by 2
    input_bits = [[0, 0, 0],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 0]
                  ]
    return random.choice(input_bits)


# verify if the winning condition is satisfied
def verify(input_bits, output_bits):
    inputs = reduce(lambda x, y: x | y, input_bits)
    outputs = reduce(lambda x, y: x ^ y, output_bits)
    return inputs == outputs

def pre_run():
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


def post_run(inputs, outputs):
    print("Verifier chose input {}".format(''.join([str(x) for x in inputs])))
    """
    print("Input bits: {}, output bits: {} the result is: ".format(''.join([str(x) for x in inputs]), ''.join([str(x) for x in outputs])), end =" ")
    print("correct!" if verify(inputs, outputs) else "incorrect!")
    """
    print("Alice given {} produce output {}".format(inputs[0], outputs[0]))
    print("Bob given {} produce output {}".format(inputs[1], outputs[1]))
    print("Charlie given {} produce output {}".format(inputs[2], outputs[2]))
    print("The condition {} ⊕ {} ⊕ {} = {} ∨ {} ∨ {}".format(outputs[0], outputs[1], outputs[2], inputs[0], inputs[1], inputs[2]), end=" ")
    print("is true" if verify(inputs, outputs) else "is false")
    print("They win!" if verify(inputs, outputs) else "They lost!")
    print()
