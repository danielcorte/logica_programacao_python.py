idade = int(input("Qual a sua idade: "))
if idade >= 60:
    print("-----------------------------------------------------------------------------------------\n"
          "|     BEBÊ     |    CRIANÇA    |   ADOLESCENTE  |     ADULTO    |        IDOSO           |\n"
          "| MENOR 2 ANOS | MENOR 13 ANOS | MENOR 18 ANOS  | MENOR 60 ANOS | MAIOR OU IGUAL 60 ANOS |\n"
          "|              |               |                |               |         ( X )          |\n"
          "-----------------------------------------------------------------------------------------")
elif idade >= 18:
    print("-----------------------------------------------------------------------------------------\n"
          "|     BEBÊ     |    CRIANÇA    |   ADOLESCENTE  |     ADULTO    |        IDOSO           |\n"
          "| MENOR 2 ANOS | MENOR 13 ANOS | MENOR 18 ANOS  | MENOR 60 ANOS | MAIOR OU IGUAL 60 ANOS |\n"
          "|              |               |                |     ( X )     |                        |\n"
          "-----------------------------------------------------------------------------------------")
elif idade >= 13:
    print("-----------------------------------------------------------------------------------------\n"
          "|     BEBÊ     |    CRIANÇA    |   ADOLESCENTE  |     ADULTO    |        IDOSO           |\n"
          "| MENOR 2 ANOS | MENOR 13 ANOS | MENOR 18 ANOS  | MENOR 60 ANOS | MAIOR OU IGUAL 60 ANOS |\n"
          "|              |               |     ( X )      |               |                        |\n"
          "-----------------------------------------------------------------------------------------")
elif idade >= 2:
    print("-----------------------------------------------------------------------------------------\n"
          "|     BEBÊ     |    CRIANÇA    |   ADOLESCENTE  |     ADULTO    |        IDOSO           |\n"
          "| MENOR 2 ANOS | MENOR 13 ANOS | MENOR 18 ANOS  | MENOR 60 ANOS | MAIOR OU IGUAL 60 ANOS |\n"
          "|              |     ( X )     |                |               |                        |\n"
          "-----------------------------------------------------------------------------------------")
elif idade >= 0:
    print("-----------------------------------------------------------------------------------------\n"
          "|     BEBÊ     |    CRIANÇA    |   ADOLESCENTE  |     ADULTO    |        IDOSO           |\n"
          "| MENOR 2 ANOS | MENOR 13 ANOS | MENOR 18 ANOS  | MENOR 60 ANOS | MAIOR OU IGUAL 60 ANOS |\n"
          "|    ( X )     |               |                |               |                        |\n"
          "-----------------------------------------------------------------------------------------")
else:
    print("-----------------------------------------------------------------------------------------\n"
          "|     BEBÊ     |    CRIANÇA    |   ADOLESCENTE  |     ADULTO    |        IDOSO           |\n"
          "| MENOR 2 ANOS | MENOR 13 ANOS | MENOR 18 ANOS  | MENOR 60 ANOS | MAIOR OU IGUAL 60 ANOS |\n"
          "|              |               |                |               |                        |\n"
          "-----------------------------------------------------------------------------------------\n"
          "                                  VALOR INCORRETO                                        ")

"""class Cadastro:
    def __init__(self):
        self.nome = ""
        self.idade = 0

    @staticmethod
    def getnome(self):
        nome = str(input("Digite o seu nome: "))
        self.nome = nome

    @staticmethod
    def getidade(self):
        idade = int(input("Digite a sua idade: "))
        self.idade = idade

    def cadastrar(self):
        self.getnome(self)
        self.getidade(self)
        print( f'Olá {self.nome}, fico feliz em saber que você tem {self.idade} anos!')

pessoa1 = Cadastro()
pessoa1.cadastrar()

pessoa2 = Cadastro()
pessoa2.cadastrar()

print(pessoa1.nome)
print(pessoa2.nome)"""

class Tabela:
    def __init__(self):
        self.idade = 0

    @staticmethod
    def getIdade(self):
        idade = int(input("Digite a sua idade: "))
        self.idade = idade

    @staticmethod
    def tabelaIdade(self):
        n1 = ''
        n2 = ''
        n3 = ''
        n4 = ''
        n5 = ''
        n6 = ''
        if idade >= 60:
            n1 = True
            return 'X'
        if idade >= 18:
            n2 = True
            return 'X'
        if idade >= 13:
            n3 = True
            return 'X'
        if idade >= 2:
            n4 = True
            return 'X'
        if idade >= 0:
            n5 = True
            return 'X'


        print(f"-----------------------------------------------------------------------------------------\n"
             f"|     BEBÊ     |    CRIANÇA    |   ADOLESCENTE  |     ADULTO    |        IDOSO           |\n"
             f"| MENOR 2 ANOS | MENOR 13 ANOS | MENOR 18 ANOS  | MENOR 60 ANOS | MAIOR OU IGUAL 60 ANOS |\n"
             f"|    ({n1})    |    ({n2})     |     ({n3})     |     ({n4})    |        ({n5})          |\n"
              "-------------------------------------------------------------------------------------------")

n1 = Tabela
n2 = Tabela.tabelaIdade()