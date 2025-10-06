from Streaming.arquivo_de_midia import ArquivoDeMidia
from Streaming.playlist import Playlist
from Streaming.musica import Musica
from Streaming.podcast import Podcast


class Usuario:
    qntd_instancias = 0

    def __init__(self, nome):
        self.nome = nome
        self.playlists = []
        self.historico = []
        #Novo: Sistema de favoritos
        #self.favoritos = []
        Usuario.qntd_instancias += 1

    def ouvir_midia(self, midia):
        self.historico.append(midia)
        midia.reproduzir()

    def criar_playlist(self, nome):
        nova = Playlist(nome, self)
        self.playlists.append(nova)
        return nova
    
    #def __repr__(self):
        #return "Usuario(nome='%s', playlists=%d, historico=%d)" % (
            #self.nome, len(self.playlists), len(self.historico)
        #)

    #def __str__(self):
        #return self.nome

    #def __eq__(self, other):
        #return isinstance(other, Usuario) and self.nome == other.nome
    
    """
    # INOVAÇÃO: Métodos do sistema de favoritos
    def curtir_midia(self, midia):
        """Curtir uma mídia e adicionar aos favoritos se não estiver."""
        if midia not in self.favoritos:
            self.favoritos.append(midia)
        midia.likes += 1
        print("Curtiu: %s" % midia.titulo)

    def descurtir_midia(self, midia):
        """Descurtir uma mídia e remover dos favoritos."""
        if midia in self.favoritos:
            self.favoritos.remove(midia)
        if midia.likes > 0:
            midia.likes -= 1
        print("Descurtiu: %s" % midia.titulo)

    def listar_favoritos(self):
        """Lista os favoritos do usuário."""
        if not self.favoritos:
            print("Nenhum favorito ainda.")
            return
        print("\nSeus favoritos:")
        for i, midia in enumerate(self.favoritos, 1):
            print("%d. %s - %s (likes: %d)" % (i, midia.titulo, midia.artista, midia.likes))
"""