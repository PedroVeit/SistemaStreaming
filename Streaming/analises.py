from Streaming.arquivo_de_midia import ArquivoDeMidia
from Streaming.playlist import Playlist
from Streaming.musica import Musica
from Streaming.podcast import Podcast
from Streaming.usuario import Usuario

class Analises:
    @staticmethod
    def top_musicas_reproduzidas(musicas, top_n):
        ordenadas = sorted(musicas, key=lambda m: m.reproducoes, reverse=True)
        return ordenadas[:max(0, int(top_n))]

    @staticmethod
    def playlist_mais_popular(playlists):
        if not playlists:
            return None
        return max(playlists, key=lambda p: p.reproducoes)

    @staticmethod
    def usuario_mais_ativo(usuarios):
        if not usuarios:
            return None
        return max(usuarios, key=lambda u: len(u.historico))
