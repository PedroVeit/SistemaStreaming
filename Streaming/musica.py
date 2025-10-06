from .arquivo_de_midia import ArquivoDeMidia
from .log import log_error


class Musica(ArquivoDeMidia):
    def _init_(self, titulo, duracao, artista, genero):
        super()._init_(titulo, duracao, artista)
        self.genero = genero
        self.avaliacoes = []

    def avaliar(self, nota):
        if not isinstance(nota, int) or nota < 0 or nota > 5:
            log_error("Avaliação inválida (nota fora do intervalo 0-5)", context={"titulo": self.titulo, "artista": self.artista, "nota": nota})
            return
        self.avaliacoes.append(nota)

    def reproduzir(self):
        self.reproducoes += 1
        print("Tocando música: %s - %s | Gênero: %s | Duração: %ds" % (self.titulo, self.artista, self.genero, self.duracao))

    def _eq_(self, other):
        if not isinstance(other, Musica):
            return False
        return self.titulo == other.titulo and self.artista == other.artista

    def _repr_(self):
        return "Musica(titulo='%s', duracao=%d, artista='%s', genero='%s', reproducoes=%d, avaliacoes=%s)" % (
            self.titulo, self.duracao, self.artista, self.genero, self.reproducoes, self.avaliacoes
        )

    def _str_(self):
        return "%s - %s (%s)" % (self.titulo, self.artista, self.genero)
