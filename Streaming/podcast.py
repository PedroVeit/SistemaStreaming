from .arquivo_de_midia import ArquivoDeMidia

class Podcast(ArquivoDeMidia):
    def __init__(self, titulo, duracao, artista, episodio, temporada, host):
        super().__init__(titulo, duracao, artista)
        self.episodio = episodio
        self.temporada = temporada
        self.host = host

    def reproduzir(self):
        self.reproducoes += 1
        print("Reproduzindo podcast: %s - Host: %s | Temporada: %s | Episódio: %s | Duração: %ds" % (
            self.titulo, self.host, self.temporada, self.episodio, self.duracao))

    def __eq__(self, other):
        if not isinstance(other, Podcast):
            return False
        return self.titulo == other.titulo and self.artista == other.artista

    def __repr__(self):
        return "Podcast(titulo='%s', duracao=%d, artista='%s', episodio='%s', temporada='%s', host='%s', reproducoes=%d)" % (
            self.titulo, self.duracao, self.artista, self.episodio, self.temporada, self.host, self.reproducoes
        )

    def __str__(self):
        return "%s - %s (Ep %s)" % (self.titulo, self.host, self.episodio)
