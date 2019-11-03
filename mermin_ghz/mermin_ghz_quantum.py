import numpy as np
# import qiskit stuffa
from qiskit import QuantumCircuit, execute
from qiskit import Aer
from qiskit.visualization import plot_state_city
from qiskit.visualization import plot_bloch_multivector
# import mermin_ghz methods:
from mermin_ghz import MerminGHZ

# Run the quantum circuit on a qasm simulator backend
backend = Aer.get_backend('qasm_simulator')

class MerminGHZQuantum(MerminGHZ):
    def __init__(self):
        super().__init__(self)
        self.strategy = "Quantum"

    def run(self, shots=1, input_bits=None):
        if input_bits is None:
            input_bits = self.generate_input()
        result = self.mermin_ghz(input_bits, shots)
        return input_bits, self.postprocess_result(result)

    # Function to create the initial entangled GHZ state: 1/sqrt(2)(|000> + |111>)
    def generate_initial_ghz(self, n_qb):
        qc = QuantumCircuit(n_qb, n_qb, name='ghz')
        # Create a GHZ state
        qc.h(0)
        for i in range(n_qb-1):
            qc.cx(i, i+1)
        return qc

    # winning strategy circuit
    def winning_strategy(self, qprog, input_bits):
        # adding barrier
        qprog.barrier()
        if qprog.n_qubits == len(input_bits):
            # Apply rotation
            for i in range(len(input_bits)):
                qprog.rz(self.generate_phase(input_bits[i]), i)
            # Adding barrier
            qprog.barrier()
            # Apply hadamard gate for each qubit
            for i in range(qprog.n_qubits):
                qprog.h(i)
        return qprog

    # generate the phase for the rz gate
    def generate_phase(self, x):
        return np.pi * x / 2

    def mermin_ghz(self, input_bits, shots):
        # prepare the initial entangled state
        ghz = self.generate_initial_ghz(3)
        # run though the winning strategy quantum circuit
        mghz = self.winning_strategy(ghz, input_bits)
        # Measure the output of the circuit
        mghz.measure([0, 1, 2], [0, 1, 2])

        # Create a Quantum Program for execution
        job = execute(mghz, backend, shots=shots)
        #obtain the results
        result = job.result()
        return result.get_counts(mghz)

    def postprocess_result(selfs, results):
        answers = []
        for key in results.keys():
            alice = int(key[0])
            bob = int(key[1])
            charlie = int(key[2])
            answers.append([alice, bob, charlie])
        return answers


def main():
    game = MerminGHZQuantum()
    # prepare the initial entangled state
    inputs, outputs = game.run(1, [0, 0, 0])
    game.pre_run()
    for a in outputs:
        game.post_run(inputs, a)

if __name__ == "__main__":
    main()
