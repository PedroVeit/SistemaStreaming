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
            print("1. Reproduzir uma música")
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
                self.reproduzir_musica(usuario)
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

    def reproduzir_midia(self, usuario): #reproduz uma mídia (música ou podcast)
        self._exibir_cabecalho("Reproduzir mídia")
        self.listar_midias(pausar=False)
        titulo = input("Digite o título da mídia que deseja ouvir: ")
        midia = self.sistema.encontrar_midia(titulo) #procura a mídia pelo título
        if midia:
            usuario.ouvir_midia(midia)
        else:
            print(f"Mídia '{titulo}' não encontrada.")
            self.sistema.log_erro(f"Mídia '{titulo}' não encontrada.") #log de erro
        input("Pressione Enter para continuar...")

    def listar_midias(self, pausar=True): #lista todas as mídias (músicas e podcasts)
        self._exibir_cabecalho("Músicas e Podcasts")
        print("\n--- Músicas ---")
        for m in self.sistema.musicas:
            print(m)

        print("\n--- Podcasts ---")
        for p in self.sistema.podcasts:
            print(p)

        if pausar:
            input("\nAperte Enter")

    def listar_playlists(self, usuario): #lista as playlists do usuário
        self._exibir_cabecalho("Suas playlists")
        if not usuario.playlists:
            print("Você ainda não criou nenhuma playlist.")
        else:
            for i, p in enumerate(usuario.playlists): #mostra o índice e o nome da playlist
                print(f"{i+1}. {p}")
        input("Aperte Enter")

    def criar_playlist(self, usuario): #cria uma nova playlist para o usuário
        self._exibir_cabecalho("Criar uma nova playlist")
        nome_playlist = input("Digite o nome da nova playlist: ")
        if nome_playlist.strip() == "": #verifica se o nome é vazio
            print("O nome da playlist não pode ser vazio.")
            self.sistema.log_erro("Tentativa de criar playlist sem nome.")
            input("Aperte enter")
            return
        try:
            playlist = usuario.criar_playlist(nome_playlist) #tenta criar a playlist
            print("\nMídias disponíveis para adicionar à playlist:")
            self.listar_midias()
            
            while True: #loop para adicionar mídias à playlist
                print("\nAdicionar mídia à playlist:")
                titulo_midia = input("Título da mídia: ")
                if not titulo_midia:
                    break
                midia = self.sistema.encontrar_midia(titulo_midia)
                if midia:
                    playlist.adicionar_midia(midia)
                    print(f"'{midia.titulo}' adicionada.")
                else:
                    print(f"Mídia '{titulo_midia}' não encontrada.")

            if not playlist.itens: #verifica se a playlist está vazia
                usuario.playlists.remove(playlist)
                print("Atenção: A playlist está vazia. Não será criada.")
                self.sistema.log_erro(f"Playlist '{nome_playlist}' não criada por estar vazia.")
            else:
                print(f"Playlist '{nome_playlist}' criada")

        except ValueError as e: #erro de playlist já existente
            print(f"Erro: {e}")
            self.sistema.log_erro(str(e))

        input("Pressione Enter para continuar...")

    def reproduzir_playlist(self, usuario): #reproduz uma playlist do usuário
        self._exibir_cabecalho("Reproduzir uma playlist")
        if not usuario.playlists: #verifica se o usuário tem playlists
            print("Você ainda não criou nenhuma playlist.")
            self.sistema.log_erro("Tentativa de reproduzir playlist sem playlists criadas.")
            input("Pressione Enter para continuar...")
            return
        i = 0 #mostra as playlists com índices
        for p in usuario.playlists: #itera sobre as playlists do usuário
            print(f"{i}. {p.nome} ({len(p)} itens)")
            i += 1

        try: #tenta pegar o índice da playlist e reproduzir
            idx = int(input("Índice da playlist para reproduzir: "))
            playlist = usuario.playlists[idx]
            playlist.reproduzir()
        except (ValueError, IndexError): #erros de conversão ou índice fora do intervalo
            print("Erro: índice inválido.")
            self.sistema.log_erro("Índice de playlist inválido ao tentar reproduzir.")

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
