
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
    
	
    ''''
	Data (int _dia, int _mes, int _ano) {
		dia = _dia;
		mes = _mes;
		ano = _ano;
	}
    '''
    '''
	string toString() {
		string ret = "";
		ret.append(to_string(dia));
		ret.append("/");
		ret.append(to_string(mes));
		ret.append("/");
		ret.append(to_string(ano));
		return ret;
	}
    '''
    def to_string():
        ret = ""
        ret += str(dia)
        ret += "/"
        ret += str(mes)
        ret += "/"
        ret += str(ano)
        return ret
    #fimdef
#fim class Data

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
    #fimdef
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass
    
    @abstractmethod
    def listarEmOrdem(self):
        pass

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles.
        '''

        qtd_nomes = int(input("Digite o quantidade de nomes "))
        #nomes = []
        for item in range(qtd_nomes):
            nome = input("Digite nome: ")
            self.__lista.append(nome)
            #self.__lista=sorted(self.__lista)
        return self.__lista
    #fimdef

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        
        self.__lista=sorted(self.__lista)
        compr = len(self.__lista)
        if compr % 2 == 1:
            return self.__lista[compr // 2] #erredonda pra baixo
        else:
            return self.__lista[compr // 2 - 1]
        #fimse
    #fimdef

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        self.__lista=sorted(self.__lista)
        return self.__lista[0]
    #fimdef

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        self.__lista=sorted(self.__lista)
        return (self.__lista[-1])
    #fimdef
    
    def __str__(self):
        '''
        This method returns a string representation of the object.
        '''
        #return f"DataFruta: lista nomes={', '.join(self.__lista)}"
        return ', '.join(self.__lista)
    #fimdef
    
    def listarEmOrdem(self):
        self.__lista=sorted(self.__lista)
        return str(self)
    #fimdef
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        qtd_datas = int(input("Digite o quantidade de datas "))
        for item in range(qtd_datas):
            #dia = int(input("Digite dia: "))
            #mes = int(input("Digite mes: "))
            #ano = int(input("Digite ano: "))
            data_str = input("Digite a data (dd/mm/aaaa): ")
            dia, mes, ano = map(int, data_str.split('/'))
            self.__lista.append(Data(dia, mes, ano))
        #fimfor
    #fimdef
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        self.__lista=sorted(self.__lista)
        compr = len(self.__lista)
        if compr % 2 == 1:
            return str(self.__lista[compr // 2])
        else:
            return str(self.__lista[compr // 2 - 1])
        #fimse
    #fimdef
     
    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        self.__lista=sorted(self.__lista)
        return str(self.__lista[0])
    #fimdef
    
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        self.__lista=sorted(self.__lista)
        return str(self.__lista[-1])
    #fimdef
    def __str__(self):
        '''
        This method returns a string representation of the object.
        '''
        #Data.__str__
        return f"DataFruta: lista Data={', '.join(str(data) for data in self.__lista)}"
    #fimdef
    def listarEmOrdem(self):
        self.__lista = sorted(self.__lista)#, key=lambda data: (data.dia, data.mes, data.ano))
        #return '\n'.join(str(data) for data in self.__lista)
        return str(self)
    #fimdef
	
class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        qtd_salarios = int(input("Digite o quantidade de salarios: "))
        for item in range(qtd_salarios):
            salario = input("Digite salario: ")
            self.__lista.append(salario)
            #self.__lista=sorted(self.__lista)
        return self.__lista
    #fimdef

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        self.__lista=sorted(self.__lista)
        compr = len(self.__lista)
        if compr % 2 == 1:
            return self.__lista[compr // 2] #arredonda pra baixo
        else:
            return (self.__lista[compr / 2]+self.__lista[compr / 2 - 1])/2
        #fimse
    #fimdef 

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        self.__lista=sorted(self.__lista)
        return self.__lista[0]

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        self.__lista=sorted(self.__lista)
        return (self.__lista[-1])
    
    def __str__(self):
        '''
        This method returns a string representation of the object.
        '''
        #return f"DataFruta: lista salario={', '.join(self.__lista)}"
        return ', '.join(self.__lista)

    #fimdef
    def listarEmOrdem(self):
        self.__lista=sorted(self.__lista)
        return str(self)
    #fimdef
	
class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        qtd_idades = int(input("Digite o quantidade de idades "))
        for item in range(qtd_idades):
            idade = int(input("Digite idade: "))
            self.__lista.append(idade)
        #fimfor
    #fimdef    
    
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        self.__lista=sorted(self.__lista)
        compr = len(self.__lista)
        if compr % 2 == 1:
            return self.__lista[compr // 2] 
        else:
            return (self.__lista[compr / 2]+self.__lista[compr / 2 - 1])/2
        #fimse
    #fimdef
    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        self.__lista=sorted(self.__lista)
        return self.__lista[0]
    #fimdef
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        self.__lista=sorted(self.__lista)
        return (self.__lista[-1])
    #fimdef
    def __str__(self):
        '''
        This method returns a string representation of the object.
        '''
        return f"DataFruta: lista idade={', '.join(str(data) for data in self.__lista)}"
    #fimdef
    def listarEmOrdem(self):
        self.__lista=sorted(self.__lista)
        return str(self)
    #fimdef
	
#fim class ListaIdades
def reajustar_salario(salario):
    return salario * 1.1  # 10% de aumento
#fimdef

'''
import unittest

class TestMostraMediana(unittest.TestCase):
    def test_odd_length(self):
        elements = [1, 3, 2, 5, 4]
        expected_median = 3
        self.assertEqual(mostraMediana(elements), expected_median)

    def test_even_length(self):
        elements = [1, 3, 2, 5, 4, 6]
        expected_median = 3
        self.assertEqual(mostraMediana(elements), expected_median)
    
    def test_empty_list(self):
        elements = []
        self.assertRaises(IndexError, mostraMediana, elements)
    
if __name__ == '__main__':
    unittest.main(ListaNomes)
'''
def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    #listaListas = [nomes, datas, salarios, idades]
    listaListas = [nomes, salarios]#, idades]
  
    for lista in listaListas:
        lista.entradaDeDados()
        #if("__main__.ListaNomes" == str(type(lista))):
         #   print("Lista de nomes")
        #print("type(lista): " + str(type(lista)))
        #print("lista: " + str(lista))
        #print("__name__: " + str(__name__))
        lista.mostraMediana()
        #print("Mediana: " + str(lista.mostraMediana()))
        lista.mostraMenor()
        #print("Menor: " + str(lista.mostraMenor()))
        lista.mostraMaior()
        #print("Maior: " + (lista.mostraMaior()))
        print(lista.listarEmOrdem())
        
        
        print("___________________")

    #print(((ListaNomes.listarEmOrdem(nomes))))
    lista_nomes=str(nomes).split(', ');
    #lista_salarios = [float(salario) for salario in lista_salarios]
    lista_salarios=str(salarios).split(', ');
    lista_salarios = [float(salario) for salario in lista_salarios]
    #lista_salarios = [float(salario) for salario in str(salarios).split(',')]
    #print(lista_salarios)
    zipped=zip(lista_nomes, lista_salarios)
    print((list(zipped)))
    #print("Zipped:"+str(Utils.zipped))
    custo_folha = sum(map(reajustar_salario, lista_salarios))
    print("Custo da folha: " + str(custo_folha))

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
