# Moshe Shahar - 211692165
# Yehonatan Klein - 322961764

def getPentaNum(n: int) -> int:
    return n * (3 * n - 1) // 2


def pentaNumRange(n1: int, n2: int) -> set:
    return set(getPentaNum(i) for i in range(n1, n2))


def sumDigits(n: int) -> int:
    return sum([int(i) for i in str(n)])


def gematriaValue(word: str) -> int:
    gematria = {
        'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
        'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90,
        'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400, 'ך': 20, 'ם': 40, 'ן': 50, 'ף': 80, 'ץ': 90
    }
    return sum([gematria[letter] for letter in word])


def isPrime(n: int) -> bool:
    if n < 2:
        return False
    dividers = set(i for i in range(2, int(n ** 0.5 + 1)) if n % i == 0)
    return not dividers


def getTwinPrimes(n: int) -> tuple:
    return tuple(i for i in range(n - 2, n + 3, 4) if isPrime(i))


def getPrimesInRange(n: int) -> dict:
    return {i: getTwinPrimes(i) for i in range(2, n) if isPrime(i)}


def add3dicts(d1: dict, d2: dict, d3: dict) -> dict:
    return {k: tuple(set(i[k] for i in (d1, d2, d3))) for k in set(d1.keys()) & set(d2.keys()) & set(d3.keys())}


def square(x: float) -> float:
    return x ** 2

def multiplyBy2(x: float) -> float:
    return x * 2

def inverse(x: float) -> float:
    return 1 / x


funcs = [square, multiplyBy2, inverse]

def applyFuncs(funcs: list, nums: set) -> dict[str, list]:
    return {f.__name__: list(f(n) for n in nums) for f in funcs}


def main():
    # Test getPentaNum
    assert getPentaNum(1) == 1, f"Expected: 1, Got: {getPentaNum(1)}"
    assert getPentaNum(2) == 5, f"Expected: 5, Got: {getPentaNum(2)}"
    assert getPentaNum(3) == 12, f"Expected: 12, Got: {getPentaNum(3)}"

    # Test pentaNumRange
    assert pentaNumRange(1, 4) == {1, 5, 12}, f"Expected: {{1, 5, 12}}, Got: {pentaNumRange(1, 4)}"
    assert pentaNumRange(3, 6) == {12, 22, 35}, f"Expected: {{12, 22, 35}}, Got: {pentaNumRange(3, 6)}"

    # Test sumDigits
    assert sumDigits(123) == 6, f"Expected: 6, Got: {sumDigits(123)}"
    assert sumDigits(4567) == 22, f"Expected: 22, Got: {sumDigits(4567)}"

    # Test gematriaValue
    assert gematriaValue('אבג') == 6, f"Expected: 6, Got: {gematriaValue('אבג')}"
    assert gematriaValue('שלום') == 376, f"Expected: 376, Got: {gematriaValue('שלום')}"

    # Test isPrime
    assert isPrime(2) == True, f"Expected: True, Got: {isPrime(2)}"
    assert isPrime(4) == False, f"Expected: False, Got: {isPrime(4)}"

    # Test getTwinPrimes
    assert getTwinPrimes(5) == (3, 7), f"Expected: (3, 7), Got: {getTwinPrimes(5)}"
    assert getTwinPrimes(11) == (13,), f"Expected: (13,), Got: {getTwinPrimes(11)}"

    # Test getPrimesInRange
    expected_primes_range_10 = {
        2: (),
        3: (5,),
        5: (3, 7),
        7: (5,)
    }
    assert getPrimesInRange(
        10) == expected_primes_range_10, f"Expected: {expected_primes_range_10}, Got: {getPrimesInRange(10)}"

    # Test add3dicts
    d1 = {'a': 1, 'b': 2}
    d2 = {'a': 3, 'b': 2}
    d3 = {'a': 1, 'b': 4}
    expected_add3dicts = {'a': (1, 3), 'b': (2, 4)}
    assert add3dicts(d1, d2, d3) == expected_add3dicts, f"Expected: {expected_add3dicts}, Got: {add3dicts(d1, d2, d3)}"

    # Test applyFuncs
    nums = {1, 2, 4}
    expected_applyFuncs = {
        'square': [1, 4, 16],
        'multiplyBy2': [2, 4, 8],
        'inverse': [1.0, 0.5, 0.25]
    }
    assert applyFuncs(funcs,
                      nums) == expected_applyFuncs, f"Expected: {expected_applyFuncs}, Got: {applyFuncs(funcs, nums)}"

    print("All tests passed!")


if __name__ == '__main__':
    main()
