from .arquivo_de_midia import ArquivoDeMidia

class Playlist:
    def __init__(self, nome, usuario):
        self.nome = nome
        self.usuario = usuario
        self.itens = []
        self.reproducoes = 0     

    def adicionar_midia(self, midia: ArquivoDeMidia):
        self.itens.append(midia)

    def remover_midia(self, midia: ArquivoDeMidia):
        self.itens.remove(midia)

    def reproduzir(self):
        print(f"Reproduzindo a playlist {self.nome} do usuário {self.usuario.nome}:")
        self.reproducoes += 1
        for midia in self.itens:
            midia.reproduzir()
        print(f"A playlist {self.nome} acabou de ser reproduzida.")
        
    def __add__(self, other): #concatena duas playlists para criar uma terceira.
        if not isinstance(other, Playlist): 
            raise NotImplementedError #só é possível concatenar com outra playlist
        
        if other is self:
            raise ValueError #não é possível concatenar a mesma playlist
        nova_playlist = Playlist(self.nome, self.usuario)
        nova_playlist.itens = list(self.itens) + list(other.itens)
        nova_playlist.reproducoes = self.reproducoes + other.reproducoes
        return nova_playlist

    def __len__(self):
        return len(self.itens)

    def __getitem__(self, index):
        return self.itens[index]

    def __eq__(self, other):
        if not isinstance(other, Playlist):
            return NotImplementedError #só é possível comparar com outra playlist
        (self.nome == other.nome and self.usario == other.usuario and self.itens == other.itens)
    
    def __str__(self):
        return f"A playlist {self.nome} foi criada pelo(a) {self.usuario.nome} , possui {len(self.itens)} mídias e o número de reproduções foi {self.reproducoes}."

    def __repr__(self):
        return f"Playlist(nome='{self.nome}', usuario='{self.usuario.nome}')"
