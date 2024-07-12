from random import randint

class Conta:
      def __init__(self, nome, cpf):
            self.nome = nome
            self.cpf = cpf
            self.contaCorrente = None

      def criarConta(self):
            self.contaCorrente = ContaCorrente(self.cpf)

class ContaCorrente:
      def __init__(self, cpf):
            self.numeroConta = randint(1000, 9999)
            self.titular = cpf
            self.saldo = 0
            self.extrato = list()

      def getNumeroConta(self): return self.numeroConta

      def adicionar(self, operacao, valor):
            self.extrato.append((operacao, valor))

      def imprimir(self, tipo):
            if tipo == "completo":
                  for operacao, valor in self.extrato:
                        print(f"""Operação: {operacao}
                              |Valor da operação: R$ {valor}
                              |---------------------------------""")
            if tipo == "deposito":
                  for operacao, valor in self.extrato:
                        if operacao == "Depósito":
                              print(f"""Operação: {operacao}
                                    |Valor da operação: R$ {valor}
                                    |---------------------------------""")
            if tipo == "saque":
                  for operacao, valor in self.extrato:
                        if operacao == "Saque":
                              print(f"""Operação: {operacao}
                                    |Valor da operação: R$ {valor}
                                    |---------------------------------""")

      def depositar(self,valor,/):
            self.saldo += valor
            self.adicionar("Depósito", valor)
            return True
      
      def saque(self,*,valor):
            if self.saldo >= valor:
                  if valor > 500:
                        print("""Valor máximo para saque é de R$ 500,00.
Por favor, realize um segundo saque com para o resto do valor requisitado.
""")
                        self.saldo -= 500
                        self.adicionar("Saque", 500)
                  else:
                        self.saldo -= valor
                        self.adicionar("Saque", valor)
                  return True
            else:
                  print("Saldo insuficiente.")
                  return False
            
      def verExtrato(self, tipo="completo"):
            print("Historico de operações:")
            print("")
            self.imprimir(tipo)
            print(f"Saldo atual: R$ {self.saldo}")
            print("")


dicionarioContas = {}

print('''\nEscolha entre alguma das operações:
      1 - Criar Usuário
      2 - Criar Conta Corrente
      3 - Ir para as operações bancárias\n''')

opcao = int(input("Opção escolhida: "))
print("")

while opcao != 3:
      if opcao == 1:
            nome = input("Nome: ")
            cpf = input("CPF: ")
            conta = Conta(nome, cpf)
            dicionarioContas[cpf] = conta

      elif opcao == 2:
            inputCpf = input("Digite o CPF do usuário: ")
            if dicionarioContas.get(inputCpf) == None:
                  print("CPF não encontrado.\nPor favor, crie um usuário primeiro.\n")
            else:
                  conta = dicionarioContas[inputCpf]
                  conta.criarConta()
                  print(f"Conta corrente de numero {conta.contaCorrente.getNumeroConta()} criada com sucesso.\n")

      else:
            print("Opção inválida.\n")

      if (opcao != 3):
            print('''Escolha entre alguma das operações:
            1 - Criar Usuário
            2 - Criar Conta Corrente
            3 - Ir para as operações bancárias\n''')
            opcao = int(input("Opção escolhida: "))
            print("\n")


cpf_conta = input("Digite o CPF do usuário da conta: ")
print("")
if dicionarioContas.get(cpf_conta) == None:
      print("CPF não encontrado.")
      print("Por favor, crie um usuário primeiro ou digite outro CPF.")
      print("")
else:
      conta = dicionarioContas[cpf_conta].contaCorrente


print('''\nEscolha entre aluma das operações bancárias:
      1 - Depositar
      2 - Sacar
      3 - Ver Extrato
      4 - Sair\n''')

opcao = int(input("Opção escolhida: "))
print("")

while opcao != 4:
      if opcao == 1:
            if conta.depositar(float(input("Valor a ser depositado: "))):
                  print("Depósito realizado com sucesso.")
                  print(f"Saldo atual: R$ {conta.saldo}")
                  print("")

      elif opcao == 2:
            if conta.saque(valor=float(input("Valor do saque: "))):
                  print("Saque realizado com sucesso.")
                  print(f"Saldo atual: R$ {conta.saldo}")
                  print("")
            else:
                  print("Erro ao realizar o saque.")
                  print("")

      elif opcao == 3:
            if input("Deseja ver o extrato completo? (S/N): ").upper() == "S":
                  conta.verExtrato()
            else:
                  if input("Deseja ver o extrato de depósitos? (S/N): ").upper() == "S":
                        conta.verExtrato(tipo="deposito")
                  else:
                        conta.verExtrato(tipo="saque")
            
      else:
            print("Opção inválida.")
            print("")

      if (opcao != 4):
            print('''Escolha entre aluma das operações bancárias:
            1 - Depositar
            2 - Sacar
            3 - Ver Extrato
            4 - Sair''')
            opcao = int(input("Opção escolhida: "))
            print("")

print("Encerrando o programa.")
print("")