"""
Punto de entrada de la aplicación Resolutor de Sudoku.
"""

from solver import Board, EMPTY_CELL, solve_sudoku
from gui import SudokuGUI
from puzzles import EXAMPLE_BOARD

def main() -> None:
    """Función principal de la aplicación."""
    board: Board = [row[:] for row in EXAMPLE_BOARD]

    print("Tablero inicial:")

    for row in board:
        print(row)

    solve_sudoku(board)
    print("Tablero resuelto:")

    for row in board:
        print(row)

    gui = SudokuGUI(board)
    print("Ejecutando la interfaz gráfica...")
    gui.run()


if __name__ == "__main__":
    main()
