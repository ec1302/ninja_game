import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos) # Convert any iterable to a list
        self.size = size
        self.velocity = [0, 0]

    # Generate a rect for physics collisions
    def rect(self):
        # Position is actually top left of entity, not center
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap, movement=(0, 0)):
        # Create a vector that indicates how much the entity should move in that frame
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        
        # Calculating gravity (y axis)
        # min() clamps the velocity which simulates terminal velocity
        # otherwise the accelaration would not stop 
        self.velocity[1] = min(5, self.velocity[1] + 0.1)
        
        # Update x position
        self.pos[0] += frame_movement[0]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                # Detecting collision
                if frame_movement[0] > 0:
                    entity_rect.right = rect.left
                if frame_movement[0] < 0:
                    entity_rect.left = rect.right
                # After calculating rect collision above, we update 
                # entity pos to rect pos
                # pygame.Rects only work with integers, cannot have subpixel movement
                # pygame-ce does have Frects that can handle floats
                self.pos[0] = entity_rect.x

        # Update y position
        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                # Detecting collision
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                self.pos[1] = entity_rect.y

    def render(self, surf):
        surf.blit(self.game.assets['player'], self.pos)