from .arquivo_de_midia import ArquivoDeMidia

class Podcast(ArquivoDeMidia):
    reproducoes = 0

    def __init__(self, titulo, duracao, artista, episodio: int, temporada: str, host: str):
        super().__init__(titulo, duracao, artista)
        self.episodio = episodio
        self.temporada = temporada
        self.host = host