thislist = ["a", "b", "c",1,'w',76,'A','J','H','p',23,0]
intlist=[]
wordlist=[]
charlist=[]
count = 0

def var_type(t):
    tp = True
    if type(t) == str:
        tp = False
    return tp

#______________________ finction sort ____________________________________________
def sort ( c ):
    new_list = []
    while c:
        minimum = c[0]  # arbitrary number in list 
        for x in c: 
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        c.remove(minimum)  
    return new_list
#____________________check to int or str ______________________________________________
for a in thislist:
    tp_var = var_type(a)
    if tp_var == True:
         intlist.append(a)
    elif tp_var == False:
        if ord(a) < 97:
            count = count+1
        charlist.append(ord(a))

#________________________convert to scki code_____________________________________________

# for b in wordlist:
#     charlist.append( ord(b))

#_________________sort str________________________________________________________
# new_list = sort(charlist)
#___________________sort int_____________________________________________
# int_list = sort(intlist)
#__________convert  aski to char__________________________________________________________

def asc_to_char(asc_lst):
    return [chr(j) for j in asc_lst]

#___________ appent two list
chr_lst = asc_to_char(sort(charlist))
export_list = chr_lst[count:] + chr_lst[:count] + sort(intlist)
print(export_list)