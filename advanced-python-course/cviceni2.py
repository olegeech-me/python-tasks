#!/usr/bin/python3
import time,sys

## EX 1
#
class Matrix:
    '''Store values using a dictionary
       with tuple as an index
    '''
    def __init__(self,name,rows,cols):
        '''Initialize matrix geometry, name and storage'''
        self.name = name
        self.rows = rows
        self.cols = cols
        self.storage = dict()  # create an emppy dictionary

    def __len__(self):
        '''Compute matrix length = number of nonzero elements'''
        return len(self.storage) 

    def __getitem__(self,index):
        '''Get value from a dictionary
           m = Matrix('test',4,4)
           m[2,1] # Matrix.__getitem__(m,(2,1))
        '''
        self.__check(index)
        return self.storage.get(index,0)

    def __setitem__(self,index,value):
        '''Set value to a dictionary
           m = Matrix('test',4,4)
           m[2,1] = 100 # Matrix.__setitem__(m, (2,1), 100)
        '''
        self.__check(index)
        if value == 0:
            return
        self.storage[index] = value

    def __add__(self,mtx):
        '''Magic method for + operator
           We can perform + on matrices with the same geometry
           m = Matrix('first',5,4)
           n = Matrix('second',5,4)
           q = Matrix('third',5,6)
           z = m + n # z = Matrix.__add__(m,n)
           w = m + q # Different geometry => Exception
        '''
        if self.rows != mtx.rows or self.cols != mtx.cols:
            raise ValueError('Geometry of matrices are different')

        # Create a brand new matrix
        result = Matrix(self.name + '+' + mtx.name, self.rows, self.cols)


        # Compute values
        for row in range(self.rows):
            for col in range(self.cols):
                result[row,col] = self[row,col] + mtx[row,col]

        return result

    def __iter__(self):
        '''Iterator support'''
        self.it = iter(self.storage.keys())
        return self

    def __next__(self):
        '''Get next non-zero element from dictionary storage'''
        return self.storage.get(next(self.it))

    def __check(self,index):
        '''
        Index helper. This method checks for index validity
        Index not a tuple => ValueError
        Index length <> 2 => ValueError
        Values in index out of range => IndexError
        '''
        if not isinstance(index,tuple):
            raise ValueError('Index type not supported')
        if len(index) != 2:
            raise ValueError('Index length out of range')
        if index[0] < 0 or index[0] >= self.rows or index[1] < 0 or index[1] >= self.cols:
            raise IndexError(f'Index out of range: [{index[0]},{index[1]}]')

    def saves(self):
        '''How many space this storage saves
           saves = matrix geometry - number of nonzero elements
        '''
        return self.rows*self.cols - len(self)

    def print(self):
        '''
        Method prints the whole matrix, including zero elements.
        It uses classical for-inside-for algorithm
        '''
        print(f"== Table '{self.name}': {self.rows} x {self.cols} ==")
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.storage.get((row,col),0), ' ', end='')
            print()
        print(f"= Number of non-zero elements: {len(self)}")

    def store(self):
        '''Storage matrix to a file
           Backup file structure for matrix with name 'sample':

           m = Matrix('sample', 4, 8)
           m[0,0] = 1000
           m[1,1] = 2000
           m.store()

           --- sample.matrix ---
           name:sample
           shape: 4x8
           0,0:1000
           1,1:2000
           ---------------------
        '''
        filename = self.name + '.matrix'
        with open(filename,'w') as out:
            out.write(f'name:{self.name}\n')
            out.write(f'shape:{self.rows}x{self.cols}\n')
            for row,col in self.storage.keys():
                out.write(f'{row},{col}:{self.storage.get((row,col))}\n')

    def load(self,filename=''):
        '''Load matrix from a file
        Backup file must have a compatible geometry ( rows x columns )
        !!! There is no backup file format check !!!
        '''
        if not filename:
            filename = self.name + '.matrix'
        elements = 0
        with open(filename) as inp:
            for line in inp:
                line = line[:-1]
                key,value = line.split(':')
                if key == 'name':
                    print(f'restoring matrix from backup: {value}')
                    continue
                if key == 'shape':
                    shape = tuple(value)
                    rows,cols = int(shape[0]),int(shape[2])
                    if rows != self.rows or cols != self.cols:
                        raise TypeError(f'Failed to load data from different matrix shape. Expected {self.rows}x{self.cols}, got {rows}x{cols}')
                    continue
                row,col = key.split(',')
                self[int(row),int(col)] = value
                elements += 1
        print(f'{elements} non-zero element(s) restored')

## EX 2
#

