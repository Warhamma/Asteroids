import pygame, random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            ast_new1_vector = self.velocity.rotate(random.uniform(20, 50))
            ast_new2_vector = self.velocity.rotate(random.uniform(20, 50) * -1)
            ast_new_radii = self.radius - ASTEROID_MIN_RADIUS
            new_ast1 = Asteroid(self.position.x, self.position.y, ast_new_radii)
            new_ast1.velocity =  ast_new1_vector * 1.2
            new_ast2 = Asteroid(self.position.x, self.position.y, ast_new_radii)
            new_ast2.velocity =  ast_new2_vector * 1.2