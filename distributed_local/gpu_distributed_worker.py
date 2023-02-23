import os
import json

import tensorflow as tf
import typer

from gpu_distributed_utilities import build_and_compile_cnn_model, get_cifar10_dataset

def main(
    batch_size: int = typer.Option(
        default=64,
        help="Batch size for training"
    ),
    epochs: int = typer.Option(
        default=1,
        help="Number of epochs in training",
    )):
    print("main running with visible devices:")
    print(tf.config.experimental.list_physical_devices())

    # Get some data
    X_train_scaled, y_train_encoded, X_test_scaled, y_test_encoded = get_cifar10_dataset()

    # Set up a CNN model using the tf.distribute.MultiWorkerMirroredStrategy() scope, which tells the 
    # model to coordinate with other nodes
    strategy = tf.distribute.MultiWorkerMirroredStrategy()
    with strategy.scope():
        model = build_and_compile_cnn_model()

    # Fit the model, as per some settings
    model.fit(x=X_train_scaled, y=y_train_encoded, epochs=epochs, batch_size=batch_size)


if __name__ == "__main__":
    typer.run(main)