from decimal import Decimal

while True:
    a = input('Number: ').replace('0.', '')
    b = Decimal('0')
    for i, c in zip(a, range(-1, -1 - len(a), -1)):
        b += Decimal(str(i)) * Decimal('2') ** Decimal(str(c))
    print(b)