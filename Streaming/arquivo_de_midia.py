class ArquivoDeMidia:
    def __init__(self, titulo, duracao, artista):
        self.titulo = str(titulo)
        self.duracao = int(duracao)
        self.artista = str(artista)
        self.reproducoes = 0

    def reproduzir(self):
        raise NotImplementedError

    def __eq__(self, other):
        raise NotImplementedError
    
    # raise NotImplementedError interrompe o programa, indicando que o método deve ser implementado em subclasses.
    
    def __repr__(self):
        return f"{self.__class__.__name__}(titulo={self.titulo!r}, duracao={self.duracao}, artista={self.artista!r}, reproducoes={self.reproducoes})"

    def __str__(self):
        minutos = self.duracao // 60
        segundos = self.duracao % 60
        return f"{self.titulo} - {self.artista} ({minutos:02d}:{segundos:02d})"