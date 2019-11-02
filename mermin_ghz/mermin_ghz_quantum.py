import numpy as np
import matplotlib
matplotlib.use("MACOSX")
import matplotlib.pyplot as plt
# import qiskit stuffa
from qiskit import QuantumCircuit, execute
from qiskit import Aer
from qiskit.visualization import plot_state_city
from qiskit.visualization import plot_bloch_multivector
# import mermin_ghz methods:
from mermin_ghz import generate_input, verify, pre_run, post_run

# Run the quantum circuit on a qasm simulator backend
backend = Aer.get_backend('qasm_simulator')


# Function to create the initial entangled GHZ state: 1/sqrt(2)(|000> + |111>)
def generate_initial_ghz(n_qb):
    qc = QuantumCircuit(n_qb, n_qb, name='ghz')
    # Create a GHZ state
    qc.h(0)
    for i in range(n_qb-1):
        qc.cx(i, i+1)
    return qc


# winning strategy circuit
def winning_strategy(qprog, input_bits):
    # adding barrier
    qprog.barrier()
    if qprog.n_qubits == len(input_bits):
        # Apply rotation
        for i in range(len(input_bits)):
            qprog.rz(generate_phase(input_bits[i]), i)
        # Adding barrier
        qprog.barrier()
        # Apply hadamard gate for each qubit
        for i in range(qprog.n_qubits):
            qprog.h(i)
    return qprog

# generate the phase for the rz gate
def generate_phase(x):
    return np.pi * x / 2


def mermin_ghz_game(input_bits):
    # prepare the initial entangled state
    ghz = generate_initial_ghz(3)
    # run though the winning strategy quantum circuit
    mghz = winning_strategy(ghz, input_bits)
    # Measure the output of the circuit
    mghz.measure([0, 1, 2], [0, 1, 2])

    # This returns a PIL Image
    # c = mghz.draw(output="latex")
    # c.show()

    # Create a Quantum Program for execution
    job = execute(mghz, backend)
    #obtain the results
    result = job.result()
    return result.get_counts(mghz)


def postprocess_result(results):
    answers = []
    for key in results.keys():
        alice = int(key[0])
        bob = int(key[1])
        charlie = int(key[2])
        answers.append([alice, bob, charlie])
    return answers


def main():
    # prepare the initial entangled state
    inputs = generate_input()
    results = mermin_ghz_game(inputs)
    answers = postprocess_result(results)
    pre_run()
    for a in answers:
        post_run(inputs, a)

if __name__ == "__main__":
    main()
