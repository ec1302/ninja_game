import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos) # Convert any iterable to a list
        self.size = size
        self.velocity = [0, 0]

    def update(self, movement=(0, 0)):
        # Create a vector that indicates how much the entity should move in that frame
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        # Update x position
        self.pos[0] += frame_movement[0]
        # Update y position
        self.pos[1] += frame_movement[1]

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)