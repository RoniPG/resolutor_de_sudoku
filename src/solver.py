from typing import List, Tuple, Optional

"""
Módulo encargado de la lógica para resolver sudokus.
"""

Board = List[List[int]]  # Representación de un tablero de Sudoku
Position = Tuple[int, int]  # Representación de una posición en el tablero

BOARD_SIZE = 9
SUBGRID_SIZE = 3
EMPTY_CELL = 0


def find_empty_position(board: Board) -> Optional[Position]:
    """
    Devuelve la posición (fila, columna) de la siguiente casiila vacía, o None si el tablero está completo.
    """
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY_CELL:
                return (row, col)
    return None


def solve_sudoku(board):
    """
    Resuelve un sudoku usando backtracking.
    """
    pass
