from cell import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for c in range(self._num_cols):
            col_cells = []
            for r in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
            
            
            for c in range(self._num_cols):
                for r in range(self._num_rows):                           
                    self._draw_cell(c, r)
                

    def _draw_cell(self, c, r):
        if self._win is None:
            return

        x1 = self._x1 + c  * self._cell_size_x
        y1 = self._y1 + r  * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[c][r].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.05)