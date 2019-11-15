class interface:
	"""docstring for """

	lista = []

	def __init__(self):
		pass

	def getListaDeNomes(self):
		#ler arquivos do arquivo de nomes e salva na lista
		arq = open('nomes.txt','r')

		for i in arq:
			self.lista.append(i)

		arq.close()

	def exibirNomes(self):
		#retorna uma string para ser exibida numa massegebox
		listaNomes = ''

		#limpa a lista e adicionar o ranking atualizado
		self.lista.clear()
		self.getListaDeNomes()

		#ordena a lista de forma descrescente
		novaLista = sorted(self.lista, reverse=True)

		for pos,i in enumerate(novaLista):
			if pos < 11:
				listaNomes += '{}\n'.format(i)

		return listaNomes

	def setNome(self,nome):
		#armazena um nome temporario para ser utilizado por jogoMiInterface
	 	arq = open('nomeTemp.txt','w')
	 	arq.write(nome)
	 	arq.close()

	def setRanking(self,nome,pontos):
		#adicionando os pontos de um novo usuario
		arq = open('nomes.txt','a')
		arq.write('{} {}\n'.format(pontos,nome))
		arq.close()
                
	def verificaNome(self, nome):
		#verifica se o nome existe, caso contrário salva
		status = False

		arq = open('nomes.txt','r')

		for i in arq:
			if nome in i:
				status = True
				break

		arq.close()
		return status

	def verificaPlayerTop(self):
		#retorna o player top 1
		self.exibirNomes()
		return self.lista[0]
		
