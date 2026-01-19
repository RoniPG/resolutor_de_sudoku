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

    def run(self) -> None:
        """Loop principal de la aplicación."""
        pygame.init()
        screen = pygame.display.set_mode((400, 400))
        pygame.display.set_caption("Resolutor de Sudoku")
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()

        
