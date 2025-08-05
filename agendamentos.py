class GerenciadorAgendamentos:
    def __init__(self):
        self.agendamentos = []

    def validar_data(self, data):
        try:
            from datetime import datetime
            datetime.strptime(data, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def validar_horario(self, horario):
        try:
            horas, minutos = map(int, horario.split(':'))
            return 0 <= horas < 24 and 0 <= minutos < 60
        except ValueError:
            return False

    def validar_duracao(self, duracao):
        return duracao.isdigit() and int(duracao) > 0

    def validar_valor(self, valor):
        try:
            return float(valor) >= 0
        except ValueError:
            return False

    def cadastrar_agendamento(self):
        print("\n--- Cadastro de Novo Agendamento ---")
        
        data = input("Data da consulta (DD/MM/AAAA): ").strip()
        while not self.validar_data(data):
            print("Data inválida. Use o formato DD/MM/AAAA.")
            data = input("Data da consulta (DD/MM/AAAA): ").strip()
        
        horario = input("Horário da consulta (HH:MM): ").strip()
        while not self.validar_horario(horario):
            print("Horário inválido. Use formato HH:MM.")
            horario = input("Horário da consulta (HH:MM): ").strip()
        
        status = input("Status do agendamento: ").strip()
        observacoes = input("Observações: ").strip()
        tipo = input("Tipo de consulta: ").strip()
        
        duracao = input("Duração em minutos: ").strip()
        while not self.validar_duracao(duracao):
            print("Duração inválida. Digite um número positivo.")
            duracao = input("Duração em minutos: ").strip()
        
        valor = input("Valor pago: R$ ").strip()
        while not self.validar_valor(valor):
            print("Valor inválido. Digite um número positivo.")
            valor = input("Valor pago: R$ ").strip()

        agendamento = {
            'data_consulta': data,
            'horario_consulta': horario,
            'status_agendamento': status,
            'observacoes': observacoes,
            'tipo_consulta': tipo,
            'duracao_minutos': int(duracao),
            'valor_pago': float(valor)
        }

        self.agendamentos.append(agendamento)
        print("\nAgendamento cadastrado com sucesso!")

    def listar_agendamentos(self):
        print("\n--- Lista de Agendamentos ---")
        if not self.agendamentos:
            print("Nenhum agendamento cadastrado.")
            return

        for i, agendamento in enumerate(self.agendamentos, 1):
            print(f"\nAgendamento {i}:")
            print(f"Data: {agendamento['data_consulta']}")
            print(f"Horário: {agendamento['horario_consulta']}")
            print(f"Status: {agendamento['status_agendamento']}")
            print(f"Observações: {agendamento['observacoes']}")
            print(f"Tipo: {agendamento['tipo_consulta']}")
            print(f"Duração: {agendamento['duracao_minutos']} minutos")
            print(f"Valor: R$ {agendamento['valor_pago']:.2f}")

    def buscar_agendamento(self, data, horario):
        for agendamento in self.agendamentos:
            if agendamento['data_consulta'] == data and agendamento['horario_consulta'] == horario:
                return agendamento
        return None

    def editar_agendamento(self):
        print("\n--- Editar Agendamento ---")
        data = input("Digite a data do agendamento (DD/MM/AAAA): ").strip()
        horario = input("Digite o horário do agendamento (HH:MM): ").strip()
        agendamento = self.buscar_agendamento(data, horario)

        if not agendamento:
            print("Agendamento não encontrado.")
            return

        novo_status = input(f"Status atual: {agendamento['status_agendamento']}\nNovo status: ").strip()
        if novo_status:
            agendamento['status_agendamento'] = novo_status

        novas_observacoes = input(f"Observações atuais: {agendamento['observacoes']}\nNovas observações: ").strip()
        if novas_observacoes:
            agendamento['observacoes'] = novas_observacoes

        novo_tipo = input(f"Tipo atual: {agendamento['tipo_consulta']}\nNovo tipo: ").strip()
        if novo_tipo:
            agendamento['tipo_consulta'] = novo_tipo

        nova_duracao = input(f"Duração atual: {agendamento['duracao_minutos']} min\nNova duração: ").strip()
        if nova_duracao:
            while not self.validar_duracao(nova_duracao):
                print("Duração inválida. Digite um número positivo.")
                nova_duracao = input("Nova duração: ").strip()
            agendamento['duracao_minutos'] = int(nova_duracao)

        novo_valor = input(f"Valor atual: R$ {agendamento['valor_pago']:.2f}\nNovo valor: R$ ").strip()
        if novo_valor:
            while not self.validar_valor(novo_valor):
                print("Valor inválido. Digite um número positivo.")
                novo_valor = input("Novo valor: R$ ").strip()
            agendamento['valor_pago'] = float(novo_valor)

        print("\nAgendamento atualizado com sucesso!")

    def excluir_agendamento(self):
        print("\n--- Excluir Agendamento ---")
        data = input("Digite a data do agendamento (DD/MM/AAAA): ").strip()
        horario = input("Digite o horário do agendamento (HH:MM): ").strip()

        for i, agendamento in enumerate(self.agendamentos):
            if agendamento['data_consulta'] == data and agendamento['horario_consulta'] == horario:
                confirmacao = input(f"Tem certeza que deseja excluir o agendamento de {data} às {horario}? (S/N): ").strip().upper()
                if confirmacao == 'S':
                    del self.agendamentos[i]
                    print("Agendamento excluído com sucesso.")
                return

        print("Agendamento não encontrado.")

def menu():
    gerenciador = GerenciadorAgendamentos()

    while True:
        print("\n--- Sistema de Gerenciamento de Agendamentos ---")
        print("1. Cadastrar novo agendamento")
        print("2. Listar todos os agendamentos")
        print("3. Editar agendamento")
        print("4. Excluir agendamento")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            gerenciador.cadastrar_agendamento()
        elif opcao == '2':
            gerenciador.listar_agendamentos()
        elif opcao == '3':
            gerenciador.editar_agendamento()
        elif opcao == '4':
            gerenciador.excluir_agendamento()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    menu()
