from modulos.restaurante import Restaurante
import os

def cabecalho():
    print('''
    ███████╗░█████╗░████████╗██╗███╗░░██╗░██████╗░  ██████╗░██╗░░░██╗
    ██╔════╝██╔══██╗╚══██╔══╝██║████╗░██║██╔════╝░  ██╔══██╗╚██╗░██╔╝
    █████╗░░███████║░░░██║░░░██║██╔██╗██║██║░░██╗░  ██████╦╝░╚████╔╝░
    ██╔══╝░░██╔══██║░░░██║░░░██║██║╚████║██║░░╚██╗  ██╔══██╗░░╚██╔╝░░
    ███████╗██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝  ██████╦╝░░░██║░░░
    ╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═════╝░░░░╚═╝░░░''')

def titulo(msg):
    os.system('cls')
    tam = len(msg) + 4
    print('=' * tam)
    print(msg.center(tam))
    print('=' * tam)

def voltar_menu():
    input('Aperte uma tecla para voltar')
    main()

def opcoes():
    print('''\n1. Cadastrar novo restaurante
2. Listar restaurantes
3. Sair''')

def escolhas():
    try:
        escolha = int(input('Sua escolha:'))
        if escolha == 1:
            cadastrar_restaurante()
        elif escolha == 2:
            listar_restaurante()
        elif escolha == 3:
            finalizar()
        else:
            print('Opção inválida!')
    except:
        print('Opção inválida!')



def cadastrar_restaurante():
    titulo('Cadastrar novo restaurante')
    nome_restaurante = input('Digite o nome do restaurante:')
    categoria_restaurante = input('Digite a categoria:')
    endereco_restaurante = input('Digite o endereço:')
    Restaurante(nome_restaurante, endereco_restaurante, categoria_restaurante)
    voltar_menu()

def listar_restaurante():
    titulo('Listando restaurantes')
    Restaurante.exibir_restaurantes()
    voltar_menu()

def finalizar():
    titulo('Finalizando...')

restaurante_pizza = Restaurante('Pizza Creck', 'Rua dos Antores', 'Pizza')
restaurante_japones = Restaurante('Japan House', 'Rua Shinobi', 'Japonesa')


def main():
    cabecalho()
    opcoes()
    escolhas()


if __name__ == '__main__':
    main()