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

    @staticmethod
    def media_avaliacoes(musicas):
        resultados = {}
        for m in musicas:
            if m.avaliacoes:
                resultados[m.titulo] = float(sum(m.avaliacoes)) / float(len(m.avaliacoes))
            else:
                resultados[m.titulo] = 0.0
        return resultados

    @staticmethod
    def total_reproducoes(usuarios):
        total = 0
        for u in usuarios:
            for midia in u.historico:
                total += midia.reproducoes
        return total

    # INOVAÇÃO: Análises do sistema de favoritos
    @staticmethod
    def top_musicas_curtidas(musicas, top_n):
        """Retorna as músicas mais curtidas."""
        ordenadas = sorted(musicas, key=lambda m: m.likes, reverse=True)
        return ordenadas[:max(0, int(top_n))]

    @staticmethod
    def total_curtidas(usuarios):
        """Total de curtidas de todos os usuários."""
        total = 0
        for u in usuarios:
            total += len(u.favoritos)
        return total
