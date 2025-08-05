class GerenciadorExames:
    def __init__(self):
        self.exames = []

    def validar_data(self, data):
        try:
            from datetime import datetime
            datetime.strptime(data, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def validar_urgencia(self, nivel):
        return nivel.isdigit() and 1 <= int(nivel) <= 5

    def validar_custo(self, valor):
        try:
            return float(valor) >= 0
        except ValueError:
            return False

    def cadastrar_exame(self):
        print("\n--- Cadastro de Novo Exame ---")
        
        nome = input("Nome do exame: ").strip()
        tipo = input("Tipo do exame: ").strip()
        
        data = input("Data de solicitação (DD/MM/AAAA): ").strip()
        while not self.validar_data(data):
            print("Data inválida. Use o formato DD/MM/AAAA.")
            data = input("Data de solicitação (DD/MM/AAAA): ").strip()
        
        laboratorio = input("Laboratório responsável: ").strip()
        resultado = input("Resultado do exame: ").strip()
        
        urgencia = input("Nível de urgência (1-5): ").strip()
        while not self.validar_urgencia(urgencia):
            print("Nível inválido. Digite um número entre 1 e 5.")
            urgencia = input("Nível de urgência (1-5): ").strip()
        
        custo = input("Custo do exame: R$ ").strip()
        while not self.validar_custo(custo):
            print("Valor inválido. Digite um número positivo.")
            custo = input("Custo do exame: R$ ").strip()

        exame = {
            'nome_exame': nome,
            'tipo_exame': tipo,
            'data_solicitacao': data,
            'laboratorio_responsavel': laboratorio,
            'resultado_exame': resultado,
            'urgencia_nivel': int(urgencia),
            'custo_exame': float(custo)
        }

        self.exames.append(exame)
        print("\nExame cadastrado com sucesso!")

    def listar_exames(self):
        print("\n--- Lista de Exames ---")
        if not self.exames:
            print("Nenhum exame cadastrado.")
            return

        for i, exame in enumerate(self.exames, 1):
            print(f"\nExame {i}:")
            print(f"Nome: {exame['nome_exame']}")
            print(f"Tipo: {exame['tipo_exame']}")
            print(f"Data solicitação: {exame['data_solicitacao']}")
            print(f"Laboratório: {exame['laboratorio_responsavel']}")
            print(f"Resultado: {exame['resultado_exame']}")
            print(f"Urgência: {exame['urgencia_nivel']}/5")
            print(f"Custo: R$ {exame['custo_exame']:.2f}")

    def buscar_exame(self, nome):
        for exame in self.exames:
            if exame['nome_exame'].lower() == nome.lower():
                return exame
        return None

    def editar_exame(self):
        print("\n--- Editar Exame ---")
        nome = input("Digite o nome do exame que deseja editar: ").strip()
        exame = self.buscar_exame(nome)

        if not exame:
            print("Exame não encontrado.")
            return

        novo_tipo = input(f"Tipo atual: {exame['tipo_exame']}\nNovo tipo: ").strip()
        if novo_tipo:
            exame['tipo_exame'] = novo_tipo

        nova_data = input(f"Data atual: {exame['data_solicitacao']}\nNova data (DD/MM/AAAA): ").strip()
        if nova_data:
            while not self.validar_data(nova_data):
                print("Data inválida. Use o formato DD/MM/AAAA.")
                nova_data = input("Nova data (DD/MM/AAAA): ").strip()
            exame['data_solicitacao'] = nova_data

        novo_lab = input(f"Laboratório atual: {exame['laboratorio_responsavel']}\nNovo laboratório: ").strip()
        if novo_lab:
            exame['laboratorio_responsavel'] = novo_lab

        novo_resultado = input(f"Resultado atual: {exame['resultado_exame']}\nNovo resultado: ").strip()
        if novo_resultado:
            exame['resultado_exame'] = novo_resultado

        nova_urgencia = input(f"Urgência atual: {exame['urgencia_nivel']}/5\nNova urgência (1-5): ").strip()
        if nova_urgencia:
            while not self.validar_urgencia(nova_urgencia):
                print("Nível inválido. Digite um número entre 1 e 5.")
                nova_urgencia = input("Nova urgência (1-5): ").strip()
            exame['urgencia_nivel'] = int(nova_urgencia)

        novo_custo = input(f"Custo atual: R$ {exame['custo_exame']:.2f}\nNovo custo: R$ ").strip()
        if novo_custo:
            while not self.validar_custo(novo_custo):
                print("Valor inválido. Digite um número positivo.")
                novo_custo = input("Novo custo: R$ ").strip()
            exame['custo_exame'] = float(novo_custo)

        print("\nExame atualizado com sucesso!")

    def excluir_exame(self):
        print("\n--- Excluir Exame ---")
        nome = input("Digite o nome do exame que deseja excluir: ").strip()

        for i, exame in enumerate(self.exames):
            if exame['nome_exame'].lower() == nome.lower():
                confirmacao = input(f"Tem certeza que deseja excluir {exame['nome_exame']}? (S/N): ").strip().upper()
                if confirmacao == 'S':
                    del self.exames[i]
                    print("Exame excluído com sucesso.")
                return

        print("Exame não encontrado.")

def menu():
    gerenciador = GerenciadorExames()

    while True:
        print("\n--- Sistema de Gerenciamento de Exames ---")
        print("1. Cadastrar novo exame")
        print("2. Listar todos os exames")
        print("3. Editar exame")
        print("4. Excluir exame")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            gerenciador.cadastrar_exame()
        elif opcao == '2':
            gerenciador.listar_exames()
        elif opcao == '3':
            gerenciador.editar_exame()
        elif opcao == '4':
            gerenciador.excluir_exame()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    menu()
