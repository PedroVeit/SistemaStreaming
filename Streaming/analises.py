from Streaming.arquivo_de_midia import ArquivoDeMidia
from Streaming.playlist import Playlist
from Streaming.musica import Musica
from Streaming.podcast import Podcast
from Streaming.usuario import Usuario

class Analises:
    @staticmethod
    def top_musicas_reproduzidas(musicas, top_n): #retorna as top_n músicas mais reproduzidas
        if not musicas or top_n <= 0: 
            return []
        return sorted(musicas, key=lambda m: m.reproducoes, reverse=True)[:top_n]   

    @staticmethod
    def playlist_mais_popular(playlists): #retorna a playlist com mais reproduções
        if not playlists:
            return None
        return max(playlists, key=lambda p: p.reproducoes)

    @staticmethod
    def usuario_mais_ativo(usuarios): #retorna o usuário com mais mídias no histórico
        if not usuarios:
            return None
        return max(usuarios, key=lambda u: len(u.historico))

    @staticmethod
    def media_avaliacoes(musicas): #retorna um dicionário com a média das avaliações de cada música
        resultados = {} #dicionário para armazenar os resultados
        for m in musicas:
            if m.avaliacoes:
                resultados[m.titulo] = float(sum(m.avaliacoes)) / float(len(m.avaliacoes)) #média das avaliações
            else:
                resultados[m.titulo] = 0.0 #se não houver avaliações, a média é 0
        return resultados

    @staticmethod
    def total_reproducoes(usuarios): #retorna o total de reproduções de todas as mídias no histórico de todos os usuários
        total = 0
        for u in usuarios:
            for midia in u.historico:
                total += midia.reproducoes
        return total