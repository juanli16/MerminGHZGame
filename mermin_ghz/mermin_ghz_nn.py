from mermin_ghz import MerminGHZ
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Input, Lambda, Dense, concatenate
from tensorflow.keras.optimizers import SGD
import numpy as np


OPT = SGD(lr=0.1)


# Neural Network strategy
class MerminGHZNN(MerminGHZ):
    def __init__(self):
        super().__init__(self)
        self.strategy = "Neural Network"


    def data_gen(self):
        x = []
        y = []
        inputs = self.input_bits
        outputs = [[x, y, z] for x in [0, 1] for y in [0, 1] for z in [0, 1]]
        data = [[x, y] for x in inputs for y in outputs if self.verify(x, y)]

        for d in data:
            x.append(d[0])
            y.append(d[1])
        #x = [[0, 0], [0, 1], [1, 0], [1, 1]]
        #y = [0, 1, 1, 0]
        x = np.array(x * 1000)
        y = np.array(y * 1000)
        return x, y

    def model(self):
        inp = Input(shape=(2,))
        inp1 = Lambda(lambda x: x[:,0:1])(inp)
        inp2 = Lambda(lambda x: x[:,1:2])(inp)
        inp3 = Lambda(lambda x: x[:,2:3])(inp)
        h1_out = Dense(9, activation='relu')(inp1)
        h2_out = Dense(9, activation='relu')(inp2)
        h3_out = Dense(9, activation='relu')(inp3)
        h_out  = concatenate([h1_out, h2_out, h3_out])
        out = Dense(1, activation='sigmoid')(h_out)
        model = Model(inp, out)
        model.compile(loss='binary_crossentropy',
              optimizer=OPT,
              metrics=['accuracy'])
        return model

    def fully_connected_model(self):
        model = Sequential()
        model.add(Dense(27, activation='sigmoid', input_dim=3))
        model.add(Dense(27, activation='sigmoid'))
        model.add(Dense(3, activation='sigmoid'))
        model.compile(loss='binary_crossentropy',
              optimizer=OPT,
              metrics=['accuracy'])
        return model

    def run_model(self, communicate=False):
        x, y = self.data_gen()
        if not communicate:
            model = self.model()
        else:
            model = self.fully_connected_model()
        model.fit(x, y, epochs = 200)
        loss, metrics = model.evaluate(x, y, verbose=0)
        # print(loss, metrics)

    def run(self):
        pass


def main():
    game = MerminGHZNN()
    connected = True
    game.run_model(connected)
    """
    inputs, outputs = game.run()
    game.pre_run()
    print("Here, players have a compute resource of an one hidden layer fully connected neural network")
    game.post_run(inputs, outputs)
    counts, stats = game.multi_play(1000)
    print(counts)
    print(stats)
    """

if __name__ == "__main__":
    main()
