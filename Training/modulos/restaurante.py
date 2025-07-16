
class Restaurante:
    restaurantes = []
    def __init__(self, nome, endereco, categoria):
        self._nome = nome
        self._endereco = endereco
        self._categoria = categoria
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def exibir_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(20)} | {'Endereço'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(20)} | '
                  f'{restaurante._endereco.ljust(25)}')

