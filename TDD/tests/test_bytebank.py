import pytest
from pytest import mark
from TDD.codigo.bytebank import Funcionario

class TestClass:
    def  test_quando_idade_recebe_05_03_2002_deve_retornar_21(self):   #para o pytest agir, o nome tem que começar com test
        #given-when-then

        #given - contexto
        entrada = "05/03/2002"
        esperado = 21

        funcionario_teste = Funcionario("Teste", entrada, 1111)

        #when-ação
        resultado = funcionario_teste.idade()

        # then-desfecho
        assert resultado == esperado


    def test_quando_sobrenome_recebe_Isabelle_Coimbra_deve_retornar_apenas_Coimbra(self):
        entrada = "Isabelle Coimbra"  #given
        esperado = "Coimbra"

        isabelle = Funcionario(entrada, "05/03/2002", 1111)
        resultado = isabelle.sobrenome() #when

        assert resultado == esperado

    @mark.skip
    def test_quando_descrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 #given
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, "11/11/2000", entrada_salario)

        funcionario_teste.decrescimo_salario()  #when
        resultado = funcionario_teste.salario

        assert resultado == esperado   #then

    #@mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000  # given
        esperado = 100

        funcionario_teste = Funcionario("teste", "11/11/2000", entrada)
        resultado = funcionario_teste.calcular_bonus() #when

        assert resultado == esperado  # then


    def test_quando_calcular_bonus_recebe_10000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000  # given

            funcionario_teste = Funcionario("teste", "11/11/2000", entrada)
            resultado = funcionario_teste.calcular_bonus()  # when

            assert resultado  # then


    def test_retorno_str(self):
        nome, data_nascimento, salario = "Teste", "12/04/1999", 1000  # given
        esperado = 'Funcionario(Teste, 12/04/1999, 1000)'

        funcionario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funcionario_teste.__str__() #when

        assert resultado == esperado  # then













