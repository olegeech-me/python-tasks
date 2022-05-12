from functools import wraps
import time


#
# 1. Decorator 'trace'


def trace(msg=""):
    """
    Decorator that prints out function name, number
    of parameters and how long it took to run
    Accepts key msg, when set to "TRACE" it will
    print all the extra information
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            if msg == "TRACE":
                print(f"{func.__name__} was called with {len(args)} args")
                print(f"{func.__name__} was called with {args}")
            start = time.time()
            result = func(*args)
            end = time.time()
            if msg == "TRACE":
                print(f"{func.__name__} took {end - start} seconds")
            return result

        return wrapper

    return decorator


@trace(msg="TRACE")
def upperCase(string):
    time.sleep(0.1)
    return string.upper()


print(upperCase("Hey there!"))

#
# 2. Decorator 'times'


def times(N):
    """
    Decorator which runs decorated function N-times
    """
    if N < 0:
        raise ValueError("Decorator accepts only non-negative value")

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            for i in range(N):
                fn(*args, **kwargs)

        return wrapper

    return decorator


@times(2)
def hello(name):
    print("Hello,", name)


hello("John")

#
# 3. Decorator 'save'


def save(file="", append=False):
    """
    Decorator that saves out from the decorated
    function to a file
    """

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            output = fn(*args, **kwargs)
            if not output:
                raise TypeError(f"Function {fn.__name__} returns nothing")
            output_file = file if file else f"{fn.__name__}.out"
            with open(output_file, "a" if append else "w") as f:
                f.write(str(output))
            print("Output saved to the file", output_file)
            return output

        return wrapper

    return decorator


@save(file="my_add.out", append=True)
def add(a, b):
    return a + b


add(4, 9)

#
# 4. Decorator 'compareWith'


def compareWith(referenceFn, exception=False):
    """
    Decorator for comparing a decorated function's
    result with a reference function' one
    """

    if not callable(referenceFn):
        raise TypeError("Reference function is not callable")

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            reference_result = referenceFn(*args, **kwargs)
            if result != reference_result:
                message = "Output of the function doesn't match with the reference"
                print(message)
                if exception:
                    raise ValueError(message)
            return result

        return wrapper

    return decorator


def compute1(a, b):
    return a + b


@compareWith(compute1, exception=True)
def add(a, b):
    return a + b


add(1, 2)  # OK, add(1,2) == compute1(1,2)


def compute2(a, b):
    return a - b


@compareWith(compute2, exception=False)
def add(a, b):
    return a + b


add(1, 2)  # !! ValueError !!, add(1,2) != compute2(1,2)

#
# 5. Decorator 'compareWithAll'


def compareWithAll(referenceFns, method):
    """
    Decorator that compares decorated function's result with
    the results of reference functions, that are given in a tuple.
    Decorator has two parameters:
      referenceFns: reference functions (tuple)
      method: match type (str), where
        'anyMatch' - at least one match is required
        'allMatch' - all reference functions must give the same result

    Return MatchError exception if results are different
    """

    class MatchError(Exception):
        """Raised when results do not match"""

        pass

    if not isinstance(referenceFns, tuple):
        raise TypeError("ReferenceFns must be a tuple")

    for f in referenceFns:
        if not callable(f):
            raise TypeError("Reference function is not callable")

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            result = fn(*args, **kwargs)
            referenceResults = [f(*args, **kwargs) for f in referenceFns]
            if method == "anyMatch":
                if result not in referenceResults:
                    raise MatchError(
                        f"Result of the function {fn.__name__} ({result}) "
                        + f"doesn't match with any of references {[r for r in referenceResults]}"
                    )
            elif method == "allMatch":
                if not all(result == r for r in referenceResults):
                    raise MatchError(
                        f"Result of the function {fn.__name__} ({result}) "
                        + f"doesn't match with all references {[r for r in referenceResults]}"
                    )
            else:
                raise ValueError("Invalid method parameter")
            return result

        return wrapper

    return decorator


@compareWithAll((lambda a, b: a * b, lambda a, b: a - b), method="anyMatch")
def add(x, y):
    return x + y


add(1, 2)  # OK, matches first lambda ( 'anyMatch' )


@compareWithAll((lambda a, b: a + b, lambda a, b: a - b), method="allMatch")
def add(x, y):
    return x + y


add(1, 2)  # MatcheError, second lambda's result is different ( 'allMatch' )
