import random

class NeuralNetwork:
    def __init__(self):
        self.weights = [random.uniform(-1, 1) for _ in range(4)]

    def decision(self, state):
        # Simple linear combination of state and weights
        decision_value = sum(w * s for w, s in zip(self.weights, state))
        if decision_value > 0:
            return [1, 0]  # Move right
        else:
            return [0, 1]  # Move down

    def update_weights(self, reward):
        # Adjust weights based on reward (simple reinforcement learning step)
        for i in range(len(self.weights)):
            self.weights[i] += reward * 0.1  # Learning rate
