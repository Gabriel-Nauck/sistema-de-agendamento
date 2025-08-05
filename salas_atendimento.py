class GerenciadorSalas:
    def __init__(self):
        self.salas = []

    def validar_capacidade(self, capacidade):
        return capacidade.isdigit() and int(capacidade) > 0

    def cadastrar_sala(self):
        print("\n--- Cadastro de Nova Sala ---")
        
        nome = input("Nome da sala: ").strip()
        if any(s['nome_sala'] == nome for s in self.salas):
            print("Sala já cadastrada.")
            return

        tipo = input("Tipo de sala: ").strip()
        equipamentos = input("Equipamentos disponíveis: ").strip()
        localizacao = input("Localização: ").strip()
        observacoes = input("Observações: ").strip()
        
        capacidade = input("Capacidade de pessoas: ").strip()
        while not self.validar_capacidade(capacidade):
            print("Capacidade inválida. Digite um número positivo.")
            capacidade = input("Capacidade de pessoas: ").strip()

        sala = {
            'nome_sala': nome,
            'tipo_sala': tipo,
            'equipamentos_disponiveis': equipamentos,
            'localizacao_sala': localizacao,
            'observacoes_sala': observacoes,
            'capacidade_pessoas': int(capacidade)
        }

        self.salas.append(sala)
        print("\nSala cadastrada com sucesso!")

    def listar_salas(self):
        print("\n--- Lista de Salas ---")
        if not self.salas:
            print("Nenhuma sala cadastrada.")
            return

        for i, sala in enumerate(self.salas, 1):
            print(f"\nSala {i}:")
            print(f"Nome: {sala['nome_sala']}")
            print(f"Tipo: {sala['tipo_sala']}")
            print(f"Equipamentos: {sala['equipamentos_disponiveis']}")
            print(f"Localização: {sala['localizacao_sala']}")
            print(f"Observações: {sala['observacoes_sala']}")
            print(f"Capacidade: {sala['capacidade_pessoas']} pessoas")

    def buscar_sala(self, nome):
        for sala in self.salas:
            if sala['nome_sala'].lower() == nome.lower():
                return sala
        return None

    def editar_sala(self):
        print("\n--- Editar Sala ---")
        nome = input("Digite o nome da sala que deseja editar: ").strip()
        sala = self.buscar_sala(nome)

        if not sala:
            print("Sala não encontrada.")
            return

        novo_tipo = input(f"Tipo atual: {sala['tipo_sala']}\nNovo tipo: ").strip()
        if novo_tipo:
            sala['tipo_sala'] = novo_tipo

        novos_equipamentos = input(f"Equipamentos atuais: {sala['equipamentos_disponiveis']}\nNovos equipamentos: ").strip()
        if novos_equipamentos:
            sala['equipamentos_disponiveis'] = novos_equipamentos

        nova_localizacao = input(f"Localização atual: {sala['localizacao_sala']}\nNova localização: ").strip()
        if nova_localizacao:
            sala['localizacao_sala'] = nova_localizacao

        novas_observacoes = input(f"Observações atuais: {sala['observacoes_sala']}\nNovas observações: ").strip()
        if novas_observacoes:
            sala['observacoes_sala'] = novas_observacoes

        nova_capacidade = input(f"Capacidade atual: {sala['capacidade_pessoas']}\nNova capacidade: ").strip()
        if nova_capacidade:
            while not self.validar_capacidade(nova_capacidade):
                print("Capacidade inválida. Digite um número positivo.")
                nova_capacidade = input("Nova capacidade: ").strip()
            sala['capacidade_pessoas'] = int(nova_capacidade)

        print("\nSala atualizada com sucesso!")

    def excluir_sala(self):
        print("\n--- Excluir Sala ---")
        nome = input("Digite o nome da sala que deseja excluir: ").strip()

        for i, sala in enumerate(self.salas):
            if sala['nome_sala'].lower() == nome.lower():
                confirmacao = input(f"Tem certeza que deseja excluir {sala['nome_sala']}? (S/N): ").strip().upper()
                if confirmacao == 'S':
                    del self.salas[i]
                    print("Sala excluída com sucesso.")
                return

        print("Sala não encontrada.")

def menu():
    gerenciador = GerenciadorSalas()

    while True:
        print("\n--- Sistema de Gerenciamento de Salas ---")
        print("1. Cadastrar nova sala")
        print("2. Listar todas as salas")
        print("3. Editar sala")
        print("4. Excluir sala")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            gerenciador.cadastrar_sala()
        elif opcao == '2':
            gerenciador.listar_salas()
        elif opcao == '3':
            gerenciador.editar_sala()
        elif opcao == '4':
            gerenciador.excluir_sala()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    menu()
