
import urllib.request as ur
import hashlib
import json
import requests



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
h = hashlib.sha1()
h.update(decifrado.encode('utf-8'))
hash2 = (h.hexdigest())

resumo_criptografico = hash2

print(hash2)

#encodar json
texto = {

'numero_casas':numero_casas,
'token':token,
'cifrado':cifrado,
'decifrado': decifrado,
'resumo_criptografico':resumo_criptografico,
}
encodar_json = json.dumps(texto)

jsonfile2 = open('answer.json', 'w+')
jsonfile2.write(encodar_json)
jsonfile2.close()

#enviar arquivo
local_envio = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=d8a2c7d19ed638555dae59b9ef594f1dc5378e27'
jsonfile3 = {'answer': open('answer.json', 'rb')}
jsonfile4 = open('answer.json', 'r')
query_envio = requests.post(local_envio, files=jsonfile3)

print(jsonfile3)
print(query_envio.json)
print(query_envio.status_code)


#envio = ur.urlopen(local_envio, query_envio)
#envio2 = envio.read()
#envio.close()
#print(envio2)

#resposta =


#TOKEN = d8a2c7d19ed638555dae59b9ef594f1dc5378e27
#https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=d8a2c7d19ed638555dae59b9ef594f1dc5378e27







#GITHUB https://github.com/lucaslimafernandes/Codenation_Desafio1.git
