from abc import ABC, abstractmethod
from typing import List


class Data:

    def __init__(self, day=1, month=1, year=2000):
        if day < 1 or day > 31:
            raise ValueError("Invalid day")
        if month < 1 or month > 12:
            raise ValueError("Invalid month")
        if year < 2000 or year > 2100:
            raise ValueError("Invalid year")
        self.__day = day
        self.__month = month
        self.__year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if day < 1 or day > 31:
            raise ValueError("Invalid day")
        self.__day = day

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month):
        if month < 1 or month > 12:
            raise ValueError("Invalid month")
        self.__month = month

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 2000 or year > 2100:
            raise ValueError("Invalid year")
        self.__year = year

    def __str__(self):
        return "{}/{}/{}".format(self.__day, self.__month, self.__year)

    def __eq__(self, another_date):
        return self.__day == another_date.__day and \
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

    @abstractmethod
    def list_in_order(self):
        pass

    @abstractmethod
    def calculate_mean(self):
        pass


class NameList(AnalysisData):

    def __init__(self):
        super().__init__(str)
        self.__list = []

    def input_data(self):
        name = input("Digite um nome: ")
        self.__list.append(name)

    def show_median(self):
        self.__list.sort()
        median = self.__list[len(self.__list) // 2]
        print("Mediana:", median)

    def show_minimum(self):
        minimum = min(self.__list)
        print("Menor:", minimum)

    def show_maximum(self):
        maximum = max(self.__list)
        print("Maior:", maximum)

    def list_in_order(self):
        print("Lista de Nomes em Ordem:")
        for name in sorted(self.__list):
            print(name)

    def calculate_mean(self):
        pass  # No mean calculation for names

    def __iter__(self):
        return iter(self.__list)

    def __str__(self):
        return str(self.__list)


class DateList(AnalysisData):

    def __init__(self):
        super().__init__(Data)
        self.__list = []

    def input_data(self):
        day = int(input("Dia: "))
        month = int(input("Mês: "))
        year = int(input("Ano: "))
        date = Data(day, month, year)
        self.__list.append(date)

    def show_median(self):
        self.__list.sort(key=lambda x: (x.year, x.month, x.day))
        median = self.__list[len(self.__list) // 2]
        print("Mediana:", median)

    def show_minimum(self):
        minimum = min(self.__list)
        print("Menor:", minimum)

    def show_maximum(self):
        maximum = max(self.__list)
        print("Maior:", maximum)

    def list_in_order(self):
        print("Lista de Datas em Ordem:")
        for date in sorted(self.__list):
            print(date)

    def calculate_mean(self):
        pass  # No mean calculation for dates

    def update_days_before_2017(self):
        for date in self.__list:
            if date.year < 2017:
                date.day = 1

    def __iter__(self):
        return iter(self.__list)

    def __str__(self):
        return '\n'.join(map(str, self.__list))


class SalaryList(AnalysisData):

    def __init__(self):
        super().__init__(float)
        self.__list = []

    def input_data(self):
        salary = float(input("Digite um salário: "))
        self.__list.append(salary)

    def show_median(self):
        self.__list.sort()
        median = self.__list[len(self.__list) // 2]
        print("Mediana:", median)

    def show_minimum(self):
        minimum = min(self.__list)
        print("Menor:", minimum)

    def show_maximum(self):
        maximum = max(self.__list)
        print("Maior:", maximum)

    def list_in_order(self):
        print("Lista de Salários em Ordem:")
        for salary in sorted(self.__list):
            print(salary)

    def calculate_mean(self):
        mean = sum(self.__list) / len(self.__list)
        print(f"Média dos salários: {mean}")

    def __iter__(self):
        return iter(self.__list)

    def __str__(self):
        return str(self.__list)


class AgeList(AnalysisData):

    def __init__(self):
        super().__init__(int)
        self.__list = []

    def input_data(self):
        age = int(input("Digite uma idade: "))
        self.__list.append(age)

    def show_median(self):
        self.__list.sort()
        median = self.__list[len(self.__list) // 2]
        print("Mediana:", median)

    def show_minimum(self):
        minimum = min(self.__list)
        print("Menor:", minimum)

    def show_maximum(self):
        maximum = max(self.__list)
        print("Maior:", maximum)

    def list_in_order(self):
        print("Lista de Idades em Ordem:")
        for age in sorted(self.__list):
            print(age)

    def calculate_mean(self):
        mean = sum(self.__list) / len(self.__list)
        print(f"Média das idades: {mean}")

    def __iter__(self):
        return iter(self.__list)

    def __str__(self):
        return str(self.__list)


def include_name(name_list):
    name_list.input_data()


def include_salary(salary_list):
    salary_list.input_data()


def include_date(date_list):
    date_list.input_data()


def include_age(age_list):
    age_list.input_data()


def traverse_lists(name_list, salary_list):
    print("Zip Iterator:")
    for name, salary in zip(name_list, salary_list):
        print(f"{name}: {salary}")


def calculate_salary_increase(salary_list):
    print("Map Iterator:")
    salaries_increased = map(lambda x: x * 1.1, salary_list)
    print(list(salaries_increased))


def modify_days_before_2017(date_list):
    print("Filter Iterator:")
    date_list.update_days_before_2017()
    for date in date_list:
        print(date)


def main():
    names = NameList()
    dates = DateList()
    salaries = SalaryList()
    ages = AgeList()

    while True:
        print("\nMenu:")
        print("1. Adicionar um nome na lista de nomes")
        print("2. Adicionar um salário na lista de salários")
        print("3. Adicionar uma data na lista de datas")
        print("4. Adicionar uma idade na lista de idades")
        print("5. Percorrer as listas de nomes e salários")
        print("6. Calcular o valor da folha com um reajuste de 10%")
        print("7. Modificar o dia das datas anteriores a 2017")
        print("8. Sair")

        choice = input("Escolha uma das opção : ")

        if choice == '1':
            include_name(names)
        elif choice == '2':
            include_salary(salaries)
        elif choice == '3':
            include_date(dates)
        elif choice == '4':
            include_age(ages)
        elif choice == '5':
            traverse_lists(names, salaries)
        elif choice == '6':
            calculate_salary_increase(salaries)
        elif choice == '7':
            modify_days_before_2017(dates)
        elif choice == '8':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
git 