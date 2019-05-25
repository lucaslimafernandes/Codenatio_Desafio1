carac = 'abcdefghijklmnopqrstuvwxyz'
chave = 26 + 2

s1 = ('c okurncegf fgekocn rqkpv yknn cnycau gpf wr yjgtg kv yknn fq vjg itgcvguv fcocig. wpmpqyp')
conv = ''
#def decriptar(s1):
def descript(cifrado, numero_casas):
    for c in cifrado:
        if c in carac:
            num = carac.find(c)
            num2 = num + 26 + numero_casas
            if num2 >= len(carac):
                num2 -= len(carac)
            elif num2 < 0:
                num2 += len(carac)
                conv += carac[num2]
        else:
            conv += c
