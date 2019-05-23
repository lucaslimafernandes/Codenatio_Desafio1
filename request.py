import urllib.request as ur

#lendo a url
f = ur.urlopen("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=d8a2c7d19ed638555dae59b9ef594f1dc5378e27")
s1 = f.read()

print(s1)


#TOKEN = d8a2c7d19ed638555dae59b9ef594f1dc5378e27








#GITHUB https://github.com/lucaslimafernandes/Codenation_Desafio1.git
