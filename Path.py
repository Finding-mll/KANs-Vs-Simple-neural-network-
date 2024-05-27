import pygame

class Path:
    def __init__(self):
        self.points = [(100, 500), (400, 300), (700, 500)]

    def draw(self, screen):
        pygame.draw.lines(screen, (255, 255, 255), False, self.points, 5)
        pygame.draw.circle(screen, (0, 255, 0), self.points[0], 10)  # Start
        pygame.draw.circle(screen, (255, 0, 0), self.points[-1], 10)  # End

    def is_on_path(self, position):
        # Simple collision detection for demonstration purposes
        for point in self.points:
            if abs(position[0] - point[0]) < 50 and abs(position[1] - point[1]) < 50:
                return True
        return False

    def next_point(self, position):
        # Return the next point on the path
        for point in self.points:
            if position[0] < point[0]:
                return point
        return self.points[-1]
      
