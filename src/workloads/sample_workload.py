import logging

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
import pynvml

logger = logging.getLogger(__name__)


def demo_function(shotsAmount=1000, device="CPU"):
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
    logging.basicConfig(level=logging.DEBUG)
    pynvml.nvmlInit()
    output = demo_function()
    print("Simulation result:", output)
    print(f"Driver Version: {pynvml.nvmlSystemGetDriverVersion()}")
    deviceCount = pynvml.nvmlDeviceGetCount()
    print(f"Number of GPUs: {deviceCount}")
    for i in range(deviceCount):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        name = pynvml.nvmlDeviceGetName(handle)
        print(f"GPU {i}: {name}")
        info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        print(f"  Total memory: {info.total / 1024 ** 2} MB")
        print(f"  Used memory: {info.used / 1024 ** 2} MB")
        print(f"  Free memory: {info.free / 1024 ** 2} MB")
    pynvml.nvmlShutdown()
