import logging

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from workloads.q8s_runtime import cuda_info

logger = logging.getLogger(__name__)


@cuda_info
def demo_function(shotsAmount=1000, device="GPU"):
    simulator = AerSimulator(method="statevector", device=device)

    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])

    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=shotsAmount)
    result = job.result()
    counts = result.get_counts()
    logger.debug(circuit)
    return counts


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    output = demo_function(2000)
    print("Simulation result:", output)
