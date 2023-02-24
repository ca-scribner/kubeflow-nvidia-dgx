# Multi-worker training with Keras

This is an example of doing multi-worker training with Tensorflow 2.10.0 and the keras API.  It is based on the [Tensorflow Multi-worker training with Keras](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras) demo.  This demo is similar to the [TFJob multi-worker example using Tensorflow and keras](https://github.com/kubeflow/training-operator/tree/master/examples/tensorflow/distribution_strategy/keras-API), except that this example does not require the user to have access to a `StorageClass` that supports `ReadWriteMany` `PVC`s.

This example was tested using [Charmed Kubeflow](https://charmed-kubeflow.io/) deployed in a [MicroK8s](https://microk8s.io/) multi-node Kubernetes cluster across several NVIDIA DGX nodes, but it suitable for any Kubernetes cluster that has multiple GPUs.  See the [TFJob instructions for using GPUs](https://www.kubeflow.org/docs/components/training/tftraining/#using-gpus) for more setup instructions.

# Steps

1. Build an image

```
docker build -f Dockerfile -t myDockerHub/multi_worker_training:v1.0 .
```

2. Create a `TFJob` (you can modify the type or number of GPUs in the file `multi_worker_tfjob.yaml`)

```
kubectl -n ${NAMESPACE} create -f multi_worker_tfjob.yaml
```

3. Monitor the `TFJob` progress

```
kubectl describe tfjob multi-worker
```

```
...
Status:
  Conditions:
    Last Transition Time:  2023-02-24T14:27:50Z
    Last Update Time:      2023-02-24T14:27:50Z
    Message:               TFJob multi-worker is created.
    Reason:                TFJobCreated
    Status:                True
    Type:                  Created
    Last Transition Time:  2023-02-24T14:27:57Z
    Last Update Time:      2023-02-24T14:27:57Z
    Message:               TFJob admin/multi-worker is running.
    Reason:                TFJobRunning
    Status:                True
    Type:                  Running
  Replica Statuses:
    Worker:
      Active:  2
  Start Time:  2023-02-24T14:27:52Z
Events:
  Type    Reason                   Age   From              Message
  ----    ------                   ----  ----              -------
  Normal  SuccessfulCreatePod      11s   tfjob-controller  Created pod: multi-worker-worker-0
  Normal  SuccessfulCreatePod      10s   tfjob-controller  Created pod: multi-worker-worker-1
  Normal  SuccessfulCreateService  10s   tfjob-controller  Created service: multi-worker-worker-0
  Normal  SuccessfulCreateService  10s   tfjob-controller  Created service: multi-worker-worker-1
```