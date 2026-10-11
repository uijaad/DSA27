"""Lab 01 — The interpreter, numbers, strings and lists.

Lab manual: docs/labs/lab01-python-basics.md
Tests:      tests/test_lab01.py

    pytest tests/test_lab01.py -v

Every function below raises `NotImplementedError`. Replace that line with
your own code. The docstring is the contract: it says what goes in, what comes
out, and gives examples you can try in the interpreter.

Use only what Lab 01 teaches: arithmetic, strings, slicing, lists, `while`,
and a first `if`. Do not import anything.
"""

# -- numbers ----------------------------------------------------------------


def seconds_to_hms(seconds):
    """Format a non-negative number of seconds as "H:MM:SS".

    seconds_to_hms(59)     -> "0:00:59"
    seconds_to_hms(3725)   -> "1:02:05"
    seconds_to_hms(86400)  -> "24:00:00"

    Hours are not padded; minutes and seconds are always two digits.
    Hint: `//` and `%`, then an f-string with `:02d`.
    """
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h}:{m:02d}:{s:02d}"

print(seconds_to_hms(3725))
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit, rounded to one decimal place.

    F = C * 9 / 5 + 32

    celsius_to_fahrenheit(100)   -> 212.0
    celsius_to_fahrenheit(-40)   -> -40.0
    celsius_to_fahrenheit(36.6)  -> 97.9
    """
    fahrenheit = celsius * 9 / 5 + 32
    return round(fahrenheit, 1)

print(celsius_to_fahrenheit(36.6))
def split_evenly(total, people):
    """Share `total` piasters between `people` as evenly as whole numbers allow.

    Return a tuple (share, left_over).

    split_evenly(100, 3) -> (33, 1)
    split_evenly(90, 3)  -> (30, 0)
    split_evenly(5, 8)   -> (0, 5)
    """
    share = total // people
    left_over = total % people

    return share, left_over


print(split_evenly(100, 3))

# -- strings ----------------------------------------------------------------


def initials(full_name):
    """The upper-case initials of a name, each followed by a dot.

    initials("haitham el-ghareeb")       -> "H.E."
    initials("  Ada   King  Lovelace ")  -> "A.K.L."
    initials("")                         -> ""

    Extra spaces anywhere are ignored. Hint: `str.split()` with no argument.
    """
    words = full_name.split()
    initials = ""
    for word in words:
        initials += word[0].upper() + "."
    return initials

print(initials("haitham el-ghareeb"))
def is_palindrome_word(word):
    """True if `word` reads the same backwards, ignoring case and outer spaces.

    is_palindrome_word("Level")   -> True
    is_palindrome_word(" noon ")  -> True
    is_palindrome_word("python")  -> False
    is_palindrome_word("")        -> True

    Hint: one slice does the reversing.
    """
    for x in range(len(word) // 2):
        if word[x].lower() != word[-(x + 1)].lower():
            return False
    return True
print(is_palindrome_word("Level"))
def mask_email(email):
    """Hide the middle of the part before "@".

    Keep the first and last character of the name, replace everything between
    them with "*" (one star per hidden character). The domain is unchanged.
    Names of length 1 or 2 are returned unchanged.

    mask_email("haitham@example.com")  -> "h*****m@example.com"
    mask_email("ab@x.org")             -> "ab@x.org"

    Hint: `str.index("@")`, slicing, and `"*" * n`.
    """
    at_index = email.index("@")
    name = email[:at_index]
    domain = email[at_index:]

    if len(name) <= 2:
        return email

    masked_name = name[0] + "*" * (len(name) - 2) + name[-1]
    return masked_name + domain

print(mask_email("haitham@example.com"))
# -- lists ------------------------------------------------------------------


def middle(values):
    """The middle of a list, as a new list.

    One element if the length is odd, two if it is even, none if it is empty.

    middle([1, 2, 3])     -> [2]
    middle([1, 2, 3, 4])  -> [2, 3]
    middle([])            -> []

    One slice is enough — no `if` needed.
    """
    length = len(values)
    mid = length // 2

    if length == 0:
        return []
    elif length % 2 == 0:
        return values[mid - 1:mid + 1]
    else:
        return [values[mid]]

print(middle([1, 2, 3]))
print(middle([1, 2, 3, 4]))

def rotate_left(values, k):
    """A NEW list with the elements moved k places to the left.

    The original list must not change. k may be larger than the list.

    rotate_left([1, 2, 3, 4, 5], 2)  -> [3, 4, 5, 1, 2]
    rotate_left([1, 2, 3], 4)        -> [2, 3, 1]
    rotate_left([], 3)               -> []
    """
    n = len(values)
    if n == 0:
        return []
    k = k % n
    return values[k:] + values[:k]

print(rotate_left([1, 2, 3, 4, 5], 2))
def fib_list(n):
    """The first n Fibonacci numbers, starting 0, 1.

    fib_list(0) -> []
    fib_list(1) -> [0]
    fib_list(7) -> [0, 1, 1, 2, 3, 5, 8]

    Hint: the tutorial's `while` loop, with `a, b = b, a + b`.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fibs = [0, 1]
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

print(fib_list(7))
def collatz_steps(n):
    """How many steps the Collatz rule needs to take n (>= 1) down to 1.

    Rule: if n is even, halve it; otherwise replace it with 3n + 1.

    collatz_steps(1)  -> 0
    collatz_steps(6)  -> 8     6 3 10 5 16 8 4 2 1
    collatz_steps(27) -> 111
    """
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

print(collatz_steps(1))
print(collatz_steps(27))
