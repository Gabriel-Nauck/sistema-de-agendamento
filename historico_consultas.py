from datetime import datetime

class GerenciadorHistoricoConsultas:
    def __init__(self):
        self.historico = []

    def validar_data(self, data):
        try:
            datetime.strptime(data, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def validar_valor(self, valor):
        try:
            return float(valor) >= 0
        except ValueError:
            return False

    def validar_cid(self, codigo):
        return len(codigo.strip()) > 0

    def cadastrar_consulta(self):
        print("\n--- Cadastro de Nova Consulta no Histórico ---")
        
        data = input("Data do atendimento (DD/MM/AAAA): ").strip()
        while not self.validar_data(data):
            print("Data inválida. Use o formato DD/MM/AAAA.")
            data = input("Data do atendimento (DD/MM/AAAA): ").strip()

        diagnostico = input("Diagnóstico inicial: ").strip()
        prescricao = input("Prescrição médica: ").strip()
        observacoes = input("Observações médicas: ").strip()
        
        cid = input("Código CID: ").strip()
        while not self.validar_cid(cid):
            print("Código CID não pode ser vazio.")
            cid = input("Código CID: ").strip()
        
        retorno = input("Necessita retorno? (S/N): ").strip().upper()
        while retorno not in ['S', 'N']:
            print("Digite S para sim ou N para não.")
            retorno = input("Necessita retorno? (S/N): ").strip().upper()
        
        valor = input("Valor da consulta: R$ ").strip()
        while not self.validar_valor(valor):
            print("Valor inválido. Digite um número positivo.")
            valor = input("Valor da consulta: R$ ").strip()

        consulta = {
            'data_atendimento': data,
            'diagnostico_inicial': diagnostico,
            'prescricao_medica': prescricao,
            'observacoes_medicas': observacoes,
            'codigo_cid': cid,
            'retorno_necessario': retorno == 'S',
            'valor_consulta_realizada': float(valor)
        }

        self.historico.append(consulta)
        print("\nConsulta registrada no histórico com sucesso!")

    def listar_consultas(self):
        print("\n--- Histórico de Consultas ---")
        if not self.historico:
            print("Nenhuma consulta registrada.")
            return

        for i, consulta in enumerate(self.historico, 1):
            print(f"\nConsulta {i}:")
            print(f"Data: {consulta['data_atendimento']}")
            print(f"Diagnóstico: {consulta['diagnostico_inicial']}")
            print(f"Prescrição: {consulta['prescricao_medica']}")
            print(f"Observações: {consulta['observacoes_medicas']}")
            print(f"CID: {consulta['codigo_cid']}")
            print(f"Retorno necessário: {'Sim' if consulta['retorno_necessario'] else 'Não'}")
            print(f"Valor: R$ {consulta['valor_consulta_realizada']:.2f}")

    def buscar_consulta(self, data):
        return [c for c in self.historico if c['data_atendimento'] == data]

    def editar_consulta(self):
        print("\n--- Editar Consulta no Histórico ---")
        data = input("Digite a data da consulta que deseja editar (DD/MM/AAAA): ").strip()
        consultas = self.buscar_consulta(data)

        if not consultas:
            print("Nenhuma consulta encontrada nesta data.")
            return

        if len(consultas) > 1:
            print("\nForam encontradas múltiplas consultas nesta data:")
            for i, c in enumerate(consultas, 1):
                print(f"\nConsulta {i}:")
                print(f"Diagnóstico: {c['diagnostico_inicial']}")
                print(f"CID: {c['codigo_cid']}")
            
            opcao = input("\nDigite o número da consulta que deseja editar: ").strip()
            while not opcao.isdigit() or int(opcao) < 1 or int(opcao) > len(consultas):
                print("Opção inválida.")
                opcao = input("Digite o número da consulta que deseja editar: ").strip()
            
            consulta = consultas[int(opcao)-1]
        else:
            consulta = consultas[0]

        novo_diagnostico = input(f"Diagnóstico atual: {consulta['diagnostico_inicial']}\nNovo diagnóstico: ").strip()
        if novo_diagnostico:
            consulta['diagnostico_inicial'] = novo_diagnostico

        nova_prescricao = input(f"Prescrição atual: {consulta['prescricao_medica']}\nNova prescrição: ").strip()
        if nova_prescricao:
            consulta['prescricao_medica'] = nova_prescricao

        novas_observacoes = input(f"Observações atuais: {consulta['observacoes_medicas']}\nNovas observações: ").strip()
        if novas_observacoes:
            consulta['observacoes_medicas'] = novas_observacoes

        novo_cid = input(f"CID atual: {consulta['codigo_cid']}\nNovo CID: ").strip()
        if novo_cid:
            while not self.validar_cid(novo_cid):
                print("Código CID não pode ser vazio.")
                novo_cid = input("Novo CID: ").strip()
            consulta['codigo_cid'] = novo_cid

        novo_retorno = input(f"Retorno necessário atual: {'Sim' if consulta['retorno_necessario'] else 'Não'}\nAlterar? (S/N): ").strip().upper()
        if novo_retorno in ['S', 'N']:
            consulta['retorno_necessario'] = novo_retorno == 'S'

        novo_valor = input(f"Valor atual: R$ {consulta['valor_consulta_realizada']:.2f}\nNovo valor: R$ ").strip()
        if novo_valor:
            while not self.validar_valor(novo_valor):
                print("Valor inválido. Digite um número positivo.")
                novo_valor = input("Novo valor: R$ ").strip()
            consulta['valor_consulta_realizada'] = float(novo_valor)

        print("\nConsulta atualizada no histórico com sucesso!")

    def excluir_consulta(self):
        print("\n--- Excluir Consulta do Histórico ---")
        data = input("Digite a data da consulta que deseja excluir (DD/MM/AAAA): ").strip()
        consultas = self.buscar_consulta(data)

        if not consultas:
            print("Nenhuma consulta encontrada nesta data.")
            return

        if len(consultas) > 1:
            print("\nForam encontradas múltiplas consultas nesta data:")
            for i, c in enumerate(consultas, 1):
                print(f"\nConsulta {i}:")
                print(f"Diagnóstico: {c['diagnostico_inicial']}")
                print(f"CID: {c['codigo_cid']}")
            
            opcao = input("\nDigite o número da consulta que deseja excluir: ").strip()
            while not opcao.isdigit() or int(opcao) < 1 or int(opcao) > len(consultas):
                print("Opção inválida.")
                opcao = input("Digite o número da consulta que deseja excluir: ").strip()
            
            consulta = consultas[int(opcao)-1]
        else:
            consulta = consultas[0]

        confirmacao = input(f"Tem certeza que deseja excluir a consulta de {data}? (S/N): ").strip().upper()
        if confirmacao == 'S':
            self.historico.remove(consulta)
            print("Consulta removida do histórico com sucesso.")

def menu():
    gerenciador = GerenciadorHistoricoConsultas()

    while True:
        print("\n--- Sistema de Gerenciamento de Histórico de Consultas ---")
        print("1. Registrar nova consulta")
        print("2. Listar histórico de consultas")
        print("3. Editar consulta")
        print("4. Excluir consulta")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            gerenciador.cadastrar_consulta()
        elif opcao == '2':
            gerenciador.listar_consultas()
        elif opcao == '3':
            gerenciador.editar_consulta()
        elif opcao == '4':
            gerenciador.excluir_consulta()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    menu()
