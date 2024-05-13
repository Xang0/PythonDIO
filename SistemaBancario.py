class noh:
      def __init__(self, operacao, valor):
            self.operacao = operacao
            self.valor = valor
            self.proximo = None

class HistoricoExtrato:
      def __init__(self) -> None:
          self.primeiro = None
          self.ultimo = None
          self.tamanho = 0

      def adicionar(self, operacao, valor):
            novo = noh(operacao, valor)
            if self.primeiro == None:
                  self.primeiro = novo
            else:
                  self.ultimo.proximo = novo

            self.ultimo = novo
            self.tamanho+=1

      def retirar(self):
            if self.primeiro != None:
                  aux = self.primeiro
                  self.primeiro = self.primeiro.proximo
                  self.tamanho-=1
                  return aux
          
      def imprimir(self):
            if self.primeiro == None:
                  print("Nenhuma operação feita ainda.")
            else:
                  for cont in range(0, self.tamanho):
                        aux = self.retirar()
                        print(f"""Operação: {aux.operacao}
Valor: {aux.valor}
""")
                        self.adicionar(aux.operacao, aux.valor)
                        cont+=1

class Conta:
      def __init__(self):
            self.saldo = 0
            self.extrato = HistoricoExtrato()

      def depositar(self, valor):
            self.saldo += valor
            self.extrato.adicionar("Depósito", valor)
            return True
      
      def saque(self, valor):
            if self.saldo >= valor:
                  if valor > 500:
                        print("""Valor máximo para saque é de R$ 500,00.
                              Por favor, realize um segundo saque com para o resto do valor requisitado.
                              """)
                        self.saldo -= 500
                        self.extrato.adicionar("Saque", 500)
                  else:
                        self.saldo -= valor
                        self.extrato.adicionar("Saque", valor)
                  return True
            else:
                  print("Saldo insuficiente.")
                  return False
            
      def verExtrato(self):
            print("Historico de operações:")
            self.extrato.imprimir()
            print(f"Saldo atual: R$ {self.saldo}")

conta = Conta()       
print('''Escolha entre aluma das operações bancárias:
      1 - Depositar
      2 - Sacar
      3 - Ver Extrato
      4 - Sair''')

opcao = int(input("Opção escolhida: "))
print("")

while opcao != 4:
      if opcao == 1:
            if conta.depositar(float(input("Valor a ser depositado: "))):
                  print("Depósito realizado com sucesso.")
                  print("")

      elif opcao == 2:
            if conta.saque(float(input("Valor do saque: "))):
                  print("Saque realizado com sucesso.")
                  print("")
            else:
                  print("Erro ao realizar o saque.")
                  print("")

      elif opcao == 3:
            conta.verExtrato()
            
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