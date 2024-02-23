num_store, num_target = map(int, input().split())
dict = {}

for _ in range(num_store):
    site, pw = input().split()
    dict[site] = pw

for _ in range(num_target):
    target = input()
    print(dict[target])