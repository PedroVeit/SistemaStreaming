from .arquivo_de_midia import ArquivoDeMidia

class Podcast(ArquivoDeMidia):
    def __init__(self, titulo: str, host: str, duracao: int, temporada: str, episodio: int):
        super().__init__(titulo, host, duracao)  # host é o artista da classe pai.
        self.temporada = temporada
        self.episodio = episodio
    
    def reproduzir(self):
        super().reproduzir()
        print(f"Ep. {self.episodio} (Temporada: {self.temporada})")

    def __str__(self):
        return f"Podcast: {self.titulo} ; Host: {self.artista} ; Duração: {self.duracao} segundos ; Temporada: {self.temporada} ; Episódio: {self.episodio} ;"

    def __repr__(self):
        return (f"Podcast(titulo='{self.titulo}', host='{self.artista}', duracao={self.duracao}, temporada='{self.temporada}', episodio={self.episodio})")