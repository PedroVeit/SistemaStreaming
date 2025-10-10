from Streaming.arquivo_de_midia import ArquivoDeMidia

class Musica(ArquivoDeMidia):
    def __init__(self, titulo, artista, duracao, genero: str): 
        super().__init__(titulo, artista, duracao)
        self.genero = genero
        self.avaliacoes = [ ] #lista para armazenar as avaliações da música]

    
    def avaliar(self, nota: int): #adiciona uma avaliação à lista de avaliações
        if 0 <= nota <= 5:
            self.avaliacoes.append(nota)
        else:
            raise ValueError ("A nota de avaliação deve ser entre 0 e 5.")

    def reproduzir(self):
        super().reproduzir()
    
    def __str__(self):
        return f"Música: {self.titulo} ; Artista: {self.artista} ; Duração: {self.duracao} segundos ; Gênero: {self.genero} ; Avaliações: {self.avaliacoes} ;"

    def __repr__(self):
        return (f"Musica(titulo='{self.titulo}', artista='{self.artista}', duracao={self.duracao}, genero='{self.genero}'")