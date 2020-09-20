from nbtex.core.Ast import Var, makeVar, isVar
from nbtex.LatexInterface.LatexFormatters import LatexMatrixFormatter
from nbtex.Dots import Dots

class Matrix(Var):
    def __init__(self, matrix=[[]], surround="[]"):
        super().__init__("matrix")
        self.matrix, self.surround = matrix, surround
        self.power, self.subs = None, None
    
    def clone(self):
        new_mtx = [[0]*len(self.matrix[0])]*len(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if isVar(self.matrix[i][j]):
                    new_mtx[i][j] = self.matrix[i][j].clone()
                else:
                    new_mtx[i][j] = self.matrix[i][j]
        return Matrix(new_mtx, self.surround)

    def __getitem__(self, ind):
        if ind >= len(self.matrix):
            raise Exception("index out of bounds")
        if len(self.matrix) == 0:
            raise Exception("empty matrix")
        if isinstance(self.matrix[0], list):
            return Matrix(self.matrix[ind])
        else:
            return Var(self.matrix[ind])

    def __pow__(self, power):
        self.power = makeVar(power)
        return self

    def subscript(self, subs):
        self.subs = makeVar(subs)
        return self

    @staticmethod
    def builder():
        return MatrixBuilder()

    @property
    def T(self):
        if len(self.matrix) == 0:
            return self
        rows, cols = len(self.matrix), len(self.matrix[0])
        matrix = [[self.matrix[j][i] for j in range(rows)] for i in range(cols)]
        return Matrix(matrix, self.surround)

    def build(self):
        begin, end = self.create_env()
        mtx = self.get_built_base_matrix()
        # print(mtx)
        power, subs = self.get_pow_subs()
        return r"" + begin + mtx + end + power + subs + r""

    def create_env(self):
        return LatexMatrixFormatter.create_env(self.surround)

    def get_built_base_matrix(self):
        mtx = self.get_built_matrix_elements()
        return LatexMatrixFormatter.matrix_to_latex(mtx)

    def get_built_matrix_elements(self):
        mtx = [[makeVar(cell) for cell in row] for row in self.matrix]
        mtx = [[cell.build() for cell in row] for row in mtx]
        return mtx

    def get_pow_subs(self):
        if self.power is not None:
            power = LatexMatrixFormatter.power_of_matrix(self.power.build())
        else:
            power = LatexMatrixFormatter.empty_power()

        if self.subs is not None:
            subs = LatexMatrixFormatter.subscript_of_matrix(self.subs.build())
        else:
            subs = LatexMatrixFormatter.empty_subscript()
        return power, subs


class MatrixBuilder:
    def __init__(self):
        self.matrix, self.cols = [], None

    def add(self, *args):
        if self.cols is None:
            self.cols = len(args)
        elif not self.cols == len(args):
            raise Exception(
                f"Different dimensions for matrix builder. dim1:{self.cols} dim2:{len(args)}"
            )
        self.matrix.append(list(args))
        return self

    def create(self, surround="[]"):
        return Matrix(self.matrix, surround)


def hasHoriDots(elements, m):
    elerowlen = max([len(ele) for ele in elements])
    return not elerowlen == len(m[0])


def hasVertDots(elements, m):
    return not len(elements) == len(m)


class MatrixWithDots(Matrix):
    def __init__(self, elements, shape=None, surround="[]"):
        # resolve elements
        self._elements_check(elements)
        self.elements = elements
        rows, cols = self._get_dimensions(elements, shape)
        matrix = self._construct_matrix(rows, cols, elements)
        super().__init__(matrix, surround)

    def _elements_check(self, elements):
        if (
            not isinstance(elements, list)
            or len(elements) == 0
            or not isinstance(elements[0], list)
        ):
            raise Exception("need to pass list of list")

    def _get_dimensions(self, elements, shape):
        minrows, mincols = len(elements), max([len(row) for row in elements])
        if shape is None:
            rows = minrows + 1 if minrows != 1 else minrows
            cols = mincols + 1 if mincols != 1 else mincols
        else:
            try:
                rows, cols = shape
                rows, cols = int(rows), int(cols)
            except:
                raise Exception("shape should be of type tuple(int,int)")
            if rows < minrows or cols < mincols:
                raise Exception("shape >= (row, cols) of elements")
        return rows, cols

    def _construct_matrix(self, rows, cols, elements):
        m = self._get_zero_matrix_of_dimensions(rows, cols)
        i = self._fill_with_elements(0, elements, m)
        i = self._fill_with_vertical_dots(i, elements, m)
        self._fill_last_row_with_elements(elements, m)
        self._put_diagonal_dot(elements, m)
        return m

    def _get_zero_matrix_of_dimensions(self, rows, cols):
        return [[0] * cols for i in range(rows)]

    def _fill_with_elements(self, start, elements, m):
        i = start
        while i < len(elements) - 1:
            m[i] = self._get_row_with_elements(elements, i, len(m[i]))
            i += 1
        return i

    def _get_row_with_elements(self, elements, row_index, mlen):
        row = elements[row_index]
        new_row = [0] * mlen
        j = 0
        while j < len(row) - 1:
            new_row[j] = row[j]
            j += 1
        while j < mlen - 1:
            new_row[j] = Dots("h")
            j += 1
        new_row[j] = row[len(row) - 1]
        return new_row

    def _fill_with_vertical_dots(self, start, elements, m):
        i = start
        while i < len(m) - 1:
            m[i] = [Dots("v")] * len(m[i])
            i += 1
        
        return i

    def _fill_last_row_with_elements(self, elements, m):
        m[len(m) - 1] = self._get_row_with_elements(
            elements, len(elements) - 1, len(m[len(m) - 1])
        )

    def _put_diagonal_dot(self, elements, m):
        dli, dlj = len(m) - 2, len(m[0]) - 2
        if (
            isinstance(m[dli][dlj], Dots)
            and hasHoriDots(elements, m)
            and hasVertDots(elements, m)
        ):

            m[dli][dlj] = Dots("d")

    @property
    def T(self):
        raise Exception("transpose of dotted matrix not allowed")
