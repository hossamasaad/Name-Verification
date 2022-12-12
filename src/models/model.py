from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Embedding, Bidirectional, LSTM, Dropout
from tensorflow.keras.callbacks import Callback


class VerificationModel(Model):

    def __init__(self, total_letters):
        super(VerificationModel, self).__init__(name='verification-model')

        self.embedding = Embedding(total_letters, 32)
        self.bi_lstm   = Bidirectional(LSTM(32))
        self.dense1    = Dense(32, activation='relu')
        self.dropout1  = Dropout(0.3)
        self.dense2    = Dense(1, activation='sigmoid')
    
    def call(self, input):

        x = self.embedding(input)
        x = self.bi_lstm(x)
        x = self.dense1(x)
        x = self.dropout1(x)
        x = self.dense2(x)

        return x


class DetectOverFitting(Callback):

    def __init__(self, threshold) -> None:
        super(DetectOverFitting, self).__init__()
        self.threshold = threshold
    
    def on_epoch_end(self, epoch, logs=None):
        ratio = logs['val_loss'] / logs['loss']
        print('Epoch: {}, val/train loss ratio: {:2f}'.format(epoch, ratio))

        if ratio > self.threshold:
            print('Stopping Training....')
            self.model.stop_training = True