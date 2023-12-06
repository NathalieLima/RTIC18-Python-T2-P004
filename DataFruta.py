from abc import ABC, abstractmethod

class CustomDate:
    def __init__(self, day=1, month=1, year=2000):
        if day < 1 or day > 31:
            raise ValueError("Dia inválido")
        if month < 1 or month > 12:
            raise ValueError("Mês inválido")
        if year < 1900 or year > 2100:
            raise ValueError("Ano inválido")
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if day < 1 or day > 31:
            raise ValueError("Dia inválido")
        self.__day = day

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if month < 1 or month > 12:
            raise ValueError("Mês inválido")
        self.__month = month

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 2000 or year > 2100:
            raise ValueError("Ano inválido")
        self.__year = year

    def __str__(self):
        return "{}/{}/{}".format(self.__day, self.__month, self.__year)

    def __eq__(self, other_date):
        return self.__day == other_date.__day and \
               self.__month == other_date.__month and \
               self.__year == other_date.__year

    def __lt__(self, other_date):
        if self.__year < other_date.__year:
            return True
        elif self.__year == other_date.__year:
            if self.__month < other_date.__month:
                return True
            elif self.__month == other_date.__month:
                if self.__day < other_date.__day:
                    return True
        return False

    def __gt__(self, other_date):
        if self.__year > other_date.__year:
            return True
        elif self.__year == other_date.__year:
            if self.__month > other_date.__month:
                return True
            elif self.__month == other_date.__month:
                if self.__day > other_date.__day:
                    return True
        return False


class Data(CustomDate):  # Inherit from CustomDate
    
    def __str__(self):
        return "{}/{}/{}".format(self.day, self.month, self.year)


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
        self.__lista = []        

    def entradaDeDados(self):
        # Implement your logic for entering names
        pass

    def mostraMediana(self):
        # Implement your logic for displaying median
        pass    

    def mostraMenor(self):
        # Implement your logic for displaying the smallest element
        pass

    def mostraMaior(self):
        # Implement your logic for displaying the largest element
        pass    

    def __str__(self):
        # Implement your logic for displaying the list
        pass
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        # Implement your logic for entering dates
        pass
    
    def mostraMediana(self):
        # Implement your logic for displaying median
        pass    
     
    def mostraMenor(self):
        # Implement your logic for displaying the smallest element
        pass
    
    def mostraMaior(self):
        # Implement your logic for displaying the largest element
        pass
    
    def __str__(self):
        # Implement your logic for displaying the list
        pass

# Similarly, modify the other classes accordingly

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
