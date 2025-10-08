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
        Usuario.qntd_instancias += 1

    def ouvir_midia(self, midia):
        self.historico.append(midia)
        midia.reproduzir()

    def criar_playlist(self, nome):
        nova = Playlist(nome, self)
        self.playlists.append(nova)
        return nova
