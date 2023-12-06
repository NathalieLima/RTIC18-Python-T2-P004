from abc import ABC, abstractmethod

class CustomDate:
    def __init__(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 1900 or ano > 2100:
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

    def __eq__(self, outra_data):
        return self.__dia == outra_data.__dia and \
               self.__mes == outra_data.__mes and \
               self.__ano == outra_data.__ano

    def __lt__(self, outra_data):
        if self.__ano < outra_data.__ano:
            return True
        elif self.__ano == outra_data.__ano:
            if self.__mes < outra_data.__mes:
                return True
            elif self.__mes == outra_data.__mes:
                if self.__dia < outra_data.__dia:
                    return True
        return False

    def __gt__(self, outra_data):
        if self.__ano > outra_data.__ano:
            return True
        elif self.__ano == outra_data.__ano:
            if self.__mes > outra_data.__mes:
                return True
            elif self.__mes == outra_data.__mes:
                if self.__dia > outra_data.__dia:
                    return True
        return False


class Data(CustomDate):  # Herda de CustomDate
    
    def __str__(self):
        return "{}/{}/{}".format(self.dia, self.mes, self.ano)


class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipo_de_dados):
        self.__tipo_de_dados = tipo_de_dados

    @abstractmethod
    def entrada_de_dados(self):
        pass

    @abstractmethod
    def mostra_mediana(self):
        pass
    
    @abstractmethod
    def mostra_menor(self):
        pass

    @abstractmethod
    def mostra_maior(self):
        pass


class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entrada_de_dados(self):
        # Implemente sua lógica para inserir nomes
        pass

    def mostra_mediana(self):
        # Implemente sua lógica para exibir a mediana
        pass    

    def mostra_menor(self):
        # Implemente sua lógica para exibir o menor elemento
        pass

    def mostra_maior(self):
        # Implemente sua lógica para exibir o maior elemento
        pass    

    def __str__(self):
        # Implemente sua lógica para exibir a lista
        pass
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entrada_de_dados(self):
        # Implemente sua lógica para inserir datas
        pass
    
    def mostra_mediana(self):
        # Implemente sua lógica para exibir a mediana
        pass    
     
    def mostra_menor(self):
        # Implemente sua lógica para exibir o menor elemento
        pass
    
    def mostra_maior(self):
        # Implemente sua lógica para exibir o maior elemento
        pass
    
    def __str__(self):
        # Implemente sua lógica para exibir a lista
        pass

# Modifique as outras classes de maneira semelhante

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    lista_listas = [nomes, datas, salarios, idades]

    for lista in lista_listas:
        lista.entrada_de_dados()
        lista.mostra_mediana()
        lista.mostra_menor()
        lista.mostra_maior()
        print("___________________")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
