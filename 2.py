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

def rt_ch(lst):
    sorted_l = srt(lst)
    return [chr(x) for x in sorted_l]


lst = [16,32,'A','b',20,12,1,2,'C','l','P','K','n','N','F',29]
char_lst = []
cnt_bs = 0
for x in lst:
    if type(x) == str:
        char_lst.append(ord(x))
    if type(x) == str and ord(x) < 97:
        cnt_bs+=1
lst = srt([x for x in lst if type(x) == int])

print(rt_ch(char_lst)[cnt_bs:]+rt_ch(char_lst)[:cnt_bs]+lst)