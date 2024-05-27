import pygame
import random

class Car:
    def __init__(self, color, neural_network, position):
        self.color = color
        self.nn = neural_network
        self.position = position
        self.speed = 5
        self.size = (50, 30)

    def update(self, path):
        state = self.get_state(path)
        decision = self.nn.decision(state)
        self.position[0] += decision[0] * self.speed
        self.position[1] += decision[1] * self.speed

        # Keep the car within screen bounds
        self.position[0] = max(0, min(self.position[0], 800 - self.size[0]))
        self.position[1] = max(0, min(self.position[1], 600 - self.size[1]))

        # Reward/Punishment
        if path.is_on_path(self.position):
            reward = 1
        else:
            reward = -1
        self.nn.update_weights(reward)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (*self.position, *self.size))

    def get_state(self, path):
        # Simplified state: distance to the next path point
        next_point = path.next_point(self.position)
        return [
            next_point[0] - self.position[0],
            next_point[1] - self.position[1]
      ]
      
