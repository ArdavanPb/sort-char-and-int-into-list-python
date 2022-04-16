def srt(lst):
    ln = len(lst)
    ch = int()
    fl = False
    for x in range(ln-1):
        k = lst[x]
        for t in range(x+1,ln):
            if lst[t] < k:
                k = lst[t]
                ch = t
                fl = True
        if fl == True:
            tm = lst[x]
            lst[x] = k
            lst[ch] = tm
            fl = False
    return lst



lst = [16,32,'A','b',20,12,1,2,'C','l','P','K','n','N','F',29]

n_lst = [x for x in lst if type(x) == int]
b_lst = []
s_lst = []

for c in lst:
    if type(c) == str and ord(c) < 97:
        b_lst.append(ord(c))
    elif type(c) == str and ord(c) > 97:
        s_lst.append(ord(c))

print([chr(x) for x in srt(s_lst)]+[chr(x) for x in srt(b_lst)]+srt(n_lst))