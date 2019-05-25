carac = 'abcdefghijklmnopqrstuvwxyz'
chave = 26 + 2

s1 = ('c okurncegf fgekocn rqkpv yknn cnycau gpf wr yjgtg kv yknn fq vjg itgcvguv fcocig. wpmpqyp')
conv = ''
#def decriptar(s1):

for c in s1:
    if c in carac:
        num = carac.find(c)
        num2 = num - chave
        if num2 >= len(carac):
            num2 -= len(carac)
        elif num2 < 0:
            num2 += len(carac)
            conv += carac[num2]
    else:
        conv += c
print(conv)
