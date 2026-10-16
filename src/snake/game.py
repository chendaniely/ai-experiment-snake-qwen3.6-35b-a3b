"""Main game class — input, update, render loop."""

import pygame
import sys

from . import constants
from .snake import Snake
from .food import Food


class SnakeGame:
    """Orchestrates game state, events, and rendering."""

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(
            (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
        )
        pygame.display.set_caption(constants.TITLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("monospace", constants.FONT_SIZE)
        self.overlay_font = pygame.font.SysFont(
            "monospace", constants.OVERLAY_FONT_SIZE, bold=True
        )
        self.grid_width = constants.GRID_WIDTH
        self.grid_height = constants.GRID_HEIGHT
        self.reset()

    def reset(self) -> None:
        """Start a fresh game."""
        self.snake = Snake()
        self.food = Food(self.snake)
        self.score = 0
        self.game_over = False

    def handle_events(self) -> None:
        """Process pygame events and direction changes."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.reset()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    continue
                key_map = {
                    pygame.K_UP: ("up", "down"),
                    pygame.K_DOWN: ("down", "up"),
                    pygame.K_LEFT: ("left", "right"),
                    pygame.K_RIGHT: ("right", "left"),
                }
                if event.key in key_map:
                    desired, opposite = key_map[event.key]
                    if self.snake.direction != opposite:
                        self.snake.direction = desired

    def update(self) -> None:
        """Advance game state by one tick."""
        if self.game_over:
            return
        if self.snake.move():
            if self.snake.head == self.food.position:
                self.score += 1
                self.food.regrow(self.snake)
                # Grow the snake back (move removed the tail)
                self.snake.body.append(self.snake.body[-1])
        else:
            self.game_over = True

    def render(self) -> None:
        """Draw everything."""
        self.screen.fill(constants.BLACK)
        self.food.draw(self.screen)
        self.snake.draw(self.screen)
        self._draw_score()
        if self.game_over:
            self._draw_overlay()
        pygame.display.flip()

    def _draw_score(self) -> None:
        label = self.font.render(f"Score: {self.score}", True, constants.WHITE)
        self.screen.blit(label, (10, 10))

    def _draw_overlay(self) -> None:
        # Semi-transparent background
        overlay = pygame.Surface(
            (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
        )
        overlay.set_alpha(180)
        overlay.fill(constants.BLACK)
        self.screen.blit(overlay, (0, 0))

        title = self.overlay_font.render("GAME OVER", True, constants.RED)
        title_rect = title.get_rect(
            center=(
                constants.WINDOW_WIDTH // 2,
                constants.WINDOW_HEIGHT // 2 - 20,
            )
        )
        self.screen.blit(title, title_rect)

        score_text = self.font.render(
            f"Final Score: {self.score}", True, constants.WHITE
        )
        score_rect = score_text.get_rect(
            center=(
                constants.WINDOW_WIDTH // 2,
                constants.WINDOW_HEIGHT // 2 + 20,
            )
        )
        self.screen.blit(score_text, score_rect)

        hint = self.font.render(
            "SPACE to restart · Q to quit", True, constants.DARK_GREEN
        )
        hint_rect = hint.get_rect(
            center=(
                constants.WINDOW_WIDTH // 2,
                constants.WINDOW_HEIGHT // 2 + 60,
            )
        )
        self.screen.blit(hint, hint_rect)

    def run(self) -> None:
        """Main game loop."""
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(constants.FPS)
