"""Módulo de la interfaz gráfica del resolutor de sudoku."""

import pygame
from solver import Board


class SudokuGUI:
    """
    Clase encargada de la ventana pygame y la visualización del tablero.
    """

    def __init__(self, board: Board) -> None:
        """Inicializa la GUI con un tablero inicial."""
        self.board = board
        self.window_size = 450
        self.cell_size = self.window_size // 9
        self.screen: pygame.Surface | None = None

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

    def run(self) -> None:
        """Loop principal de la aplicación."""
        pygame.init()
        self.screen = pygame.display.set_mode((self.window_size, self.window_size))
        pygame.display.set_caption("Resolutor de Sudoku")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((255, 255, 255))
            self._draw_grid()
            pygame.display.flip()
        pygame.quit()
