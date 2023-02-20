import decimal
import requests
a = decimal.Decimal('0.01')
b = decimal.Decimal("0.02")
if a + b == 0.03:
    print("精度正确")
    print(a + b)
elif a + b == decimal.Decimal('0.03'):
    print("精度不正常")
    print(decimal.Decimal('0.03'))
