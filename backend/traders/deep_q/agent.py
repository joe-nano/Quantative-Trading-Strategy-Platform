from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense
from keras.optimizers import Adam

import numpy as np
import random
from collections import deque
from traders.constants.activations import *
from configs.logger import Logger


logger = Logger(__name__).log


class DeepQAgent:
    def __init__(self, state_size: int, is_eval: bool=False, model_name: str=''):
        self.state_size = state_size  # normalized previous days
        self.action_size = 5  # buy_1, sell_1, DO Nothing, buy2, sell2
        self.memory = deque(maxlen=2000)
        self.inventory1 = []
        self.inventory2 = []
        self.model_name = model_name
        self.is_eval = is_eval
        self.gamma = 0.95  # gamma is the discount factor. It quantifies how much importance we give for future rewards.
        self.epsilon = 1.0  # Exploration and Exploitation — Epsilon (ε)
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.model = load_model("models/{}".format(model_name)) if is_eval else self._model()

    def _model(self) -> Sequential:
        model = Sequential()
        model.add(Dense(units=64, input_dim=self.state_size, activation=RELU))
        model.add(Dense(units=32, activation=RELU))
        model.add(Dense(units=8, activation=RELU))
        model.add(Dense(self.action_size, activation=LINEAR))
        model.compile(loss="mse", optimizer=Adam(lr=0.0001))
        return model

    def act(self, state) -> np.array:
        if not self.is_eval and random.random() <= self.epsilon:
            logger.info('Random action')
            return random.randrange(self.action_size)
        logger.info("Calculating using model: {}".format(self.model))
        options = self.model.predict(state)
        logger.info("Agent predict move: {}".format(options))
        return np.argmax(options[0])

    def exp_replay(self, batch_size: int):
        logger.info('Length of agent memory: {}', len(self.memory))
        mini_batch = random.sample(self.memory, batch_size)

        for state, action, reward, next_state, done in mini_batch:
            target = reward

            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(next_state)[0])

            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)

        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
