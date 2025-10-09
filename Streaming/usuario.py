from Streaming.arquivo_de_midia import ArquivoDeMidia
from Streaming.playlist import Playlist
from Streaming.musica import Musica
from Streaming.podcast import Podcast

class Usuario:
    qntd_instancias = 0 #contador de instâncias da classe

    def __init__(self, nome): #construtor
        self.nome = nome
        self.playlists = []
        self.historico = []
        Usuario.qntd_instancias += 1

    def ouvir_midia(self, midia): #adiciona a mídia ao histórico e reproduz
        self.historico.append(midia)
        midia.reproduzir()

    def criar_playlist(self, nome): #cria uma nova playlist e a adiciona à lista de playlists do usuário
        nova_playlist = Playlist(nome, self)
        self.playlists.append(nova_playlist)
        return nova_playlist
    
    def __repr__(self):
        return f"Usuario(nome='{self.nome}' , playlists={len(self.playlists)}, historico={len(self.historico)})"

    def __str__(self):
        return f"Usuário: {self.usuario} ; Playlists: {len(self.playlists)} ; Histórico de reprodução: {len(self.historico)} ;"
