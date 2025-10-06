from .arquivo_de_midia import ArquivoDeMidia


class Playlist:
    def __init__(self, nome, usuario):
        self.nome = nome
        self.usuario = usuario
        self.itens = []
        self.reproducoes = 0

    def adicionar_midia(self, midia):
        self.itens.append(midia)

    def remover_midia(self, midia):
        try:
            self.itens.remove(midia)
        except ValueError:
            pass

    def reproduzir(self):
        self.reproducoes += 1

        for midia in self.itens:
            midia.reproduzir()

    def __add__(self, other):
        #if not isinstance(other, Playlist):
            #return ValueError
        
        nova = Playlist(self.nome, self.usuario)
        nova.itens = list(self.itens) + list(other.itens)
        nova.reproducoes = self.reproducoes + other.reproducoes
        return nova

    def __len__(self):
        return len(self.itens)

    def __getitem__(self, index):
        return self.itens[index]

    def __eq__(self, other):
        if not isinstance(other, Playlist):
            return False
        
        mesmos = [m.titulo for m in self.itens] == [m.titulo for m in other.itens]
        return self.nome == other.nome and self.usuario == other.usuario and mesmos

    #def __repr__(self):
        #return "Playlist(nome='%s', usuario=%s, itens=%d, reproducoes=%d)" % (
            #self.nome, self.usuario, len(self.itens), self.reproducoes
        #)

    #def __str__(self):
        #return "Playlist '%s' por %s (%d itens)" % (self.nome, self.usuario.nome, len(self))
