"""Snake entity with movement, collision, and rendering."""

from __future__ import annotations

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
        # Start near center, length 5, heading right
        # Body trails behind head, so for heading right, body is to the left
        cx = constants.GRID_WIDTH // 2
        cy = constants.GRID_HEIGHT // 2
        self.body: list[tuple[int, int]] = [
            (cx - i, cy) for i in range(5)
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

        # Self collision: check new head against body excluding tail (tail will vacate)
        tail = self.body[-1]
        if (new_x, new_y) in self.body[:-1]:
            return False

        # Commit the move
        self.body.pop()
        self.body.insert(0, (new_x, new_y))
        return True

    def grow(self) -> None:
        """Add a segment (tail doubles last cell)."""
        tail = self.body[-1]
        self.body.append(tail)

    def draw(self, surface) -> None:
        """Render each segment; head brighter, direction-aware."""
        gs = constants.GRID_SIZE
        for i, (x, y) in enumerate(self.body):
            color = constants.HEAD_GREEN if i == 0 else constants.GREEN
            rect = (x * gs, y * gs, gs - 1, gs - 1)
            surface.fill(color, rect)

            # Draw eyes on head to show direction
            if i == 0:
                eye_size = 3
                if self.direction == "right":
                    e1 = (x * gs + gs - 6, y * gs + 4, eye_size, eye_size)
                    e2 = (x * gs + gs - 6, y * gs + gs - 7, eye_size, eye_size)
                elif self.direction == "left":
                    e1 = (x * gs + 3, y * gs + 4, eye_size, eye_size)
                    e2 = (x * gs + 3, y * gs + gs - 7, eye_size, eye_size)
                elif self.direction == "up":
                    e1 = (x * gs + 4, y * gs + 3, eye_size, eye_size)
                    e2 = (x * gs + gs - 7, y * gs + 3, eye_size, eye_size)
                else:  # down
                    e1 = (x * gs + 4, y * gs + gs - 6, eye_size, eye_size)
                    e2 = (x * gs + gs - 7, y * gs + gs - 6, eye_size, eye_size)
                surface.fill(constants.BLACK, e1)
                surface.fill(constants.BLACK, e2)
