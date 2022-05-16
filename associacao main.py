from associacao import Escritor, Caneta, MaquinaEscrever


escritor = Escritor('qwerty')
caneta = Caneta('Bic')
maquina = MaquinaEscrever()


print(escritor.nome)
print(caneta.marca)

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

