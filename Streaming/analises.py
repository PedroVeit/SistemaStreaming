from Streaming.arquivo_de_midia import ArquivoDeMidia
from Streaming.playlist import Playlist
from Streaming.musica import Musica
from Streaming.podcast import Podcast
from Streaming.usuario import Usuario

class Analises:
    @staticmethod
    def top_musicas_reproduzidas(musicas: list[Musica], top_n: int):
        #ordenadas = sorted(musicas, key=lambda m: m.reproducoes, reverse=True)
        #return ordenadas[:max(0, int(top_n))]

    @staticmethod
    def playlist_mais_popular(playlists: list[Playlist]):
        if not playlists:
            return None
        return max(playlists, key=lambda p: p.reproducoes)

    @staticmethod
    def usuario_mais_ativo(usuarios: list[Usuario]):
        if not usuarios:
            return None
        return max(usuarios, key=lambda u: len(u.historico))
        
    @staticmethod
    def media_avaliacoes(musicas: list[Musica]):
        resultados = {}
        for m in musicas:
            if m.avaliacoes:
                resultados[m.titulo] = float(sum(m.avaliacoes)) / float(len(m.avaliacoes))
            else:
                resultados[m.titulo] = 0.0
        return resultados

    @staticmethod
    def total_reproducoes(usuarios: list[Usuario]):
        total = 0
        for u in usuarios:
            for midia in u.historico:
                total += midia.reproducoes
        return total
