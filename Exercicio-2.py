from abc import ABC, abstractmethod
from typing import List

class Data:
    
    def __init__(self, day=1, month=1, year=2000):
        if day < 1 or day > 31:
            raise ValueError("Dia inválido")
        if month < 1 or month > 12:
            raise ValueError("Mês inválido")
        if year < 2000 or year > 2100:
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

    def __eq__(self, another_date):
        return  self.__day == another_date.__day and \
                self.__month == another_date.__month and \
                self.__year == another_date.__year
    
    def __lt__(self, another_date):
        if self.__year < another_date.__year:
            return True
        elif self.__year == another_date.__year:
            if self.__month < another_date.__month:
                return True
            elif self.__month == another_date.__month:
                if self.__day < another_date.__day:
                    return True
        return False
    
    def __gt__(self, another_date):
        if self.__year > another_date.__year:
            return True
        elif self.__year == another_date.__year:
            if self.__month > another_date.__month:
                return True
            elif self.__month == another_date.__month:
                if self.__day > another_date.__day:
                    return True
        return False

class AnalysisData(ABC):
    @abstractmethod
    def __init__(self, data_type):
        self.__data_type = data_type

    @abstractmethod
    def input_data(self):
        pass

    @abstractmethod
    def show_median(self):
        pass
    
    @abstractmethod
    def show_minimum(self):
        pass

    @abstractmethod
    def show_maximum(self):
        pass

class NameList(AnalysisData):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__list = []        

    def input_data(self):
        n = int(input("Quantos nomes na lista? "))
        for _ in range(n):
            name = input("Digite um nome: ")
            self.__list.append(name)

    def show_median(self):
        self.__list.sort()
        median = self.__list[len(self.__list)//2]
        print("Mediana:", median)

    def show_minimum(self):
        minimum = min(self.__list)
        print("Mínimo:", minimum)

    def show_maximum(self):
        maximum = max(self.__list)
        print("Máximo:", maximum)

    def __str__(self):
        return str(self.__list)

class DateList(AnalysisData):
    
    def __init__(self):
        super().__init__(type(Data))
        self.__list = []        

    def input_data(self):
        n = int(input("Quantas datas na lista? "))
        for _ in range(n):
            day = int(input("Dia: "))
            month = int(input("Mês: "))
            year = int(input("Ano: "))
            date = Data(day, month, year)
            self.__list.append(date)

    def show_median(self):
        self.__list.sort(key=lambda x: (x.year, x.month, x.day))
        median = self.__list[len(self.__list)//2]
        print("Mediana:", median)

    def show_minimum(self):
        minimum = min(self.__list)
        print("Mínimo:", minimum)

    def show_maximum(self):
        maximum = max(self.__list)
        print("Máximo:", maximum)

    def __str__(self):
        return '\n'.join(map(str, self.__list))

class SalaryList(AnalysisData):

    def __init__(self):
        super().__init__(type(float))
        self.__list = []        

    def input_data(self):
        n = int(input("Quantos salários na lista? "))
        for _ in range(n):
            salary = float(input("Digite um salário: "))
            self.__list.append(salary)

    def show_median(self):
        self.__list.sort()
        median = self.__list[len(self.__list)//2]
        print("Mediana:", median)

    def show_minimum(self):
        minimum = min(self.__list)
        print("Mínimo:", minimum)

    def show_maximum(self):
        maximum = max(self.__list)
        print("Máximo:", maximum)

    def __str__(self):
        return str(self.__list)

class AgeList(AnalysisData):
    
    def __init__(self):
        super().__init__(type(int))
        self.__list = []        

    def input_data(self):
        n = int(input("Quantas idades na lista? "))
        for _ in range(n):
            age = int(input("Digite uma idade: "))
            self.__list.append(age)

    def show_median(self):
        self.__list.sort()
        median = self.__list[len(self.__list)//2]
        print("Mediana:", median)

    def show_minimum(self):
        minimum = min(self.__list)
        print("Mínimo:", minimum)

    def show_maximum(self):
        maximum = max(self.__list)
        print("Máximo:", maximum)

    def __str__(self):
        return str(self.__list)

def main():
    names = NameList()
    dates = DateList()
    salaries = SalaryList()
    ages = AgeList()

    lists = [names, dates, salaries, ages]

    for lista in lists:
        lista.input_data()
        lista.show_median()
        lista.show_minimum()
        lista.show_maximum()
        print("___________________")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
