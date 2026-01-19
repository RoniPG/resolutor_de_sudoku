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

def is_valid_move(board: Board, row: int, col: int, value:int) -> bool:
    """
    Indica si `value` se puede colocar en (row, col) sin romper las reglas.
    """
    # Comprobar fila
    for c in range(BOARD_SIZE):
        if board[row][c] == value:
            return False
    
    # Comprobar columna
    for r in range(BOARD_SIZE):
        if board[r][col] == value:
            return False

    # Comprobar subcuadrícula
    start_row = (row // SUBGRID_SIZE) * SUBGRID_SIZE
    start_col = (col // SUBGRID_SIZE) * SUBGRID_SIZE
    for r in range(start_row, start_row + SUBGRID_SIZE):
        for c in range(start_col, start_col + SUBGRID_SIZE):
            if board[r][c] == value:
                return False

    return True


def _backtack(board: Board) -> bool:
    """
    Algoritmo de backtracking que modifica el tablero en sitio.
    Devuelve True si encuentra una solución valida.
    """
    empty_pos = find_empty_position(board)
    if empty_pos is None:
        return True  # No hay casillas vacías
    
    row, col = empty_pos
    for value in range(1, BOARD_SIZE + 1):
        if is_valid_move(board, row, col, value):
            board[row][col] = value  # Colocar el valor
            
            if _backtack(board):
                return True  # Solución encontrada
            
            board[row][col] = EMPTY_CELL  # Retroceder
    
    return False

def solve_sudoku(board):
    """
    Resuelve un sudoku usando backtracking.
    """
    if not _backtack(board):
        raise ValueError("El Sudoku no tiene solución")
    return board

