from playsound import playsound as ps

m = input('Digite o nome do arquivo .mp3: ')
print('Reproduzindo {}.mp3'.format(m))
ps(m + '.mp3')
