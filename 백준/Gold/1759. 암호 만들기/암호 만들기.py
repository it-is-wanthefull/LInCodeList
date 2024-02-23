def pick(picks, lst, L):
    if len(picks) == L:
        cnt = sum(1 for char in picks if char in 'aeiou')

        if 1 <= cnt <= L-2:
            print(''.join(picks))

    for e in lst:
        if not picks or e > picks[-1]: #비어있는 즉 첫선택이면 조건없이 뽑고, 2번째이상이면 이전 알파벳보다 뒷알파벳
            pick(picks+[e], lst, L)

#----- ----- ----- ----- ----- ----- ----- ----- ----- -----

L, C = map(int, input().split())
lst = input().split()
lst.sort()

pick([], lst, L)