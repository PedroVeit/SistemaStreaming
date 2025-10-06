from abc import ABC, abstractmethod

class ArquivoDeMidia:
    @abstractmethod
    def __init__(self, titulo, duracao, artista):
        self.titulo = titulo
        self.duracao = duracao
        self.artista = artista
        self.reproducoes = 0

        #Novo: Sistema de curtidas
        #self.likes = 0

    def reproduzir(self):
        return "%s(titulo='%s', duracao=%d, artista='%s', reproducoes=%d)" % (
            self.__class__.__name__, self.titulo, self.duracao, self.artista, self.reproducoes
        )
    
    def __eq__(self, other):
        self.titulo == other.titulo and self.artista == other.artista

    #def __str__(self):
        #minutos = self.duracao // 60
        #segundos = self.duracao % 60
        #return "%s - %s (%02d:%02d)" % (self.titulo, self.artista, minutos, segundos)