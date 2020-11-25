import tensorflow as tf
import nni


def load_dataset():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    return (x_train/255., y_train), (x_test/255., y_test)


def create_model(num_units, dropout_rate, lr, activation):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(num_units, activation=activation),
        tf.keras.layers.Dropout(dropout_rate),
        tf.keras.layers.Dense(10, activation="softmax")
    ])

    model.compile(
        loss="sparse_categorical_crossentropy",
        optimizer=tf.keras.optimizers.Adam(lr=lr),
        metrics=["accuracy"]
    )
    return model


class ReportIntermediates(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs=None):
        acc = logs.get("val_accuracy") or 0.
        nni.report_intermediate_result(acc)


def main(params):
    num_units = params.get("num_units")
    dropout_rate = params.get("dropout_rate")
    lr = params.get("lr")
    batch_size = params.get("batch_size")
    activation = params.get("activation")

    model = create_model(num_units, dropout_rate, lr, activation)

    (x_train, y_train), (x_test, y_test) = load_dataset()

    _ = model.fit(
        x_train, y_train,
        validation_data=(x_test, y_test),
        epochs=10,
        verbose=False,
        batch_size=batch_size,
        callbacks=[ReportIntermediates()]
    )

    _, acc = model.evaluate(x_test, y_test, verbose=False)
    nni.report_final_result(acc)


if __name__ == "__main__":
    params = {
        "num_units": 32,
        "dropout_rate": 0.1,
        "lr": 0.0001,
        "batch_size": 32,
        "activation": "relu"
    }

    tuned_params = nni.get_next_parameter()
    params.update(tuned_params)

    main(params)
