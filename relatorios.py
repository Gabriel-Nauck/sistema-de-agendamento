import os
from datetime import datetime

class GerenciadorRelatorios:
    def __init__(self):
        self.relatorios = []

    def validar_data(self, data):
        try:
            datetime.strptime(data, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def validar_numero(self, valor):
        try:
            return float(valor) >= 0
        except ValueError:
            return False

    def validar_periodo(self, periodo):
        try:
            if '-' in periodo:
                inicio, fim = periodo.split('-')
                return self.validar_data(inicio.strip()) and self.validar_data(fim.strip())
            return self.validar_data(periodo.strip())
        except:
            return False

    def cadastrar_relatorio(self):
        print("\n--- Cadastro de Novo Relatório ---")
        
        tipo = input("Tipo de relatório: ").strip()
        
        data = input("Data de geração (DD/MM/AAAA): ").strip()
        while not self.validar_data(data):
            print("Data inválida. Use o formato DD/MM/AAAA.")
            data = input("Data de geração (DD/MM/AAAA): ").strip()
        
        periodo = input("Período de análise (DD/MM/AAAA ou DD/MM/AAAA - DD/MM/AAAA): ").strip()
        while not self.validar_periodo(periodo):
            print("Período inválido. Use formato DD/MM/AAAA ou DD/MM/AAAA - DD/MM/AAAA.")
            periodo = input("Período de análise: ").strip()
        
        usuario = input("Usuário gerador: ").strip()
        
        caminho = input("Caminho do arquivo: ").strip()
        while not os.path.exists(caminho):
            print("Arquivo não encontrado. Verifique o caminho.")
            caminho = input("Caminho do arquivo: ").strip()
        
        registros = input("Total de registros: ").strip()
        while not registros.isdigit() or int(registros) < 0:
            print("Número inválido. Digite um valor inteiro positivo.")
            registros = input("Total de registros: ").strip()
        
        tamanho = input("Tamanho do arquivo (MB): ").strip()
        while not self.validar_numero(tamanho):
            print("Valor inválido. Digite um número positivo.")
            tamanho = input("Tamanho do arquivo (MB): ").strip()

        relatorio = {
            'tipo_relatorio': tipo,
            'data_geracao': data,
            'periodo_analise': periodo,
            'usuario_gerador': usuario,
            'arquivo_caminho': caminho,
            'total_registros': int(registros),
            'tamanho_arquivo_mb': float(tamanho)
        }

        self.relatorios.append(relatorio)
        print("\nRelatório cadastrado com sucesso!")

    def listar_relatorios(self):
        print("\n--- Lista de Relatórios ---")
        if not self.relatorios:
            print("Nenhum relatório cadastrado.")
            return

        for i, rel in enumerate(self.relatorios, 1):
            print(f"\nRelatório {i}:")
            print(f"Tipo: {rel['tipo_relatorio']}")
            print(f"Data geração: {rel['data_geracao']}")
            print(f"Período análise: {rel['periodo_analise']}")
            print(f"Usuário: {rel['usuario_gerador']}")
            print(f"Arquivo: {rel['arquivo_caminho']}")
            print(f"Registros: {rel['total_registros']}")
            print(f"Tamanho: {rel['tamanho_arquivo_mb']:.2f} MB")

    def buscar_relatorio(self, caminho):
        for rel in self.relatorios:
            if rel['arquivo_caminho'] == caminho:
                return rel
        return None

    def editar_relatorio(self):
        print("\n--- Editar Relatório ---")
        caminho = input("Digite o caminho do arquivo que deseja editar: ").strip()
        relatorio = self.buscar_relatorio(caminho)

        if not relatorio:
            print("Relatório não encontrado.")
            return

        novo_tipo = input(f"Tipo atual: {relatorio['tipo_relatorio']}\nNovo tipo: ").strip()
        if novo_tipo:
            relatorio['tipo_relatorio'] = novo_tipo

        nova_data = input(f"Data atual: {relatorio['data_geracao']}\nNova data (DD/MM/AAAA): ").strip()
        if nova_data:
            while not self.validar_data(nova_data):
                print("Data inválida. Use o formato DD/MM/AAAA.")
                nova_data = input("Nova data (DD/MM/AAAA): ").strip()
            relatorio['data_geracao'] = nova_data

        novo_periodo = input(f"Período atual: {relatorio['periodo_analise']}\nNovo período: ").strip()
        if novo_periodo:
            while not self.validar_periodo(novo_periodo):
                print("Período inválido. Use formato DD/MM/AAAA ou DD/MM/AAAA - DD/MM/AAAA.")
                novo_periodo = input("Novo período: ").strip()
            relatorio['periodo_analise'] = novo_periodo

        novo_usuario = input(f"Usuário atual: {relatorio['usuario_gerador']}\nNovo usuário: ").strip()
        if novo_usuario:
            relatorio['usuario_gerador'] = novo_usuario

        novo_caminho = input(f"Caminho atual: {relatorio['arquivo_caminho']}\nNovo caminho: ").strip()
        if novo_caminho:
            while not os.path.exists(novo_caminho):
                print("Arquivo não encontrado. Verifique o caminho.")
                novo_caminho = input("Novo caminho: ").strip()
            relatorio['arquivo_caminho'] = novo_caminho

        novos_registros = input(f"Registros atuais: {relatorio['total_registros']}\nNovo total: ").strip()
        if novos_registros:
            while not novos_registros.isdigit() or int(novos_registros) < 0:
                print("Número inválido. Digite um valor inteiro positivo.")
                novos_registros = input("Novo total de registros: ").strip()
            relatorio['total_registros'] = int(novos_registros)

        novo_tamanho = input(f"Tamanho atual: {relatorio['tamanho_arquivo_mb']:.2f} MB\nNovo tamanho (MB): ").strip()
        if novo_tamanho:
            while not self.validar_numero(novo_tamanho):
                print("Valor inválido. Digite um número positivo.")
                novo_tamanho = input("Novo tamanho (MB): ").strip()
            relatorio['tamanho_arquivo_mb'] = float(novo_tamanho)

        print("\nRelatório atualizado com sucesso!")

    def excluir_relatorio(self):
        print("\n--- Excluir Relatório ---")
        caminho = input("Digite o caminho do arquivo que deseja excluir: ").strip()

        for i, rel in enumerate(self.relatorios):
            if rel['arquivo_caminho'] == caminho:
                confirmacao = input(f"Tem certeza que deseja excluir o relatório {caminho}? (S/N): ").strip().upper()
                if confirmacao == 'S':
                    del self.relatorios[i]
                    print("Relatório excluído com sucesso.")
                return

        print("Relatório não encontrado.")

def menu():
    gerenciador = GerenciadorRelatorios()

    while True:
        print("\n--- Sistema de Gerenciamento de Relatórios ---")
        print("1. Cadastrar novo relatório")
        print("2. Listar todos os relatórios")
        print("3. Editar relatório")
        print("4. Excluir relatório")
        print("5. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            gerenciador.cadastrar_relatorio()
        elif opcao == '2':
            gerenciador.listar_relatorios()
        elif opcao == '3':
            gerenciador.editar_relatorio()
        elif opcao == '4':
            gerenciador.excluir_relatorio()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    menu()
