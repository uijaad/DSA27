"""Lab 02 — Control flow, functions, errors and modules.

Lab manual: docs/labs/lab02-control-flow-functions.md
Tests:      tests/test_lab02.py

    pytest tests/test_lab02.py -v

Replace each `raise NotImplementedError` with your own code. When a docstring
says "raise ValueError", the tests check that you do — use
`raise ValueError("a message that says what was wrong")`.
"""

# -- decisions --------------------------------------------------------------


def classify_triangle(a, b, c):
    """Name the triangle with side lengths a, b, c.

    Return "equilateral" (three equal sides), "isosceles" (exactly two) or
    "scalene" (none).

    Raise ValueError if any side is not positive, or if the sides break the
    triangle inequality: each side must be strictly shorter than the sum of
    the other two.

    classify_triangle(3, 3, 3)  -> "equilateral"
    classify_triangle(3, 3, 5)  -> "isosceles"
    classify_triangle(3, 4, 5)  -> "scalene"
    classify_triangle(1, 2, 3)  -> ValueError   (1 + 2 is not > 3)
    """
    sides = (a, b, c)
    if any(side <= 0 for side in sides):
        raise ValueError("triangle sides must be positive")
    if any(side >= sum(sides) - side for side in sides):
        raise ValueError("triangle inequality violated")
    if a == b == c:
        return "equilateral"
    if a == b or a == c or b == c:
        return "isosceles"
    return "scalene"
    


def course_result(coursework, final, attendance):
    """Apply this course's pass rules to one student.

    coursework  marks out of 40
    final       marks out of 60
    attendance  percentage of sessions attended, 0 to 100

    Return, checking in this order:
        "barred"  if attendance is below 75       (محروم — no final exam)
        "fail"    if final is below 18            (under 30% of the final)
        "fail"    if coursework + final is below 60
        "pass"    otherwise

    Raise ValueError if any argument is outside its range.

    course_result(35, 25, 90)  -> "pass"
    course_result(38, 15, 100) -> "fail"     total 53, and final under 18
    course_result(40, 60, 70)  -> "barred"
    """
    if not 0 <= coursework <= 40:
        raise ValueError("coursework must be between 0 and 40")
    if not 0 <= final <= 60:
        raise ValueError("final must be between 0 and 60")
    if not 0 <= attendance <= 100:
        raise ValueError("attendance must be between 0 and 100")
    if attendance < 75:
        return "barred"
    if final < 18 or coursework + final < 60:
        return "fail"
    return "pass"


# -- loops ------------------------------------------------------------------


def fizzbuzz(n):
    """The FizzBuzz sequence from 1 to n, as a list of strings.

    Multiples of 3 -> "Fizz", of 5 -> "Buzz", of both -> "FizzBuzz",
    anything else -> the number itself as a string.

    fizzbuzz(5)  -> ["1", "2", "Fizz", "4", "Buzz"]
    fizzbuzz(0)  -> []
    """
    result = []
    for number in range(1, n + 1):
        if number % 15 == 0:
            result.append("FizzBuzz")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(number))
    return result


def is_prime(n):
    """True if n is a prime number.

    Numbers below 2 are not prime. It is enough to try divisors up to and
    including the square root of n — ask yourself why.

    is_prime(2) -> True ;  is_prime(9) -> False ;  is_prime(97) -> True
    """
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def primes_below(n):
    """Every prime p with 2 <= p < n, in increasing order.

    primes_below(10) -> [2, 3, 5, 7]
    primes_below(2)  -> []
    """
    return [number for number in range(2, n) if is_prime(number)]


def first_repeated(values):
    """The first element that equals an element before it, or None.

    "First" means the repeat that happens earliest in the list.

    first_repeated([3, 1, 4, 1, 5, 9, 5])  -> 1
    first_repeated([1, 2, 3])              -> None

    Use loops and `break` or an early `return`. (In Lab 03 you will do this
    again with a set, and it will be much faster.)
    """
    for index, value in enumerate(values):
        for previous in values[:index]:
            if value == previous:
                return value
    return None


def count_pairs(n):
    """How many times does the inner body run in this loop?

        for i in range(n):
            for j in range(i + 1, n):
                ...                       # <- count this

    count_pairs(0) -> 0 ;  count_pairs(4) -> 6 ;  count_pairs(10) -> 45

    First write it with the two loops and a counter. Then find a formula that
    gives the same answer without looping, and use that instead. Both pass —
    only one of them is O(1).
    """
    return n * (n - 1) // 2


def calculator(command):
    """Evaluate a tiny command language with a `match` statement.

    The command is words separated by spaces:

        "add A B"   -> A + B
        "mul A B"   -> A * B
        "neg A"     -> -A
        "sum A B C ..." (one or more numbers) -> their total

    A, B, C are integers written in decimal. Anything else raises ValueError.

    calculator("add 2 3")     -> 5
    calculator("neg 7")       -> -7
    calculator("sum 1 2 3 4") -> 10
    calculator("div 1 2")     -> ValueError
    """
    parts = command.split()
    if not parts:
        raise ValueError("command cannot be empty")
    operation, *arguments = parts
    try:
        numbers = [int(argument) for argument in arguments]
    except ValueError as error:
        raise ValueError("arguments must be integers") from error

    match operation, numbers:
        case "add", [a, b]:
            return a + b
        case "mul", [a, b]:
            return a * b
        case "neg", [a]:
            return -a
        case "sum", [*values] if values:
            return sum(values)
        case _:
            raise ValueError("invalid calculator command")


# -- functions --------------------------------------------------------------


def parse_int(text, default=None):
    """Convert text to an int; return `default` if it is not a valid integer.

    parse_int("42")        -> 42
    parse_int(" -7 ")      -> -7
    parse_int("4.5")       -> None
    parse_int("abc", 0)    -> 0

    Use try/except — do not test the characters yourself.
    """
    try:
        return int(text)
    except (TypeError, ValueError):
        return default


def stats(*numbers):
    """Return (smallest, largest, mean) of any number of arguments.

    stats(3, 1, 2)  -> (1, 3, 2.0)
    stats(5)        -> (5, 5, 5.0)
    stats()         -> ValueError

    Write the loop yourself — no min(), max() or sum().
    """
    if not numbers:
        raise ValueError("at least one number is required")
    smallest = largest = numbers[0]
    total = 0
    count = 0
    for number in numbers:
        if number < smallest:
            smallest = number
        if number > largest:
            largest = number
        total += number
        count += 1
    return smallest, largest, total / count


def append_to(item, target=None):
    """Append item to target and return target.

    If no list is given, start a NEW empty list every call.

    append_to(1)       -> [1]
    append_to(2)       -> [2]          not [1, 2]
    append_to(3, [0])  -> [0, 3]

    This is the mutable-default-argument trap from the manual. Do not write
    `target=[]`.
    """
    if target is None:
        target = []
    target.append(item)
    return target


def make_multiplier(k):
    """Return a FUNCTION that multiplies its argument by k.

    triple = make_multiplier(3)
    triple(5)  -> 15
    """
    def multiply(value):
        return value * k
    return multiply


def apply_n(f, x, n):
    """Apply f to x, n times: f(f(...f(x)...)).

    apply_n(lambda v: v * 2, 1, 10)  -> 1024
    apply_n(str.upper, "hi", 0)      -> "hi"
    """
    result = x
    for _ in range(n):
        result = f(result)
    return result
