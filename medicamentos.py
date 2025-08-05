class GerenciadorMedicamentos:
    def __init__(self):
        self.medicamentos = []

    def validar_codigo_anvisa(self, codigo):
        return codigo.isdigit() and len(codigo) == 13

    def validar_dosagem(self, dosagem):
        try:
            return float(dosagem) > 0
        except ValueError:
            return False

    def validar_quantidade(self, quantidade):
        return quantidade.isdigit() and int(quantidade) >= 0

    def validar_preco(self, preco):
        try:
            return float(preco) > 0
        except ValueError:
            return False

    def cadastrar_medicamento(self):
        print("\n--- Cadastro de Novo Medicamento ---")
        
        nome = input("Nome do medicamento: ").strip()
        if any(med['nome_medicamento'].lower() == nome.lower() for med in self.medicamentos):
            print("Medicamento já cadastrado.")
            return

        principio = input("Princípio ativo: ").strip()
        
        dosagem = input("Dosagem prescrita (mg/ml): ").strip()
        while not self.validar_dosagem(dosagem):
            print("Dosagem inválida. Digite um número positivo.")
            dosagem = input("Dosagem prescrita (mg/ml): ").strip()
        
        fabricante = input("Fabricante: ").strip()
        
        codigo = input("Código ANVISA (13 dígitos): ").strip()
        while not self.validar_codigo_anvisa(codigo):
            print("Código inválido. Deve conter 13 dígitos numéricos.")
            codigo = input("Código ANVISA (13 dígitos): ").strip()
        
        if any(med['codigo_anvisa'] == codigo for med in self.medicamentos):
            print("Código ANVISA já cadastrado para outro medicamento.")
            return

        quantidade = input("Quantidade em estoque: ").strip()
        while not self.validar_quantidade(quantidade):
            print("Quantidade inválida. Digite um número inteiro positivo.")
            quantidade = input("Quantidade em estoque: ").strip()
        
        preco = input("Preço unitário: R$ ").strip()
        while not self.validar_preco(preco):
            print("Preço inválido. Digite um número positivo.")
            preco = input("Preço unitário: R$ ").strip()

        medicamento = {
            'nome_medicamento': nome,
            'principio_ativo': principio,
            'dosagem_prescrita': float(dosagem),
            'fabricante': fabricante,
            'codigo_anvisa': codigo,
            'quantidade_estoque': int(quantidade),
            'preco_unitario': float(preco)
        }

        self.medicamentos.append(medicamento)
        print("\nMedicamento cadastrado com sucesso!")

    def listar_medicamentos(self):
        print("\n--- Lista de Medicamentos ---")
        if not self.medicamentos:
            print("Nenhum medicamento cadastrado.")
            return

        for i, med in enumerate(self.medicamentos, 1):
            print(f"\nMedicamento {i}:")
            print(f"Nome: {med['nome_medicamento']}")
            print(f"Princípio ativo: {med['principio_ativo']}")
            print(f"Dosagem: {med['dosagem_prescrita']} mg/ml")
            print(f"Fabricante: {med['fabricante']}")
            print(f"Código ANVISA: {med['codigo_anvisa']}")
            print(f"Estoque: {med['quantidade_estoque']} unidades")
            print(f"Preço: R$ {med['preco_unitario']:.2f}")

    def buscar_medicamento(self, codigo):
        for med in self.medicamentos:
            if med['codigo_anvisa'] == codigo:
                return med
        return None

    def editar_medicamento(self):
        print("\n--- Editar Medicamento ---")
        codigo = input("Digite o código ANVISA do medicamento que deseja editar: ").strip()
        medicamento = self.buscar_medicamento(codigo)

        if not medicamento:
            print("Medicamento não encontrado.")
            return

        novo_nome = input(f"Nome atual: {medicamento['nome_medicamento']}\nNovo nome: ").strip()
        if novo_nome:
            medicamento['nome_medicamento'] = novo_nome

        novo_principio = input(f"Princípio ativo atual: {medicamento['principio_ativo']}\nNovo princípio: ").strip()
        if novo_principio:
            medicamento['principio_ativo'] = novo_principio

        nova_dosagem = input(f"Dosagem atual: {medicamento['dosagem_prescrita']} mg/ml\nNova dosagem: ").strip()
        if nova_dosagem:
            while not self.validar_dosagem(nova_dosagem):
                print("Dosagem inválida. Digite um número positivo.")
                nova_dosagem = input("Nova dosagem (mg/ml): ").strip()
            medicamento['dosagem_prescrita'] = float(nova_dosagem)

        novo_fabricante = input(f"Fabricante atual: {medicamento['fabricante']}\nNovo fabricante: ").strip()
        if novo_fabricante:
            medicamento['fabricante'] = novo_fabricante

        nova_quantidade = input(f"Estoque atual: {medicamento['quantidade_estoque']}\nNova quantidade: ").strip()
        if nova_quantidade:
            while not self.validar_quantidade(nova_quantidade):
                print("Quantidade inválida. Digite um número inteiro positivo.")
                nova_quantidade = input("Nova quantidade: ").strip()
            medicamento['quantidade_estoque'] = int(nova_quantidade)

        novo_preco = input(f"Preço atual: R$ {medicamento['preco_unitario']:.2f}\nNovo preço: R$ ").strip()
        if novo_preco:
            while not self.validar_preco(novo_preco):
                print("Preço inválido. Digite um número positivo.")
                novo_preco = input("Novo preço: R$ ").strip()
            medicamento['preco_unitario'] = float(novo_preco)

        print("\nMedicamento atualizado com sucesso!")

    def excluir_medicamento(self):
        print("\n--- Excluir Medicamento ---")
        codigo = input("Digite o código ANVISA do medicamento que deseja excluir: ").strip()

        for i, med in enumerate(self.medicamentos):
            if med['codigo_anvisa'] == codigo:
                confirmacao = input(f"Tem certeza que deseja excluir {med['nome_medicamento']}? (S/N): ").strip().upper()
                if confirmacao == 'S':
                    del self.medicamentos[i]
                    print("Medicamento excluído com sucesso.")
                return

        print("Medicamento não encontrado.")

def menu():
    gerenciador = GerenciadorMedicamentos()

    while True:
        print("\n--- Sistema de Gerenciamento de Medicamentos ---")
        print("1. Cadastrar novo medicamento")
        print("2. Listar todos os medicamentos")
        print("3. Editar medicamento")
        print("4. Excluir medicamento")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            gerenciador.cadastrar_medicamento()
        elif opcao == '2':
            gerenciador.listar_medicamentos()
        elif opcao == '3':
            gerenciador.editar_medicamento()
        elif opcao == '4':
            gerenciador.excluir_medicamento()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    menu()
