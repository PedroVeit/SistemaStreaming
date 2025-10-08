from .arquivo_de_midia import ArquivoDeMidia


class Playlist:
      reproducoes = 0
    
    def __init__(self, nome: str, usuario, iens: list[ArquivoDeMidia]):
        self.nome = nome
        self.usuario = usuario
        self.itens = itens     

    def adicionar_midia(self, midia: ArquivoDeMidia):
        self.itens.append(midia)

    def remover_midia(self, midia: ArquivoDeMidia):
        self.itens.append(midia)

    def reproduzir(self):
        self.reproducoes += 1
        print('Músicas reproduzidas')
        for i in self.itens:
            print(i)
            i.reproducoes += 1

    def __add__(self, other):
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
        (self.nome == other.nome and self.usario == other.usuario and self.itens == other.itens)

