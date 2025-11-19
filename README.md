# Developing with Q8S

## Getting Started

This is an example project demonstrating how to set up continuous integration (CI) for a Q8S project. The project includes a simple Python environment configuration and CI workflows to automate building of images used to execute workloads in Qubernetes clusters.

### Prerequisites

Create a virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the `q8sctl` command-line tool:

```bash
pip install -r requirements-dev.txt
```

### Initializing the project

Initialize the Q8S project:

```bash
q8sctl init --images
```
