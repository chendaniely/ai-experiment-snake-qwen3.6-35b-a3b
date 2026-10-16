"""Food placement on the grid, avoiding the snake's body."""

from __future__ import annotations

import random

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

    def draw(self, surface) -> None:
        """Render food as a red circle."""
        gs = constants.GRID_SIZE
        cx = self.position[0] * gs + gs // 2
        cy = self.position[1] * gs + gs // 2
        surface.fill(constants.RED, (self.position[0] * gs, self.position[1] * gs, gs - 1, gs - 1))
        # Highlight dot
        surface.fill(constants.ORANGE, (cx - 2, cy - 2, 4, 4))
