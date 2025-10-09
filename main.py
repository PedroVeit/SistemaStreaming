import os

class SistemaStreaming:
    def __init__(self, arquivo_config):
        self.musicas = []
        self.podcasts = []
        self.usuarios = []
        self.playlists = []
        self.arquivo_config = arquivo_config
        self.log = 'erros.log'

    def _salvar_erro(self, mensagem):
        try:
            with open(self.log, 'a') as arquivo:
                arquivo.write(mensagem + '\n')
        except:
            pass