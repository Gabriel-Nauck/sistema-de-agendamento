class GerenciadorConsultorios:
    def __init__(self):
        self.consultorios = []

    def validar_telefone(self, telefone):
        return telefone.isdigit() and len(telefone) >= 10

    def validar_cnpj(self, cnpj):
        return cnpj.isdigit() and len(cnpj) == 14

    def validar_numero_salas(self, numero):
        return numero.isdigit() and int(numero) > 0

    def cadastrar_consultorio(self):
        print("\n--- Cadastro de Novo Consultório ---")
        
        nome = input("Nome do consultório: ").strip()
        if any(cons['nome_consultorio'] == nome for cons in self.consultorios):
            print("Consultório já cadastrado.")
            return

        endereco = input("Endereço: ").strip()
        
        telefone = input("Telefone principal: ").strip()
        while not self.validar_telefone(telefone):
            print("Telefone inválido. Digite apenas números com DDD.")
            telefone = input("Telefone principal: ").strip()
        
        cnpj = input("CNPJ (apenas números): ").strip()
        while not self.validar_cnpj(cnpj):
            print("CNPJ inválido. Deve conter 14 dígitos numéricos.")
            cnpj = input("CNPJ (apenas números): ").strip()
        
        if any(cons['cnpj'] == cnpj for cons in self.consultorios):
            print("CNPJ já cadastrado para outro consultório.")
            return

        responsavel = input("Responsável técnico: ").strip()
        
        salas = input("Número de salas: ").strip()
        while not self.validar_numero_salas(salas):
            print("Número inválido. Digite um número positivo.")
            salas = input("Número de salas: ").strip()

        consultorio = {
            'nome_consultorio': nome,
            'endereco_consultorio': endereco,
            'telefone_principal': telefone,
            'cnpj': cnpj,
            'responsavel_tecnico': responsavel,
            'numero_salas': int(salas)
        }

        self.consultorios.append(consultorio)
        print("\nConsultório cadastrado com sucesso!")

    def listar_consultorios(self):
        print("\n--- Lista de Consultórios ---")
        if not self.consultorios:
            print("Nenhum consultório cadastrado.")
            return

        for i, cons in enumerate(self.consultorios, 1):
            print(f"\nConsultório {i}:")
            print(f"Nome: {cons['nome_consultorio']}")
            print(f"Endereço: {cons['endereco_consultorio']}")
            print(f"Telefone: {cons['telefone_principal']}")
            print(f"CNPJ: {cons['cnpj']}")
            print(f"Responsável técnico: {cons['responsavel_tecnico']}")
            print(f"Número de salas: {cons['numero_salas']}")

    def buscar_consultorio(self, cnpj):
        for cons in self.consultorios:
            if cons['cnpj'] == cnpj:
                return cons
        return None

    def editar_consultorio(self):
        print("\n--- Editar Consultório ---")
        cnpj = input("Digite o CNPJ do consultório que deseja editar: ").strip()
        consultorio = self.buscar_consultorio(cnpj)

        if not consultorio:
            print("Consultório não encontrado.")
            return

        novo_nome = input(f"Nome atual: {consultorio['nome_consultorio']}\nNovo nome: ").strip()
        if novo_nome:
            consultorio['nome_consultorio'] = novo_nome

        novo_endereco = input(f"Endereço atual: {consultorio['endereco_consultorio']}\nNovo endereço: ").strip()
        if novo_endereco:
            consultorio['endereco_consultorio'] = novo_endereco

        novo_telefone = input(f"Telefone atual: {consultorio['telefone_principal']}\nNovo telefone: ").strip()
        if novo_telefone:
            while not self.validar_telefone(novo_telefone):
                print("Telefone inválido. Digite apenas números com DDD.")
                novo_telefone = input("Novo telefone: ").strip()
            consultorio['telefone_principal'] = novo_telefone

        novo_responsavel = input(f"Responsável atual: {consultorio['responsavel_tecnico']}\nNovo responsável: ").strip()
        if novo_responsavel:
            consultorio['responsavel_tecnico'] = novo_responsavel

        novas_salas = input(f"Salas atuais: {consultorio['numero_salas']}\nNovo número de salas: ").strip()
        if novas_salas:
            while not self.validar_numero_salas(novas_salas):
                print("Número inválido. Digite um número positivo.")
                novas_salas = input("Novo número de salas: ").strip()
            consultorio['numero_salas'] = int(novas_salas)

        print("\nConsultório atualizado com sucesso!")

    def excluir_consultorio(self):
        print("\n--- Excluir Consultório ---")
        cnpj = input("Digite o CNPJ do consultório que deseja excluir: ").strip()

        for i, cons in enumerate(self.consultorios):
            if cons['cnpj'] == cnpj:
                confirmacao = input(f"Tem certeza que deseja excluir {cons['nome_consultorio']}? (S/N): ").strip().upper()
                if confirmacao == 'S':
                    del self.consultorios[i]
                    print("Consultório excluído com sucesso.")
                return

        print("Consultório não encontrado.")

def menu():
    gerenciador = GerenciadorConsultorios()

    while True:
        print("\n--- Sistema de Gerenciamento de Consultórios ---")
        print("1. Cadastrar novo consultório")
        print("2. Listar todos os consultórios")
        print("3. Editar consultório")
        print("4. Excluir consultório")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            gerenciador.cadastrar_consultorio()
        elif opcao == '2':
            gerenciador.listar_consultorios()
        elif opcao == '3':
            gerenciador.editar_consultorio()
        elif opcao == '4':
            gerenciador.excluir_consultorio()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    menu()
