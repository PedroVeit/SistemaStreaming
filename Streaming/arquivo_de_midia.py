from abc import ABC, abstractmethod

class ArquivoDeMidia:
    @abstractmethod
    def __init__(self, titulo, duracao, artista):
        self.titulo = titulo
        self.duracao = duracao
        self.artista = artista
        self.reproducoes = 0 #contador de quantas vezes a midia foi reproduzida

    def reproduzir(self): #exibe as informações da mídia e incrementa o contador de reproduções
        print(f"Título: {self.titulo} ; Artista: {self.artista} ; Duração: {self.duracao} segundos ;") 
        self.reproducoes += 1
    
    def __eq__(self, outro): #verifica se duas mídias são iguais pelo título e artista
        if not isinstance(outro, ArquivoDeMidia):
            raise NotImplementedError
        else:
            return self.titulo == outro.titulo and self.artista == outro.artista

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass