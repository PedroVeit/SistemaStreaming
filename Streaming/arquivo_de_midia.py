class ArquivoDeMidia:
    def __init__(self, titulo, duracao, artista):
        self.titulo = titulo
        self.duracao = duracao
        self.artista = artista
        self.reproducoes = 0

        # INOVAÇÃO: Sistema de curtidas
        self.likes = 0

    def reproduzir(self): # simula a execução do arquivo de mídia, mostra na tela as informações contendo título, artista e duração.
        raise NotImplementedError

    def __eq__(self, other): # compara dois arquivos de mídia (mesmo título e artista)
        raise NotImplementedError
    
    # raise NotImplementedError obriga classes filhas a implementarem este método

    def __repr__(self):
        return "%s(titulo='%s', duracao=%d, artista='%s', reproducoes=%d)" % (
            self.__class__.__name__, self.titulo, self.duracao, self.artista, self.reproducoes
        )

    def __str__(self):
        minutos = self.duracao // 60
        segundos = self.duracao % 60
        return "%s - %s (%02d:%02d)" % (self.titulo, self.artista, minutos, segundos)