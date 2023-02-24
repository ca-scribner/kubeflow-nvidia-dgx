# Nvidia DGX Kubeflow demos

This document contains several demo workloads that were executed using [Charmed Kubeflow 1.6](https://charmed-kubeflow.io/) on Nvidia's DGX enabled hardware with Tensorflow. Setup follows these guides:

* [Installing MicroK8s on NVIDIA DGX](https://microk8s.io/docs/nvidia-dgx)
* [Installing Charmed Kubeflow](https://charmed-kubeflow.io/docs/install)

With a log of the setup actions taken here included in the `kubernetes-setup.md` file. 

Examples here are:
* multi-gpu-in-notebook: example of how you can train Tensorflow models in a Jupyter Notebook.  
* distributed_local

We provide also examples on how to use Kubeflow instance with multiple GPUs. In the file `gpu-pipeline.ipynb` you can find basic example of [Kubeflow pipeline](https://www.kubeflow.org/docs/components/pipelines/v1/introduction/), where we demonstrate multi GPU training on Tensorflow model. This example provides instrctions on how to deploy the trained model with [MlFlow](https://mlflow.org/) and [Seldon core](https://www.seldon.io/solutions/open-source-projects/core).

In the file `gpu-notebook.ipynb` you can find example [Jupyter notebook](https://jupyter.org/) with the same classiffier as in case of pipeline. Notebook also uses multi GPU setup.

**Author:** Michal Hucko (michal.hucko@canonical.com)