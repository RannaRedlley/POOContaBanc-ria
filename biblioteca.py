class ContaBancaria:
    def _init_(self,numero,nome,tipo):
        self.numero = numero
        self.saldo = 0
        self.nome = nome
        self.tipo = tipo
        self.status = False
        self.limite =0
        self.AtivarConta = False
        self.DesativarConta = False

    def sacar(self,saque):
        if self.StatusConta ==True:
          if saque > 0 and saque <= self.saldo + self.limite:
                    self.limite = self.saldo - (saque - self.limite)
                    self.saldo = self.saldo - saque
                    print(f"Seu saque de R${saque} foi concluido com sucesso.")
          elif saque > self.limite:
                print(f"Seu limite é de : R${self.limite}.")
          else:
                print("Você não possui saldo suficiente.")
        else:
            print("Conta desativada, impossível sacar.")

    def Depositar(self, deposito):
        if self.status == True:
            if deposito > 0:
                self.saldo += deposito
                print(f"Foi realizado um depósito de R${deposito}. Seu Saldo atual é de R${self.saldo}")
            else:
                print(f"Valor inválido.")
        else:
            print("Conta desativada")

    def AtivarConta(self):
        if self.ativar == False:
            self.ativar = True
            self.status = True
            print("Conta ativada com sucesso!")
        else:
            print("A conta já está ativada.")

    def DesativarConta(self):
        if self.saldo_conta > 0:
            print("Impossível desativar conta com saldo positivo.")
        elif self.status_conta == True:
            self.ativar = False
            self.status_conta = False
            self.desativar = True
            print("Conta desativada!")
        else:
            print("A conta já está desativada.")

    def verificarSaldo(self):
        print(f"O saldo de sua conta é de: R${self.saldo}\nLimite R$:{self.limite}")

    def AtivarLimite(self, valor):
        self.limite = valor
        print(f"Seu crétido especial é de R$: {self.limite}")

    def DesativarLimite(self):
        self.limite = 0
        print(f"Seu crétido especial é de R$: {self.limite}")