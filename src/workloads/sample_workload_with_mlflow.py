import logging
import os
import mlflow

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

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
    mlflow.set_experiment("Sample Workload Experiment")

    with mlflow.start_run():
        # Set Git-related tags for traceability
        mlflow.set_tag(
            "mlflow.source.git.commit", os.getenv("MLFLOW_GIT_COMMIT", "unknown")
        )
        mlflow.set_tag(
            "mlflow.source.git.branch", os.getenv("MLFLOW_GIT_BRANCH", "unknown")
        )
        mlflow.set_tag(
            "mlflow.source.git.repoURL", os.getenv("MLFLOW_GIT_REPO_URL", "unknown")
        )

        # logging.basicConfig(level=logging.DEBUG)

        shots = 1000
        device = "GPU"
        mlflow.log_param("shots", shots)
        mlflow.log_param("device", device)
        counts = demo_function(shotsAmount=shots, device=device)
        mlflow.log_dict(counts, "simulation_counts.json")
