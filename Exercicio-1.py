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


class DataAnalysis(ABC):

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


class NameList(DataAnalysis):

    def __init__(self):
        super().__init__(type("String"))
        self.__list = []

    def input_data(self):
        num_elements = int(input("Quantos elementos na lista de nomes? "))
        for _ in range(num_elements):
            name = input("Digite um nome: ")
            self.__list.append(name)

    def show_median(self):
        try:
            sorted_list = sorted(self.__list)
            size = len(sorted_list)
            if size % 2 == 0:
                middle1 = sorted_list[size // 2 - 1]
                middle2 = sorted_list[size // 2]
                median = f"{middle1} e {middle2}"
            else:
                median = sorted_list[size // 2]
            print("Mediana:", median)
        except TypeError:
            print("Erro: Certifique-se de que todos os valores na lista de nomes sejam strings.")

    def show_minimum(self):
        print("Menor elemento:", min(self.__list))

    def show_maximum(self):
        print("Maior elemento:", max(self.__list))

    def __str__(self):
        return str(self.__list)


class DateList(DataAnalysis):

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


class SalaryList(DataAnalysis):

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


class AgeList(DataAnalysis):

    def __init__(self):
        super().__init__(type(int))
        self.__list = []

    def input_data(self):
        num_elements = int(input("Quantos elementos na lista de idades? "))
        for _ in range(num_elements):
            age = int(input("Idade: "))
            self.__list.append(age)

    def show_median(self):
        try:
            sorted_list = sorted(self.__list)
            size = len(sorted_list)
            if size % 2 == 0:
                median = (sorted_list[size // 2 - 1] + sorted_list[size // 2]) / 2
            else:
                median = sorted_list[size // 2]
            print("Mediana:", median)
        except TypeError:
            print("Erro: Certifique-se de que todos os valores na lista de idades sejam números.")

    def show_minimum(self):
        try:
            minimum_age = min(self.__list)
            print("Menor idade:", minimum_age)
        except ValueError:
            print("Erro: Certifique-se de que todos os valores na lista de idades sejam números.")

    def show_maximum(self):
        try:
            maximum_age = max(self.__list)
            print("Maior idade:", maximum_age)
        except ValueError:
            print("Erro: Certifique-se de que todos os valores na lista de idades sejam números.")

    def __str__(self):
        return str(self.__list)


def main():
    names = NameList()
    dates = DateList()
    salaries = SalaryList()
    ages = AgeList()

    data_lists = [names, dates, salaries, ages]

    for data_list in data_lists:
        data_list.input_data()
        data_list.show_median()
        data_list.show_minimum()
        data_list.show_maximum()
        print("___________________")

    print("Fim do teste!!!")


if __name__ == "__main__":
    main()