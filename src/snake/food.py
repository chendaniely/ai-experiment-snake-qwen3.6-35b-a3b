"""Food placement on the grid, avoiding the snake's body."""

from __future__ import annotations

import random
import pygame

from . import constants
from .snake import Snake


class Food:
    """A single food item that respawns elsewhere after being eaten."""

    def __init__(self, snake: Snake) -> None:
        self.position = self._spawn(snake)

    def regrow(self, snake: Snake) -> None:
        """Pick a new free cell."""
        self.position = self._spawn(snake)

    def _spawn(self, snake: Snake) -> tuple[int, int]:
        occupied = set(snake.body)
        free_cells = [
            (x, y)
            for x in range(constants.GRID_WIDTH)
            for y in range(constants.GRID_HEIGHT)
            if (x, y) not in occupied
        ]
        return random.choice(free_cells)

    def draw(self, surface: pygame.Surface) -> None:
        """Render food as a red square."""
        gs = constants.GRID_SIZE
        rect = pygame.Rect(
            self.position[0] * gs,
            self.position[1] * gs,
            gs - 1,
            gs - 1,
        )
        pygame.draw.rect(surface, constants.RED, rect)
