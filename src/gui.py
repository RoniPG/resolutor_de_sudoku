"""Módulo de la interfaz gráfica del resolutor de sudoku."""

from solver import Board


class SudokuGUI:
    """
    Clase encargada de la ventana pygame y la visualización del tablero.
    """

    def __init__(self, board: Board) -> None:
        """Inicializa la GUI con un tablero inicial."""
        self.board = board

    def run(self) -> None:
        """Loop principal de la aplicación (aún no implementado)."""
        pass
