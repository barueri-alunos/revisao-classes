# Para definir uma classe em Python é utilizado "class" e nome da classe.
# Todas as classes obrigatoriamente devem ter a primeira letra em maiúsculo.

class Pessoa:
    # A função __init__ é o construtor da classe. Construtor, em 
    # linguagens de programação orientadas a objeto é um método que chamamos
    # para criar uma nova instância do objeto. É a definição inicial dos atributos.
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    # imprimir_dados é um função (método)
    def imprimir_dados(self):
        print('Nome: ' + self.nome) 
        print('Idade: '+ self.idade)
        print('Genero: ' + self.genero)

# A classe Paciente é herdeira da classe Pessoa, uma vez que ao declarar
# a classe, definimos "class Paciente(Pessoa)".
class Paciente(Pessoa):
    def __init__(self, sintoma, nome, idade, genero):  #parametros necessários para a criação de um paciente
        super().__init__(nome, idade, genero)
        self.sintoma = sintoma

        # A função "super" é utilizada para acessar os atributos
        # e métodos da classe pai. Como precisamos chamar o construtor de
        # Pessoa no construtor de Paciente para definirmos os valores dos 
        # atributos "nome", "idade" e "genero", fazemos isso com o "super".

    def imprimir_sintoma(self):
        return print('Sintomas: ' + self.sintoma)

class Medico(Pessoa):
    def __init__(self, crm, nome, idade, genero):
        super().__init__(nome, idade, genero)
        self.crm = crm

    def imprimir_crm(self):
        return print( 'CRM: ' + self.crm)

#Chamando os métodos nas instâncias:
print('________PACIENTE_______')
paciente = Paciente('Gripe', 'Marcia', '23', 'F')
paciente.imprimir_dados()
paciente.imprimir_sintoma()

print('_________MEDICO______')
medico =  Medico('272671', 'Diane', '28', 'F')
medico.imprimir_crm()
medico.imprimir_dados()