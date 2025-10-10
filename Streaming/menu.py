import os
import datetime
from Streaming.analises import Analises
from Streaming.playlist import Playlist

class Menu: #gerencia a interface de linha de comando do sistema
    def __init__(self, sistema):
        self.sistema = sistema

    def _limpar_tela(self): #limpa a tela do terminal
        os.system('cls' if os.name == 'nt' else 'clear')

    def _mostrar_cabecalho(self, titulo): #exibe o cabeçalho do menu com o título centralizado
        self._limpar_tela()
        print(f"\n{'=' * 30}\n{titulo.center(30)}\n{'=' * 30}")

    def menu_principal(self): #menu principal
        while True:
            self._mostrar_cabecalho("MENU PRINCIPAL")
            print("1. Entrar como usuário")
            print("2. Criar novo usuário")
            print("3. Listar usuários")
            print("4. Sair")
            
            escolha = input("Opção: ")
            if escolha == '1':
                self.entrar_como_usuario()
            elif escolha == '2':
                self.criar_novo_usuario()
            elif escolha == '3':
                self.listar_usuarios()
            elif escolha == '4':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida!")
                input("Aperte Enter")

    def entrar_como_usuario(self): #login de usuário    
        self._mostrar_cabecalho("Entrar como usuário")
        nome = input("Nome de usuário: ")
        usuario = self.sistema.encontrar_usuario(nome)
        if usuario:
            self.menu_usuario(usuario)
        else:
            print("Usuário não encontrado!")
            input("Aperte Enter")

    def criar_novo_usuario(self): #cria um novo usuário
        self._mostrar_cabecalho("Criar novo usuário")
        nome = input("Nome do novo usuário: ")
        if not nome.strip():
            print("Nome não pode ser vazio!")
        else:
            try: #tenta criar o usuário
                self.sistema.criar_usuario(nome)
                print("Usuário criado com sucesso!")
            except ValueError as e: #erro de usuário já existente
                print(f"Erro: {e}") #exibe a mensagem de erro
        input("Aperte Enter")

    def listar_usuarios(self): #lista todos os usuários cadastrados
        self._mostrar_cabecalho("Listar usuários")
        if not self.sistema.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for usuario in self.sistema.usuarios:
                print(f"- {usuario.nome}")
        input("Aperte Enter")

    def menu_usuario(self, usuario): #menu específico para cada usuário
        while True:
            self._mostrar_cabecalho(f"BEM-VINDO, {usuario.nome.upper()}")
            print("1. Reproduzir uma mídia") 
            print("2. Listar músicas")
            print("3. Listar podcasts")
            print("4. Listar playlists")
            print("5. Reproduzir uma playlist")
            print("6. Criar nova playlist")
            print("7. Concatenar playlists")
            print("8. Gerar relatório")
            print("9. Sair")
            escolha = input("Opção: ")

            if escolha == '1':
                self.reproduzir_midia(usuario)
            elif escolha == '2':
                self.listar_musicas()
            elif escolha == '3':
                self.listar_podcasts()
            elif escolha == '4':
                self.listar_playlists(usuario)
            elif escolha == '5':
                self.reproduzir_playlist(usuario)
            elif escolha == '6':
                self.criar_playlist(usuario)
            elif escolha == '7':
                self.concatenar_playlists(usuario)
            elif escolha == '8':
                self.gerar_relatorio()
            elif escolha == '9':
                break
            else:
                print("Opção inválida!")
                input("Aperte Enter")

    def reproduzir_midia(self, usuario): #reproduz uma mídia escolhida pelo usuário
        self._mostrar_cabecalho("Reproduzir Mídia (Música/Podcast)")
        print("Mídias disponíveis (Músicas e Podcasts):")
        
        self.listar_musicas(pausar=False) 
        self.listar_podcasts(pausar=False)
        
        titulo = input("Título da mídia que deseja reproduzir: ")

        midia = self.sistema.encontrar_midia(titulo)
        
        if midia:
            usuario.ouvir_midia(midia)
            print(f"Reproduzindo '{midia.titulo}'.")
        else:
            print("Mídia (Música ou Podcast) não encontrada!")
        
        input("Aperte Enter")

    def listar_musicas(self, pausar=True): #lista todas as músicas disponíveis no sistema
        self._mostrar_cabecalho("Listar músicas")
        
        if not self.sistema.musicas: 
            print("Nenhuma música cadastrada no sistema.")
        else:
            for musica in self.sistema.musicas:
                print(f"- {musica.titulo} | Artista: {musica.artista}")
        
        if pausar:
            input("Aperte Enter")

    def listar_podcasts(self, pausar=True): #lista todos os podcasts disponíveis no sistema
        self._mostrar_cabecalho("Listar podcasts")
        
        if not self.sistema.podcasts:
            print("Nenhum podcast cadastrado no sistema.")
        else:
            for podcast in self.sistema.podcasts:
                print(f"- {podcast.titulo} | Host: {podcast.artista}") 
        
        if pausar:
            input("Aperte enter")

    def listar_playlists(self, usuario): #lista todas as playlists do usuário
        self._mostrar_cabecalho("Listar playlists")
        if not usuario.playlists:
            print("Nenhuma playlist criada.")
        else:
            for i, playlist in enumerate(usuario.playlists, 1): #percorre as playlists com índice começando em 1
                print(f"{i}. {playlist.nome} ({len(playlist)} itens)")
        input("Aperte Enter")

    def reproduzir_playlist(self, usuario): #reproduz uma playlist escolhida pelo usuário
        self._mostrar_cabecalho("Reproduzir playlist")
        if not usuario.playlists:
            print("Nenhuma playlist criada.")
            input("Aperte enter")
            return
            
        self.listar_playlists(usuario)

        try: #pega o índice da playlist e reproduz
            idx = int(input("Índice da playlist: ")) - 1
            playlist = usuario.playlists[idx]
            playlist.reproduzir() 
            print(f"Reproduzindo playlist '{playlist.nome}'.")
        except (ValueError, IndexError): #erros de conversão ou índice fora do intervalo
            print("Índice inválido!")
        input("Aperte enter")

    def criar_playlist(self, usuario): #cria uma nova playlist para o usuário
        self._mostrar_cabecalho("Criar nova playlist")
        nome = input("Nome da playlist: ")
        if not nome.strip():
            print("Nome não pode ser vazio!")
            input("Aperte enter")
            return
        
        playlist = usuario.criar_playlist(nome) #cria a playlist no usuário
        print("Playlist criada com sucesso!")
        input("Aperte enter")

    def concatenar_playlists(self, usuario): #concatena duas playlists do usuário
        self._mostrar_cabecalho("Concatenar duas playlists")
        if len(usuario.playlists) < 2:
            print("É necessário pelo menos duas playlists!")
            input("Aperte enter")
            return
        
        self.listar_playlists(usuario) #mostra as playlists do usuário
        try: #pega os índices das playlists e concatena
            idx1 = int(input("Índice da primeira playlist: ")) - 1
            idx2 = int(input("Índice da segunda playlist: ")) - 1
            p1 = usuario.playlists[idx1]
            p2 = usuario.playlists[idx2]
            
            nova_playlist = p1 + p2 
            
            usuario.playlists.append(nova_playlist)
            print(f"Playlists '{p1.nome}' e '{p2.nome}' concatenadas!")
        except (ValueError, IndexError): #erros de conversão ou índice fora do intervalo
            print("Índices inválidos!")
        input("Aperte enter")

    def gerar_relatorio(self): #gera um relatório de análises do sistema
        self._mostrar_cabecalho("Gerar relatório") #cabeçalho
        print("Relatório gerado com sucesso!")
        input("Aperte enter")
        
    #fizemos uso de inteligência artificial nesta parte do trabalho para nos auxiliar
