# Nvidia DGX Kubeflow demos

This document contains several demo workloads that were executed using [Charmed Kubeflow 1.6](https://charmed-kubeflow.io/) on Nvidia's DGX enabled hardware with Tensorflow. Setup follows these guides:

* [Installing MicroK8s on NVIDIA DGX](https://microk8s.io/docs/nvidia-dgx)
* [Installing Charmed Kubeflow](https://charmed-kubeflow.io/docs/install)

With a log of the setup actions taken here included in the `kubernetes-setup.md` file. 

Examples here are:
* multi-gpu-in-notebook: training Tensorflow models with GPUs in a Kubeflow Notebook
* multi-gpu-in-pipeline: (under construction) training Tensorflow models with GPUs in a Kubeflow Pipeline
* multi-node-gpu-simulated: a simulated example of multi-node training in Tensorflow, but using just a single node
* multi-node-gpu-tfjob: multi-node training in Tensorflow using the Kubeflow Training Operator's TFJob

**Author:** Michal Hucko (michal.hucko@canonical.com) and Andrew Scribner (andrew.scribner@canonical.com)