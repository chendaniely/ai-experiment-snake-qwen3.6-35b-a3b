"""Snake entity with movement, collision, and rendering."""

from __future__ import annotations

import pygame

from . import constants


class Snake:
    """A snake that grows when eating and dies on wall/self collision."""

    DIRECTIONS = {
        "up": (0, -1),
        "down": (0, 1),
        "left": (-1, 0),
        "right": (1, 0),
    }

    def __init__(self) -> None:
        cx = constants.GRID_WIDTH // 2
        cy = constants.GRID_HEIGHT // 2
        # body index 0 = head; body grows leftward
        self.body: list[tuple[int, int]] = [
            (cx + i, cy) for i in range(4)
        ]
        self.direction = "right"

    @property
    def head(self) -> tuple[int, int]:
        return self.body[0]

    def move(self) -> bool:
        """Advance one cell. Returns True if alive, False if hit wall or self."""
        dx, dy = self.DIRECTIONS[self.direction]
        hx, hy = self.head
        new_x = hx + dx
        new_y = hy + dy

        # Wall collision
        if new_x < 0 or new_x >= constants.GRID_WIDTH:
            return False
        if new_y < 0 or new_y >= constants.GRID_HEIGHT:
            return False

        # Self collision
        if (new_x, new_y) in self.body:
            return False

        self.body.insert(0, (new_x, new_y))
        self.body.pop()  # remove tail; grow handled by caller
        return True

    def draw(self, surface: pygame.Surface) -> None:
        """Render each segment; head is brighter."""
        gs = constants.GRID_SIZE
        for i, (x, y) in enumerate(self.body):
            color = constants.GREEN if i == 0 else constants.DARK_GREEN
            rect = pygame.Rect(x * gs, y * gs, gs - 1, gs - 1)
            pygame.draw.rect(surface, color, rect)
