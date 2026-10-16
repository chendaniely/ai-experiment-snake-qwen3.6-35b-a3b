"""Main game class — input, update, render loop."""

import pygame
import sys

from . import constants
from .snake import Snake
from .food import Food


class SnakeGame:
    """Orchestrates game states: INTRO → PLAYING → GAME_OVER."""

    STATE_INTRO = "intro"
    STATE_PLAYING = "playing"
    STATE_GAME_OVER = "game_over"

    def __init__(self) -> None:
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode(
            (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
        )
        pygame.display.set_caption(constants.TITLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, constants.FONT_SIZE)
        self.title_font = pygame.font.SysFont(None, constants.OVERLAY_FONT_SIZE, bold=True)
        self.small_font = pygame.font.SysFont(None, constants.SMALL_FONT)
        self.state = self.STATE_INTRO
        self.score = 0
        self.snake = None
        self.food = None
        self.high_score = self._load_high_score()

    def _load_high_score(self) -> int:
        """Load high score from a local file."""
        try:
            with open("high_score.txt", "r") as f:
                return int(f.read().strip())
        except (FileNotFoundError, ValueError):
            return 0

    def _save_high_score(self) -> None:
        """Persist high score."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as f:
                f.write(str(self.high_score))

    def start_game(self) -> None:
        """Begin a new game."""
        self.snake = Snake()
        self.food = Food(self.snake)
        self.score = 0
        self.state = self.STATE_PLAYING

    def handle_events(self) -> None:
        """Process pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # Intro screen — press any key to start
                if self.state == self.STATE_INTRO:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.start_game()
                    continue

                # Game over — Space/Enter to restart, Q to quit
                if self.state == self.STATE_GAME_OVER:
                    if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                        self.start_game()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                    continue

                # Playing — arrow keys, WASD, IJKL
                if self.state == self.STATE_PLAYING:
                    key_map = {
                        pygame.K_UP: ("up", "down"),
                        pygame.K_DOWN: ("down", "up"),
                        pygame.K_LEFT: ("left", "right"),
                        pygame.K_RIGHT: ("right", "left"),
                        pygame.K_w: ("up", "down"),
                        pygame.K_s: ("down", "up"),
                        pygame.K_a: ("left", "right"),
                        pygame.K_d: ("right", "left"),
                        pygame.K_i: ("up", "down"),
                        pygame.K_k: ("down", "up"),
                        pygame.K_j: ("left", "right"),
                        pygame.K_l: ("right", "left"),
                    }
                    if event.key in key_map:
                        desired, opposite = key_map[event.key]
                        if self.snake.direction != opposite:
                            self.snake.direction = desired

    def update(self) -> None:
        """Advance game state."""
        if self.state != self.STATE_PLAYING:
            return

        if self.snake.move():
            if self.snake.head == self.food.position:
                self.score += 1
                self.food.regrow(self.snake)
                self.snake.grow()
        else:
            self.state = self.STATE_GAME_OVER
            self._save_high_score()

    def render(self) -> None:
        """Draw the current state."""
        self.screen.fill(constants.DARK_BG)

        if self.state == self.STATE_INTRO:
            self._draw_intro()
        elif self.state == self.STATE_PLAYING:
            self._draw_playing()
        else:
            self._draw_game_over()

        pygame.display.flip()

    def _draw_intro(self) -> None:
        """Draw the intro/start screen."""
        # Title
        title = self.title_font.render("SNAKE", True, constants.GREEN)
        title_rect = title.get_rect(center=(
            constants.WINDOW_WIDTH // 2,
            constants.WINDOW_HEIGHT // 3,
        ))
        self.screen.blit(title, title_rect)

        # Instructions
        lines = [
            "Arrow keys / WASD / IJKL to move",
            "Eat the red food to grow",
            "Don't hit the walls or yourself",
            "",
            "Press SPACE or ENTER to start",
        ]
        for i, line in enumerate(lines):
            color = constants.GREEN if i == len(lines) - 1 else constants.DARK_GRAY
            surf = self.font.render(line, True, color)
            rect = surf.get_rect(center=(
                constants.WINDOW_WIDTH // 2,
                constants.WINDOW_HEIGHT // 2 + 20 + i * 32,
            ))
            self.screen.blit(surf, rect)

        # High score
        if self.high_score > 0:
            hs = self.small_font.render(f"High Score: {self.high_score}", True, constants.GRAY)
            hs_rect = hs.get_rect(center=(
                constants.WINDOW_WIDTH // 2,
                constants.WINDOW_HEIGHT - 50,
            ))
            self.screen.blit(hs, hs_rect)

    def _draw_playing(self) -> None:
        """Draw during gameplay."""
        # Grid lines
        gs = constants.GRID_SIZE
        for x in range(0, constants.WINDOW_WIDTH, gs):
            pygame.draw.line(self.screen, constants.GRID_COLOR, (x, 0), (x, constants.WINDOW_HEIGHT))
        for y in range(0, constants.WINDOW_HEIGHT, gs):
            pygame.draw.line(self.screen, constants.GRID_COLOR, (0, y), (constants.WINDOW_WIDTH, y))

        self.food.draw(self.screen)
        self.snake.draw(self.screen)

        # Score
        label = self.font.render(f"Score: {self.score}", True, constants.WHITE)
        self.screen.blit(label, (10, 10))

        if self.high_score > 0:
            hs = self.small_font.render(f"Best: {self.high_score}", True, constants.GRAY)
            self.screen.blit(hs, (constants.WINDOW_WIDTH - hs.get_width() - 10, 10))

    def _draw_game_over(self) -> None:
        """Draw the game over screen."""
        # Dim overlay
        overlay = pygame.Surface(
            (constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT)
        )
        overlay.set_alpha(180)
        overlay.fill(constants.BLACK)
        self.screen.blit(overlay, (0, 0))

        # Title
        title = self.title_font.render("GAME OVER", True, constants.RED)
        title_rect = title.get_rect(center=(
            constants.WINDOW_WIDTH // 2,
            constants.WINDOW_HEIGHT // 2 - 60,
        ))
        self.screen.blit(title, title_rect)

        # Score
        score_text = self.font.render(f"Score: {self.score}", True, constants.WHITE)
        score_rect = score_text.get_rect(center=(
            constants.WINDOW_WIDTH // 2,
            constants.WINDOW_HEIGHT // 2 - 10,
        ))
        self.screen.blit(score_text, score_rect)

        # High score
        if self.score >= self.high_score and self.score > 0:
            hs_text = self.font.render("New High Score!", True, constants.ORANGE)
        else:
            hs_text = self.small_font.render(f"High Score: {self.high_score}", True, constants.GRAY)
        hs_rect = hs_text.get_rect(center=(
            constants.WINDOW_WIDTH // 2,
            constants.WINDOW_HEIGHT // 2 + 25,
        ))
        self.screen.blit(hs_text, hs_rect)

        # Hint
        hint = self.font.render("Press SPACE to play again", True, constants.GREEN)
        hint_rect = hint.get_rect(center=(
            constants.WINDOW_WIDTH // 2,
            constants.WINDOW_HEIGHT // 2 + 70,
        ))
        self.screen.blit(hint, hint_rect)

    def run(self) -> None:
        """Main game loop."""
        while True:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(constants.FPS)
