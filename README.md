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

install pre-commit hooks:

```bash
pre-commit install --hook-type post-checkout
```

### Initializing the project

Initialize the project:

```bash
q8sctl init --images
```

### Getting the cluster configurations

Login into the Qubernetes [Console](https://console.em4qs.qubernetes.dev) select the Settings -> General option and download the kubeconfig file for your cluster. Save it as `kubeconfig.yaml` in the project root directory.

### Getting a PAT for GitHub Container Registry

To execute workloads that have images in GitHub Container Registry (GHCR), you need a Personal Access Token (PAT) with the `read:packages` scope. Follow [GitHub’s guide on creating a Personal Access Token (classic)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) to create one.

## Execute workloads from command line

To execute workloads in your Qubernetes cluster, use the following command:

```bash
q8sctl execute --registry-pat YOUR_GHCR_PAT --target cpu /src/workloads/sample_workload.py
```

## Execute workloads from Jupyter Lab notebooks

Install Jupyter Lab if you haven't already:

```bash
pip install jupyter
```

To execute workloads from notebooks, start Jupyter Lab with the following command:

```bash
q8sctl jupyter --registry-pat YOUR_GHCR_PAT --target cpu --install
```

Open the `notebook.ipynb` file in Jupyter Lab. Select the kernel `Q8s kernel`.

## Building Images with CI

The image build workflow is defined in `.github/workflows/build-images.yaml`. It is triggered when a new branch is created or when a commit with a modified `Q8Sproject` file is pushed.
