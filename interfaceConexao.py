class interface:
	"""docstring for """

	lista = []

	def __init__(self):
		pass

	def getListaDeNomes(self):
		arq = open('nomes.txt','r')

		for i in arq:
			self.lista.append(i)

		arq.close()

	def exibirNomes(self):
		listaNomes = ''

		if len(self.lista) == 0:
			self.getListaDeNomes()

		novaLista = sorted(self.lista, reverse=True)

		for i in novaLista:
			listaNomes += '{}\n'.format(i)

		return listaNomes

	def setNome(self,nome):

	 	arq = open('nomeTemp.txt','w')
                #arq.write('Pontos:{} Nome:{}\n'.format(pontos,nome))
	 	arq.write(nome)
	 	arq.close()

	def setRanking(self,nome,pontos):
                arq = open('nomes.txt','a')
                arq.write('Pontos:{} Nome:{}\n'.format(pontos,nome))
                arq.close()
                
	def verificaNome(self, nome):
		status = False

		arq = open('nomes.txt','r')

		for i in arq:
			if nome in i:
				status = True
				break

		arq.close()
		return status
