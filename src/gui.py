"""Módulo de la interfaz gráfica del resolutor de sudoku."""

import pygame
from solver import Board, EMPTY_CELL


class SudokuGUI:
    """
    Clase encargada de la ventana pygame y la visualización del tablero.
    """

    def __init__(self, board: Board, initial_board: Board) -> None:
        """Inicializa la GUI con un tablero inicial."""
        self.board = board
        self.initial_board = initial_board
        self.window_size = 450
        self.cell_size = self.window_size // 9
        self.screen: pygame.Surface | None = None
        self.font: pygame.font.Font | None = None

    def _draw_grid(self) -> None:
        """Dibuja la cuadrícula del Sudoku."""
        assert self.screen is not None

        for i in range(10):
            width = 3 if i % 3 == 0 else 1
            x = i * self.cell_size
            y = i * self.cell_size

            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (x, 0),
                (x, self.window_size),
                width,
            )

            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (0, y),
                (self.window_size, y),
                width,
            )

    def _draw_numbers(self) -> None:
        assert self.screen is not None
        assert self.font is not None
        for row in range(9):
            for col in range(9):
                value = self.board[row][col]
                if value == EMPTY_CELL:
                    continue
                is_initial = self.initial_board[row][col] != EMPTY_CELL
                color = (0, 0, 0) if is_initial else (0, 0, 200)
                text = self.font.render(str(value), True, color)
                x = col * self.cell_size + self.cell_size // 2
                y = row * self.cell_size + self.cell_size // 2
                rect  = text.get_rect(center=(x, y))
                self.screen.blit(text, rect)

    def run(self) -> None:
        """Loop principal de la aplicación."""
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_size, self.window_size))
        pygame.display.set_caption("Resolutor de Sudoku")
        self.font = pygame.font.SysFont(None, self.cell_size // 2)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((255, 255, 255))
            self._draw_grid()
            self._draw_numbers()
            pygame.display.flip()
        pygame.quit()
