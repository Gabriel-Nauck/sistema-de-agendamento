class GerenciadorEspecialidades:
    def __init__(self):
        self.especialidades = []

    def validar_tempo_consulta(self, tempo):
        return tempo.isdigit() and int(tempo) > 0

    def validar_valor(self, valor):
        try:
            return float(valor) > 0
        except ValueError:
            return False

    def cadastrar_especialidade(self):
        print("\n--- Cadastro de Nova Especialidade ---")
        
        nome = input("Nome da especialidade: ").strip()
        if any(esp['nome_especialidade'] == nome for esp in self.especialidades):
            print("Especialidade já cadastrada.")
            return

        descricao = input("Descrição: ").strip()
        codigo = input("Código CBIPM: ").strip()
        area = input("Área da medicina: ").strip()
        requisitos = input("Requisitos de formação: ").strip()
        
        tempo = input("Tempo padrão de consulta (minutos): ").strip()
        while not self.validar_tempo_consulta(tempo):
            print("Tempo inválido. Digite um número positivo.")
            tempo = input("Tempo padrão de consulta (minutos): ").strip()
        
        valor = input("Valor médio da consulta: R$ ").strip()
        while not self.validar_valor(valor):
            print("Valor inválido. Digite um número positivo.")
            valor = input("Valor médio da consulta: R$ ").strip()

        especialidade = {
            'nome_especialidade': nome,
            'descricao_especialidade': descricao,
            'codigo_cbipm': codigo,
            'area_medicina': area,
            'requisitos_formacao': requisitos,
            'tempo_consulta_padrao': int(tempo),
            'valor_medio_consulta': float(valor)
        }

        self.especialidades.append(especialidade)
        print("\nEspecialidade cadastrada com sucesso!")

    def listar_especialidades(self):
        print("\n--- Lista de Especialidades ---")
        if not self.especialidades:
            print("Nenhuma especialidade cadastrada.")
            return

        for i, esp in enumerate(self.especialidades, 1):
            print(f"\nEspecialidade {i}:")
            print(f"Nome: {esp['nome_especialidade']}")
            print(f"Descrição: {esp['descricao_especialidade']}")
            print(f"Código CBIPM: {esp['codigo_cbipm']}")
            print(f"Área: {esp['area_medicina']}")
            print(f"Requisitos: {esp['requisitos_formacao']}")
            print(f"Tempo consulta: {esp['tempo_consulta_padrao']} min")
            print(f"Valor médio: R$ {esp['valor_medio_consulta']:.2f}")

    def buscar_especialidade(self, nome):
        for esp in self.especialidades:
            if esp['nome_especialidade'].lower() == nome.lower():
                return esp
        return None

    def editar_especialidade(self):
        print("\n--- Editar Especialidade ---")
        nome = input("Digite o nome da especialidade que deseja editar: ").strip()
        especialidade = self.buscar_especialidade(nome)

        if not especialidade:
            print("Especialidade não encontrada.")
            return

        nova_descricao = input(f"Descrição atual: {especialidade['descricao_especialidade']}\nNova descrição: ").strip()
        if nova_descricao:
            especialidade['descricao_especialidade'] = nova_descricao

        novo_codigo = input(f"Código atual: {especialidade['codigo_cbipm']}\nNovo código: ").strip()
        if novo_codigo:
            especialidade['codigo_cbipm'] = novo_codigo

        nova_area = input(f"Área atual: {especialidade['area_medicina']}\nNova área: ").strip()
        if nova_area:
            especialidade['area_medicina'] = nova_area

        novos_requisitos = input(f"Requisitos atuais: {especialidade['requisitos_formacao']}\nNovos requisitos: ").strip()
        if novos_requisitos:
            especialidade['requisitos_formacao'] = novos_requisitos

        novo_tempo = input(f"Tempo atual: {especialidade['tempo_consulta_padrao']} min\nNovo tempo: ").strip()
        if novo_tempo:
            while not self.validar_tempo_consulta(novo_tempo):
                print("Tempo inválido. Digite um número positivo.")
                novo_tempo = input("Novo tempo (minutos): ").strip()
            especialidade['tempo_consulta_padrao'] = int(novo_tempo)

        novo_valor = input(f"Valor atual: R$ {especialidade['valor_medio_consulta']:.2f}\nNovo valor: R$ ").strip()
        if novo_valor:
            while not self.validar_valor(novo_valor):
                print("Valor inválido. Digite um número positivo.")
                novo_valor = input("Novo valor: R$ ").strip()
            especialidade['valor_medio_consulta'] = float(novo_valor)

        print("\nEspecialidade atualizada com sucesso!")

    def excluir_especialidade(self):
        print("\n--- Excluir Especialidade ---")
        nome = input("Digite o nome da especialidade que deseja excluir: ").strip()

        for i, esp in enumerate(self.especialidades):
            if esp['nome_especialidade'].lower() == nome.lower():
                confirmacao = input(f"Tem certeza que deseja excluir {esp['nome_especialidade']}? (S/N): ").strip().upper()
                if confirmacao == 'S':
                    del self.especialidades[i]
                    print("Especialidade excluída com sucesso.")
                return

        print("Especialidade não encontrada.")

def menu():
    gerenciador = GerenciadorEspecialidades()

    while True:
        print("\n--- Sistema de Gerenciamento de Especialidades ---")
        print("1. Cadastrar nova especialidade")
        print("2. Listar todas as especialidades")
        print("3. Editar especialidade")
        print("4. Excluir especialidade")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            gerenciador.cadastrar_especialidade()
        elif opcao == '2':
            gerenciador.listar_especialidades()
        elif opcao == '3':
            gerenciador.editar_especialidade()
        elif opcao == '4':
            gerenciador.excluir_especialidade()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    menu()
