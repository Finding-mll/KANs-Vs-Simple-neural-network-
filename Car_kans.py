import pygame
import torch

class Car:
    def __init__(self, color, neural_network, position):
        self.color = color
        self.nn = neural_network
        self.position = torch.tensor(position, dtype=torch.float32)
        self.speed = 5
        self.size = (50, 30)

    def update(self, path):
        state = self.get_state(path)
        decision = self.nn(state).detach().numpy()
        self.position[0] += decision[0] * self.speed
        self.position[1] += decision[1] * self.speed

        self.position[0] = max(0, min(self.position[0], 800 - self.size[0]))
        self.position[1] = max(0, min(self.position[1], 600 - self.size[1]))

        if not path.is_on_path(self.position):
            self.position[0] -= decision[0] * self.speed
            self.position[1] -= decision[1] * self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (*self.position.numpy(), *self.size))

    def get_state(self, path):
        next_point = path.next_point(self.position.numpy())
        return torch.tensor([next_point[0] - self.position[0], next_point[1] - self.position[1]], dtype=torch.float32)
      
