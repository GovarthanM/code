def plus_one(digits):
    for i in reversed(range(len(digits))):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits

digits = [1, 2, 3]
print(plus_one(digits))