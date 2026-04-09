def distributeCandies(T, N):
    result = []

    for candies in N:
        max_children = 0

        # Try number of children from large to small
        for c in range(1, int((2 * candies) ** 0.5) + 2):
            numerator = 2 * candies - c * (c - 1)
            if numerator <= 0:
                continue

            if numerator % (2 * c) == 0:
                a = numerator // (2 * c)
                if a >= 1:
                    max_children = c

        result.append(max_children)

    return result


# INPUT
T = int(input())
N = []
for _ in range(T):
    N.append(int(input()))

# OUTPUT
res = distributeCandies(T, N)
for r in res:
    print(r)