class Matrix:
    """
    This class creates a matrix with its name and dimension (nRows, nColumns)
    Supports the following operations:
        - using in string context
        - using in index context (getting and setting values)
        - using in len() function
        - printing the number of empty slots left in the matrix
        - addition of two instances of the class Matrix
        - using instance of the class as an iterator
        - saving to a file
        - loading data from a file
    """

    def __init__(
        self,
        name: str,
        nRows: int,
        nColumns: int,
    ):
        self.name = name
        # check if rows and columns are positive integers
        if nRows > 0 and nColumns > 0:
            self.nRows = nRows
            self.nColumns = nColumns
        else:
            raise ValueError("Dimensions must be positive integers")

        # create a table with nRows and nColumns
        self.__table = [[0 for i in range(nColumns)] for j in range(nRows)]

    # magic method for using instance in string context (aka print(instance))
    def __str__(self):
        """
        This method prints the matrix and some extra info
        """
        # print the header
        string = f"=== Table '{self.name}': {self.nRows} x {self.nColumns} ===\n\n"
        # draw the matrix
        for i in range(self.nRows):
            for j in range(self.nColumns):
                string += str(self.__table[i][j]) + " "
            string += "\n"
        # print extra info
        string += f"\n=== Number of non-zero elements: {self.__len__()} ==="
        return string

    def __check_index(self, index):
        """
        This private method checks if the index is a list of two positive integers
        and is in the range of the table
        """
        if not isinstance(index, tuple):
            raise TypeError(
                "Index must be a tuple of two positive integers, got " + f"{type(index)} instead"
            )

        if len(index) == 2 and isinstance(index[0], int) and isinstance(index[1], int):
            if index[0] not in range(self.nRows) or index[1] not in range(self.nColumns):
                raise IndexError(
                    f"Index {index} is out of range of the table "
                    + f"'{self.name}' ({self.nRows} x {self.nColumns})"
                )
        else:
            raise TypeError("Index must be a list of two integers")

    # magic method for using instance in index context
    def __getitem__(self, index):
        """
        This method returns the value of the table at the index
        """
        self.__check_index(index)
        return self.__table[index[0]][index[1]]

    # magic method for setting data to the instance in index context
    def __setitem__(self, index, value):
        """
        This method sets non-zero value at index of the table
        """
        self.__check_index(index)
        self.__table[index[0]][index[1]] = value
        # print(self.__table)

    # magic method for using instance inside len() function
    def __len__(self):
        """
        This method returns the number of non-zero values inside the matrix
        """
        flat_table_non_zero = [col for row in self.__table for col in row if col != 0]
        return len(flat_table_non_zero)

    def saves(self):
        """
        Method that returns the number of empty slots left in the matrix
        """
        dimension = self.nRows * self.nColumns
        return dimension - self.__len__()

    def __check_matrix_demisions(self, matrix):
        """
        This private method checks if the matrix has the same dimensions as the instance
        """
        if self.nRows != matrix.nRows or self.nColumns != matrix.nColumns:
            raise ValueError(
                f"Matrix '{matrix.name}' has different dimensions than the instance '{self.name}': "
                + f"{matrix.nRows} x {matrix.nColumns} != {self.nRows} x {self.nColumns} "
            )

    # magic method for using instance in + context
    def __add__(self, matrix):
        """
        Method for addition of the instances of a Matrix class
        """
        self.__check_matrix_demisions(matrix)

        # create a new instance of the class
        new_matrix = Matrix(f"{self.name}", self.nRows, self.nColumns)
        # add the values of the two instances
        for i in range(self.nRows):
            for j in range(self.nColumns):
                new_matrix[(i, j)] = self[(i, j)] + matrix[(i, j)]

        return new_matrix

    def store(self):
        """
        Method for saving matrix values to a file
        """
        print(f"Storing data to '{self.name}.matrix'")
        matrix = {}
        # saving only non-zero values
        for i in range(self.nRows):
            for j in range(self.nColumns):
                if self.__table[i][j] != 0:
                    matrix[(i, j)] = self.__table[i][j]

        # save results to a file
        # file's format example: {(0, 1): 100, (1, 2): 150}
        with open(f"{self.name}.matrix", "w") as fd:
            fd.write(str(matrix))

    def load(self):
        """
        Method for loading matrix values from a file
        """
        print(f"Loading data from '{self.name}.matrix'")
        with open(f"{self.name}.matrix", "r") as fd:
            # eval is unsafe, better to use ast module literal_eval
            matrix = eval(fd.read())

        # update the instance with the results
        # do not update self.__table directly to
        # avoid possible IndexError exceptions
        # (will be using __setitem__ method instead)
        for i in range(self.nRows):
            for j in range(self.nColumns):
                if (i, j) in matrix:
                    self[(i, j)] = matrix[(i, j)]
                else:
                    self[(i, j)] = 0

    # magic method for using instance in iterator context
    def __iter__(self):
        """
        This method returns an iterator for the Matrix table
        """
        return self.__table.__iter__()


# initialize table
table1 = Matrix("table1", 2, 3)

# set values at indices
table1[0, 1] = 100
table1[1, 2] = 150

# out of range index
# table1[25, 25] = 100500

# print index value
print("Matrix value at (1,2):", table1[1, 2])

# print table length
print("Number of busy slots:", len(table1))

# print how much space left
print("Space left:", table1.saves())

# print the whole table
print(table1)

# save matrix values a file
table1.store()

# load matrix values from a file
table1.load()


# initialize table2
table2 = Matrix("table2", 2, 3)

# set values at indices
table2[0, 1] = 12
table2[1, 2] = 15
table2[0, 0] = 4

print(table2)

# add up table1 and table2
table3 = table1 + table2

# print results
print("Results after addition\n", table3)

print("Use Matrix class in iteration context:")
for row in table3:
    for col in row:
        print(col, end=" ")
    print()
