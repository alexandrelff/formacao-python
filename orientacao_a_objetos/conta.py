
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo total de R${} do titular {}".format(self.__saldo, self.__titular))
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, saque):
        valor_disponivel = self.__saldo + self.__limite
        return saque <= valor_disponivel

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor R${} passou do limite.".format(valor))
    
    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    
    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB":"001", "Caixa":"104","Bradesco":"237"}



conta = Conta(123, "Alexandre", 100, 1000)
conta2 = Conta(321, "Cacilda", 500, 2000)


