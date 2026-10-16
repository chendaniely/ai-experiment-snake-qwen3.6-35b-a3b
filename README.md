# Snake

Classic Snake game built with Python and Pygame.

## Requirements

- Python 3.14+
- [uv](https://github.com/astral-sh/uv) (for dependency management)
- **Note:** uses `pygame-ce` (Community Edition) — required for Python 3.14+ support

## Getting started

```bash
# Install dependencies (creates .venv if needed)
uv sync

# Play
uv run snake
```

## Controls

| Key | Action |
|-----|--------|
| Arrow keys / WASD / IJKL | Move |
| Space | Start / Restart |
| Q | Quit (during game over) |

## How it works

```
src/snake/
├── __init__.py   # Entry point (main())
├── game.py       # Game loop, input, rendering, states
├── snake.py      # Snake body, movement, collision, eyes
├── food.py       # Food placement (avoids snake body)
└── constants.py  # Config: colors, grid size, FPS
```

Game runs at 10 ticks per second. States: INTRO → PLAYING → GAME_OVER.
Snake dies on wall or self collision. High score saved to disk.
