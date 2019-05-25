import urllib.request as ur
import json

#lendo a url
f = ur.urlopen("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=d8a2c7d19ed638555dae59b9ef594f1dc5378e27")
s1 = f.read()

#print(str(s1))

#salvando answer.json
jsonfile = open('answer.json', 'wb')
jsonfile.write(s1)
jsonfile.close()


#lendo o arquivo json em python

ler_json = json.loads(s1)
numero_casas = int(ler_json['numero_casas'])
token = ler_json['token']
cifrado = ler_json['cifrado']
decifrado = ler_json['decifrado']
resumo_criptografico = ler_json['resumo_criptografico']

#Parte funcional de decifrar
carac = 'abcdefghijklmnopqrstuvwxyz'
conv = ''
for c in cifrado:
    if c in carac:
        num = carac.find(c)
        num2 = num - (26 + numero_casas)
        if num2 >= len(carac):
            num2 -= len(carac)
        elif num2 < 0:
            num2 += len(carac)
            conv += carac[num2]
    else:
        conv += c
decifrado = conv

print(decifrado)

#encodar json
texto = {

'numero_casas':numero_casas,
'token':token,
'cifrado':cifrado,
'decifrado': decifrado,
'resumo_criptografico':resumo_criptografico,
}
encodar_json = json.dumps(texto)

jsonfile2 = open('answer2.json', 'w+')
jsonfile2.write(encodar_json)
jsonfile2.close()



#print(ler_json["numero_casas"])




#TOKEN = d8a2c7d19ed638555dae59b9ef594f1dc5378e27








#GITHUB https://github.com/lucaslimafernandes/Codenation_Desafio1.git
