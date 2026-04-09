N, x = map(int, input().split())
arr = list(map(int, input().split()))
c = set(arr)

# Case 0: duplicates in input
if len(c) < N:
    print(0)

else:
    # Case 1: exists v & x that collapses into an existing different element
    for v in c:
        w = v & x
        if w != v and w in c:
            print(1)
            break
    else:
        # Case 2: AND with x reduces the number of distinct values
        cp = {v & x for v in c}
        if len(cp) < len(c):
            print(2)
        else:
            print(-1)

