import urllib.request as ur

#lendo a url
f = ur.urlopen("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=d8a2c7d19ed638555dae59b9ef594f1dc5378e27")
s1 = f.read()

print(str(s1))

json = open('answer.json', 'wb')
json.write(s1)
json.close()

#TOKEN = d8a2c7d19ed638555dae59b9ef594f1dc5378e27








#GITHUB https://github.com/lucaslimafernandes/Codenation_Desafio1.git
