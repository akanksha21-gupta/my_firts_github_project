
def productDigits(A, B):
    # WRITE YOUR LOGIC HERE
    product = A * B
    return len(str(product))


# Driver code for the test environment
A, B = map(int, input().split())
result = productDigits(A, B)
print(result)
