"""
Punto de entrada de la aplicación Resolutor de Sudoku.
"""

from solver import Board, EMPTY_CELL, solve_sudoku
from gui import SudokuGUI


def main() -> None:
    """Función principal de la aplicación."""
    board: Board = [[EMPTY_CELL for _ in range(9)] for _ in range(9)]

    print("Tablero inicial:")

    for row in board:
        print(row)

    solve_sudoku(board)
    print("Tablero resuelto:")

    for row in board:
        print(row)

    gui = SudokuGUI(board)
    print(type(gui).__name__)


if __name__ == "__main__":
    main()
