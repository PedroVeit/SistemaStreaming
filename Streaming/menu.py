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
