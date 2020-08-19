import random

def estrofe1():
	return verso()+ "<br>" + verso() + "<br>" + verso() + "<br>" + verso() + "<br> <br>"
	return """
		Amo-te tanto, meu amor... nao canto
		O humano coracao com mais verdade...
		Amo-te como amigo e como amante
		Numa sempre diversa realidade
	"""

def estrofe2():
	return verso()+ "<br>" + verso() + "<br>" + verso() + "<br>" + verso() + "<br> <br>"
	return """
		Amo-te afim, de um calmo amor prestante,
		E te amo alem, presente na saudade.
		Amo-te, enfim, com grande liberdade
		Dentro da eternidade e a cada instante.
	"""

def estrofe3():
	return verso()+ "<br>" + verso() + "<br>" + verso() + "<br> <br>"
	return """
		Amo-te como um bicho, simplesmente,
		De um amor sem misterio e sem virtude
		Com um desejo macico e permanente.
	"""

def estrofe4():
	return verso()+ "<br>" + verso() + "<br>" + verso() + "<br> <br>"
	return """
		E de te amar assim muito amiude,
		que um dia em teu corpo de repente
		Hei de morrer de amar mais do que pude.
	"""

def verboInfinitivo():
	lista = ["amar", "beijar", "ver", "viver", "contar", "dancar", "voar", "sonhar", "buscar"]
	return random.choice(lista)

def verboConjugado():
	lista = ["quero", "vou", "preciso", "desejo", "espero", "nasci para"]
	return random.choice(lista)

def substantivo():
	lista = ["pudim", 
			"aipim", 
			"ceu", 
			"no beleleu", 
			"pastel", 
			"irmao do jorel", 
			"doguinho", 
			"passarinho", 
			"carinho", 
			"baixinho"]
	return random.choice(lista)

def verso():
	return verboConjugado() + " " + verboInfinitivo() + " " + substantivo() + "\n"

def imprime():
	inicio = "<html> <head> </head> <body>"
	fim = "</body> </html>"
	print inicio, getSoneto(), fim

def getSoneto():
	return estrofe1(), "\n", estrofe2(), "\n", estrofe3(), "\n", estrofe4()

def getSonetoJson():
	return {'estrofe1': estrofe1(), 'estrofe2': estrofe2(), 'estrofe3': estrofe3(), 'estrofe4': estrofe4()}

