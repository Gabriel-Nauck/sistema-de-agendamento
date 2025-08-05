class GerenciadorHorarios:
    def __init__(self):
        self.horarios = []
    
    def validar_horario(self, horario):
        try:
            horas, minutos = map(int, horario.split(':'))
            return 0 <= horas < 24 and 0 <= minutos < 60
        except:
            return False
    
    def validar_dia_semana(self, dia):
        dias_validos = ['segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo']
        return dia.lower() in dias_validos
    
    def validar_intervalo(self, intervalo):
        return intervalo.isdigit() and int(intervalo) > 0
    
    def cadastrar_horario(self):
        print("\n--- Cadastro de Novo Horário ---")
        
        dia_semana = input("Dia da semana: ").strip().lower()
        while not self.validar_dia_semana(dia_semana):
            print("Dia inválido. Digite: segunda, terça, quarta, quinta, sexta, sábado ou domingo")
            dia_semana = input("Dia da semana: ").strip().lower()
        
        if any(h['dia_semana'] == dia_semana for h in self.horarios):
            print("Já existe horário cadastrado para este dia.")
            return
        
        horario_abertura = input("Horário de abertura (HH:MM): ").strip()
        while not self.validar_horario(horario_abertura):
            print("Horário inválido. Use formato HH:MM")
            horario_abertura = input("Horário de abertura (HH:MM): ").strip()
        
        horario_fechamento = input("Horário de fechamento (HH:MM): ").strip()
        while not self.validar_horario(horario_fechamento):
            print("Horário inválido. Use formato HH:MM")
            horario_fechamento = input("Horário de fechamento (HH:MM): ").strip()
        
        horario_almoco_inicio = input("Horário de início do almoço (HH:MM): ").strip()
        while not self.validar_horario(horario_almoco_inicio):
            print("Horário inválido. Use formato HH:MM")
            horario_almoco_inicio = input("Horário de início do almoço (HH:MM): ").strip()
        
        ativo_dia = input("Dia ativo? (S/N): ").strip().upper()
        while ativo_dia not in ['S', 'N']:
            print("Digite S para sim ou N para não")
            ativo_dia = input("Dia ativo? (S/N): ").strip().upper()
        
        intervalo_consultas_min = input("Intervalo entre consultas (minutos): ").strip()
        while not self.validar_intervalo(intervalo_consultas_min):
            print("Intervalo inválido. Digite um número positivo")
            intervalo_consultas_min = input("Intervalo entre consultas (minutos): ").strip()
        
        horario = {
            'dia_semana': dia_semana,
            'horario_abertura': horario_abertura,
            'horario_fechamento': horario_fechamento,
            'horario_almoco_inicio': horario_almoco_inicio,
            'ativo_dia': ativo_dia == 'S',
            'intervalo_consultas_min': int(intervalo_consultas_min)
        }
        
        self.horarios.append(horario)
        print("\nHorário cadastrado com sucesso!")
    
    def listar_horarios(self):
        print("\n--- Lista de Horários ---")
        if not self.horarios:
            print("Nenhum horário cadastrado.")
            return
        
        for i, horario in enumerate(self.horarios, 1):
            print(f"\nHorário {i}:")
            print(f"Dia: {horario['dia_semana'].capitalize()}")
            print(f"Abertura: {horario['horario_abertura']}")
            print(f"Fechamento: {horario['horario_fechamento']}")
            print(f"Início almoço: {horario['horario_almoco_inicio']}")
            print(f"Dia ativo: {'Sim' if horario['ativo_dia'] else 'Não'}")
            print(f"Intervalo consultas: {horario['intervalo_consultas_min']} minutos")
    
    def buscar_horario(self, dia):
        for horario in self.horarios:
            if horario['dia_semana'] == dia:
                return horario
        return None
    
    def editar_horario(self):
        print("\n--- Editar Horário ---")
        dia = input("Digite o dia da semana que deseja editar: ").strip().lower()
        horario = self.buscar_horario(dia)
        
        if not horario:
            print("Horário não encontrado.")
            return
        
        novo_horario_abertura = input(f"Abertura atual: {horario['horario_abertura']}\nNova abertura (HH:MM): ").strip()
        if novo_horario_abertura:
            while not self.validar_horario(novo_horario_abertura):
                print("Horário inválido. Use formato HH:MM")
                novo_horario_abertura = input("Nova abertura (HH:MM): ").strip()
            horario['horario_abertura'] = novo_horario_abertura
        
        novo_horario_fechamento = input(f"Fechamento atual: {horario['horario_fechamento']}\nNovo fechamento (HH:MM): ").strip()
        if novo_horario_fechamento:
            while not self.validar_horario(novo_horario_fechamento):
                print("Horário inválido. Use formato HH:MM")
                novo_horario_fechamento = input("Novo fechamento (HH:MM): ").strip()
            horario['horario_fechamento'] = novo_horario_fechamento
        
        novo_horario_almoco = input(f"Início almoço atual: {horario['horario_almoco_inicio']}\nNovo início (HH:MM): ").strip()
        if novo_horario_almoco:
            while not self.validar_horario(novo_horario_almoco):
                print("Horário inválido. Use formato HH:MM")
                novo_horario_almoco = input("Novo início almoço (HH:MM): ").strip()
            horario['horario_almoco_inicio'] = novo_horario_almoco
        
        novo_ativo = input(f"Dia ativo atual: {'Sim' if horario['ativo_dia'] else 'Não'}\nAtualizar? (S/N): ").strip().upper()
        if novo_ativo:
            while novo_ativo not in ['S', 'N']:
                print("Digite S para sim ou N para não")
                novo_ativo = input("Dia ativo? (S/N): ").strip().upper()
            horario['ativo_dia'] = novo_ativo == 'S'
        
        novo_intervalo = input(f"Intervalo atual: {horario['intervalo_consultas_min']} minutos\nNovo intervalo: ").strip()
        if novo_intervalo:
            while not self.validar_intervalo(novo_intervalo):
                print("Intervalo inválido. Digite um número positivo")
                novo_intervalo = input("Novo intervalo (minutos): ").strip()
            horario['intervalo_consultas_min'] = int(novo_intervalo)
        
        print("\nHorário atualizado com sucesso!")
    
    def excluir_horario(self):
        print("\n--- Excluir Horário ---")
        dia = input("Digite o dia da semana que deseja excluir: ").strip().lower()
        
        for i, horario in enumerate(self.horarios):
            if horario['dia_semana'] == dia:
                confirmacao = input(f"Tem certeza que deseja excluir o horário de {horario['dia_semana']}? (S/N): ").strip().upper()
                if confirmacao == 'S':
                    del self.horarios[i]
                    print("Horário excluído com sucesso.")
                return
        
        print("Horário não encontrado.")

def menu():
    gerenciador = GerenciadorHorarios()
    
    while True:
        print("\n--- Sistema de Gerenciamento de Horários ---")
        print("1. Cadastrar novo horário")
        print("2. Listar todos os horários")
        print("3. Editar horário")
        print("4. Excluir horário")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            gerenciador.cadastrar_horario()
        elif opcao == '2':
            gerenciador.listar_horarios()
        elif opcao == '3':
            gerenciador.editar_horario()
        elif opcao == '4':
            gerenciador.excluir_horario()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    menu()