def trace(msg='TRACE'):
    def internal(fn):
        def subinternal(*args):
            print(f'{msg} function name: {fn.__name__}')
            print(f'{msg} number of args: {len(args)}')
            start = time.time()
            ret = fn(*args)
            print(f'{msg} runtime: ({int((time.time() - start)*1_000_000)} usec)')
            return ret
        return subinternal
    return internal

@trace()
def upperCase(string):
    return string.upper()


print('---')
upperCase('I like Python')
print('---')

## EX 3
#

def times(n):
    def internal(fn):
        nonlocal n
        if n < 0:
            print(f'Warning: number is negative, using abs value ( {n} -> {abs(n)} )')
            n = abs(n)
        for run in range(n):
            fn()
    return internal

@times(-4)
def hello():
    print('hello')

## EX 4
#

def save(file,append=False):
    '''Decorator for saving data to file
       Example:


       @save(file='proc.out')
       def proc(a,b):
         return a + b

       proc(1,2) # This line will create 'proc.out' with content like this:

       --- proc.out ---
       function: proc
       timestamp: 1223445566
       ===== data =====
       3
       == end of data ==

       ----------------

       If a decorated function does not return any data ( Nonetype ), exception occurs
    '''
    def internal(fn):
        def subinternal(*args):
            ret = fn(*args)

            if not ret:
                raise TypeError('save: no return value from a function')

            mode = 'a' if append else 'w'

            with open(file,mode) as out:
                out.write(f'function: {fn.__name__}\n')
                out.write(f'timestamp: {int(time.time())}\n')
                out.write('===== data =====\n')
                out.write(f'{ret}\n')
                out.write('== end of data ==\n')
            return ret
        return subinternal
    return internal

@save(file='add.out', append=True)
def add(a,b):
    return a + b

add(8,8)


## EX 5
#

def compareWith(refcode,exception=False):
    '''This decorator runs a decorated function and compares
       its return code with 'refcode' return code.

       'refcode' must be callable 

       If comparison fails and 'exception' is True, ValueError will be raised.

       Example:

       @compareWith(lambda a,b: a + b)
       def add(a,b):
          return a + b
      
       add(1,2)

    '''

    if not callable(refcode):
        raise TypeError('refcode is not callable')

    def internal(fn):
        def subinternal(*args):
            ret = fn(*args)
            refret = refcode(*args)
            msg = ''

            if ret != refret:
                msg = f'compareWith failed: {fn.__name__}({args}) = {ret} != {refcode.__name__}({args}) = {refret}'
                print(msg,file=sys.stderr)
                if exception: 
                    raise ValueError(msg)

        return subinternal
    return internal

def add(a,b):
    return a + b

@compareWith(add, exception=True)
def testAdd(a,b):
    return a - b


testAdd(1,1)

## EX 6
#

class MatchError(Exception):
    '''Custom exception class'''
    def __init__(self,message):
        super().__init__(message)


def compareWithAll(codelist,method='anyMatch'):
    '''This decorator compares decorated method's result with results from 'codelist'
       functions following 'method' policy

       Supported methods are:

       'anyMatch'(default) - if there is a match, stop comparisons ( like short-circuit boolean expressions )
       'allMatch' - all 'codelist' methods must return the same result as a decorated function

       Example:
       

        def test1(a,b):
            return a + b

        def test2(a,b):
            return a - b

        @compareWithAll((test1,test2))
        def add(a,b):
          return a + b

        add(1,2)        # method = 'anyMatch', test1(1,2) == add(1,2), OK


        @compareWithAll((test1,test2),allMatch)
        def add(a,b):
          return a + b

        add(1,2)       # method = 'allMatch', test1(1,2) == add(1,2) => OK, but test2(1,2) != add(1,2) => FAIL and expection

    '''
    if not isinstance(codelist,tuple):
        raise TypeError('compareWithAll: invalid first parameter type')

    for code in codelist:
        if not callable(code):
            raise TypeError('compareWithAll: codelist element is not callable')

    if method not in ('anyMatch','allMatch'):
        raise ValueError(f'Invalid match policy: {method}')

    def internal(fn):
        def subinternal(*args):
            ret = fn(*args)
            status = False
            checkid = -1 
            for code in codelist:
                checkid += 1
                checkret = code(*args)
                if checkret == ret:
                    if method == 'anyMatch':
                        return ret
                else:
                    status = False
                    raise MatchError(f'compareWithAll: match failed at level {checkid}: expected {ret}, got {checkret}') 
        return subinternal
    return internal

@compareWithAll((lambda a,b:a+b,lambda a,b:a-b), 'allMatch')
def add(a,b):
    return a + b

add(1,8)
