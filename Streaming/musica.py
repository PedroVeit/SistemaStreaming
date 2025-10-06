from Streaming.arquivo_de_midia import ArquivoDeMidia

class Musica(ArquivoDeMidia):
    reproducoes = 0

    def _init_(self, titulo, duracao, artista, genero: str, avaliacoes: list[int] = None):
        super()._init_(titulo, duracao, artista) #herdou de ArquivoDeMidia
        self.genero = genero
        self.avaliacoes = avaliacoes #if avaliacoes is not None else []

    
    def avaliar(self, nota: int):
        if 0 <= nota <= 5:
            self.avaliacoes.append(nota)
        else:
            raise ValueError ("A nota de avaliação deve ser entre 0 e 5.")

    
    def reproduzir(self):
        Musica.reproducoes += 1