class GerenciadorPlanosSaude:
    def __init__(self):
        self.planos = []

    def validar_codigo_ans(self, codigo):
        return codigo.isdigit() and len(codigo) == 6

    def validar_cobertura(self, percentual):
        try:
            return 0 <= float(percentual) <= 100
        except ValueError:
            return False

    def cadastrar_plano(self):
        print("\n--- Cadastro de Novo Plano de Saúde ---")
        
        nome = input("Nome do plano: ").strip()
        operadora = input("Operadora: ").strip()
        tipo = input("Tipo do plano: ").strip()
        
        codigo = input("Código ANS (6 dígitos): ").strip()
        while not self.validar_codigo_ans(codigo):
            print("Código inválido. Deve conter 6 dígitos numéricos.")
            codigo = input("Código ANS (6 dígitos): ").strip()
        
        if any(p['codigo_ans'] == codigo for p in self.planos):
            print("Código ANS já cadastrado para outro plano.")
            return

        contato = input("Contato da operadora: ").strip()
        categoria = input("Categoria do plano: ").strip()
        
        cobertura = input("Cobertura percentual (0-100%): ").strip()
        while not self.validar_cobertura(cobertura):
            print("Percentual inválido. Digite um valor entre 0 e 100.")
            cobertura = input("Cobertura percentual (0-100%): ").strip()

        plano = {
            'nome_plano': nome,
            'operadora': operadora,
            'tipo_plano': tipo,
            'codigo_ans': codigo,
            'contato_operadora': contato,
            'categoria_plano': categoria,
            'cobertura_percentual': float(cobertura)
        }

        self.planos.append(plano)
        print("\nPlano de saúde cadastrado com sucesso!")

    def listar_planos(self):
        print("\n--- Lista de Planos de Saúde ---")
        if not self.planos:
            print("Nenhum plano cadastrado.")
            return

        for i, plano in enumerate(self.planos, 1):
            print(f"\nPlano {i}:")
            print(f"Nome: {plano['nome_plano']}")
            print(f"Operadora: {plano['operadora']}")
            print(f"Tipo: {plano['tipo_plano']}")
            print(f"Código ANS: {plano['codigo_ans']}")
            print(f"Contato: {plano['contato_operadora']}")
            print(f"Categoria: {plano['categoria_plano']}")
            print(f"Cobertura: {plano['cobertura_percentual']}%")

    def buscar_plano(self, codigo):
        for plano in self.planos:
            if plano['codigo_ans'] == codigo:
                return plano
        return None

    def editar_plano(self):
        print("\n--- Editar Plano de Saúde ---")
        codigo = input("Digite o código ANS do plano que deseja editar: ").strip()
        plano = self.buscar_plano(codigo)

        if not plano:
            print("Plano não encontrado.")
            return

        novo_nome = input(f"Nome atual: {plano['nome_plano']}\nNovo nome: ").strip()
        if novo_nome:
            plano['nome_plano'] = novo_nome

        nova_operadora = input(f"Operadora atual: {plano['operadora']}\nNova operadora: ").strip()
        if nova_operadora:
            plano['operadora'] = nova_operadora

        novo_tipo = input(f"Tipo atual: {plano['tipo_plano']}\nNovo tipo: ").strip()
        if novo_tipo:
            plano['tipo_plano'] = novo_tipo

        novo_contato = input(f"Contato atual: {plano['contato_operadora']}\nNovo contato: ").strip()
        if novo_contato:
            plano['contato_operadora'] = novo_contato

        nova_categoria = input(f"Categoria atual: {plano['categoria_plano']}\nNova categoria: ").strip()
        if nova_categoria:
            plano['categoria_plano'] = nova_categoria

        nova_cobertura = input(f"Cobertura atual: {plano['cobertura_percentual']}%\nNova cobertura (0-100%): ").strip()
        if nova_cobertura:
            while not self.validar_cobertura(nova_cobertura):
                print("Percentual inválido. Digite um valor entre 0 e 100.")
                nova_cobertura = input("Nova cobertura (0-100%): ").strip()
            plano['cobertura_percentual'] = float(nova_cobertura)

        print("\nPlano atualizado com sucesso!")

    def excluir_plano(self):
        print("\n--- Excluir Plano de Saúde ---")
        codigo = input("Digite o código ANS do plano que deseja excluir: ").strip()

        for i, plano in enumerate(self.planos):
            if plano['codigo_ans'] == codigo:
                confirmacao = input(f"Tem certeza que deseja excluir {plano['nome_plano']}? (S/N): ").strip().upper()
                if confirmacao == 'S':
                    del self.planos[i]
                    print("Plano excluído com sucesso.")
                return

        print("Plano não encontrado.")

def menu():
    gerenciador = GerenciadorPlanosSaude()

    while True:
        print("\n--- Sistema de Gerenciamento de Planos de Saúde ---")
        print("1. Cadastrar novo plano")
        print("2. Listar todos os planos")
        print("3. Editar plano")
        print("4. Excluir plano")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            gerenciador.cadastrar_plano()
        elif opcao == '2':
            gerenciador.listar_planos()
        elif opcao == '3':
            gerenciador.editar_plano()
        elif opcao == '4':
            gerenciador.excluir_plano()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    menu()
