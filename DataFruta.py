# EXERCÍCIO 1

from abc import ABC, abstractmethod


class Data:
    
    def __init__(self, dia = 1, mes = 1, ano = 2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return  self.__dia == outraData.__dia and \
                self.__mes == outraData.__mes and \
                self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False

class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

class ListaNomes(AnaliseDados):

    def __init__(self):
        super().__init__(type("String"))
        self.__list = []

    def ordenaLista(self):
        '''
        Este método retorna nova lista 
        a partir da ordenação da atual
        '''
        lista = self.__lista
        lista.sort()

        return lista

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles.
        '''
        flag = False
        qtde = 0

        while not flag:
            # Solicitar a quantidade de elementos
            qtde = int(input("Quantos elementos vão existir na lista? "))

            if qtde > 0:
                flag = True
            else:
                print("Aviso: Entre com um número a partir de 1.")

        # Solicitar cada elemento
        for i in range(qtde):
            elemento = input(f'Nome {i + 1}: ').capitalize()

            self.__lista.append(elemento)

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        lista_sorteada = self.ordenaLista()
        tamanho = len(lista_sorteada)
        mediana = ""
        indice_mediana = ""
        
        if (tamanho % 2 == 0):
            indice_mediana = tamanho // 2 - 1
        else:
            indice_mediana = tamanho // 2

        # Atribuição da mediana 
        mediana = lista_sorteada[indice_mediana]

        print('A mediana da lista de nomes é', mediana)    

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        menor = min(self.__lista)

        print('O primeiro nome alfabeticamente é:', menor)

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        maior = max(self.__lista)

        print('O último nome alfabeticamente é:', maior)

    def mostraDados(self):
        '''
        Este método percorre e mostra os elementos da lista
        '''
        print('LISTA DE NOMES')

        for (index, item) in enumerate(self.__lista):
            print(f'Nome {index + 1}: {item}')

    def __str__(self):
        return str(self.__lista)
	
class ListaDatas(AnaliseDados):

    def __init__(self):
        super().__init__(type(CustomDate))
        self.__list = []

    def input_data(self):
        num_elements = int(input("Quantos elementos na lista de datas? "))
        for _ in range(num_elements):
            day = int(input("Dia: "))
            month = int(input("Mês: "))
            year = int(input("Ano: "))
            new_date = CustomDate(day, month, year)
            self.__list.append(new_date)

    def show_median(self):
        try:
            sorted_list = sorted(self.__list, key=lambda data: (data.year, data.month, data.day))
            size = len(sorted_list)
            if size % 2 == 0:
                middle1 = sorted_list[size // 2 - 1]
                middle2 = sorted_list[size // 2]
                median = f"{middle1} e {middle2}"
            else:
                median = sorted_list[size // 2]
            print("Mediana:", median)
        except TypeError:
            print("Erro: Certifique-se de que todos os valores na lista de datas sejam objetos CustomDate.")

    def show_minimum(self):
        try:
            minimum_date = min(self.__list, key=lambda data: (data.year, data.month, data.day))
            print("Menor data:", minimum_date)
        except TypeError:
            print("Erro: Certifique-se de que todos os valores na lista de datas sejam objetos CustomDate.")

    def show_maximum(self):
        try:
            maximum_date = max(self.__list, key=lambda data: (data.year, data.month, data.day))
            print("Maior data:", maximum_date)
        except TypeError:
            print("Erro: Certifique-se de que todos os valores na lista de datas sejam objetos CustomDate.")

    def __str__(self):
        return str(self.__list)


class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__list = []

    def input_data(self):
        num_elements = int(input("Quantos elementos na lista de salários? "))
        for _ in range(num_elements):
            salary = float(input("Salário: "))
            self.__list.append(salary)

    def show_median(self):
        try:
            sorted_list = sorted(self.__list)
            size = len(sorted_list)
            if size % 2 == 0:
                median = (float(sorted_list[size // 2 - 1]) + float(sorted_list[size // 2])) / 2
            else:
                median = float(sorted_list[size // 2])
            print("Mediana:", median)
        except ValueError:
            print("Erro: Certifique-se de que todos os valores na lista de salários sejam números.")

    def show_minimum(self):
        try:
            minimum_salary = min(self.__list)
            print("Menor salário:", minimum_salary)
        except ValueError:
            print("Erro: Certifique-se de que todos os valores na lista de salários sejam números.")

    def show_maximum(self):
        try:
            maximum_salary = max(self.__list)
            print("Maior salário:", maximum_salary)
        except ValueError:
            print("Erro: Certifique-se de que todos os valores na lista de salários sejam números.")

    def __str__(self):
        return str(self.__list)


class ListaIdades(AnaliseDados):

    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        ida = int(input("Quantas idades na lista?"))
        for _ in range(ida):
            idade = (input("Idade: "))
            self.__lista.append(idade)

    
    def mostraMediana(self):
        sorted_list = sorted(self.__lista)
        size = len(sorted_list)
        if size % 2 == 0:
            median = (sorted_list[size // 2 - 1] + sorted_list[size // 2]) / 2
        else: 
            median = sorted_list[size // 2]
        print("Mediana ", median)
    
    def mostraMenor(self):
        menor_idade = min(self.__lista)
        print("Menor idade: ", menor_idade)
    
    def mostraMaior(self):
        maior_idade = max(self.__lista)
        print("Maior idade: ", maior_idade)

    def __str__(self):
        return str(self.__lista)

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        print("___________________")

    print("Fim do teste!!!")


if __name__ == "__main__":
    main()