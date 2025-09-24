def multiple(n):
    return lambda x : x * n

mul = multiple(2)
result = mul(3)
print(result)