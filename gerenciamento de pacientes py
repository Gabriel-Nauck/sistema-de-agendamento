import re
from datetime import datetime

class GerenciadorPacientes:
    def __init__(self):
        self.pacientes = []
   
    def validar_cpf(self, cpf):
        """Valida o formato do CPF (apenas dígitos, 11 caracteres)"""
        return cpf.isdigit() and len(cpf) == 11
   
    def formatar_telefone(self, telefone):
        """Remove caracteres não numéricos do telefone"""
        return ''.join(filter(str.isdigit, telefone))
   
    def validar_idade(self, idade):
        """Valida se a idade é um número positivo"""
        return idade.isdigit() and int(idade) >= 0
   
    def validar_peso(self, peso):
        """Valida se o peso é um número positivo"""
        try:
            peso_float = float(peso)
            return peso_float > 0
        except ValueError:
            return False
   
    def cadastrar_paciente(self):
        """Cadastra um novo paciente"""
        print("\n--- Cadastro de Novo Paciente ---")
       
        nome_paciente = input("Nome completo do paciente: ").strip()
       
        cpf_paciente = input("CPF (apenas números): ").strip()
        while not self.validar_cpf(cpf_paciente):
            print("CPF inválido. Deve conter exatamente 11 dígitos numéricos.")
            cpf_paciente = input("CPF (apenas números): ").strip()
       
        # Verificar se CPF já existe
        if any(paciente['cpf_paciente'] == cpf_paciente for paciente in self.pacientes):
            print("Erro: Já existe um paciente cadastrado com este CPF.")
            return
       
        telefone_contato = self.formatar_telefone(input("Telefone para contato: ").strip())
        endereco_completo = input("Endereço completo: ").strip()
        plano_saude = input("Plano de saúde: ").strip()
       
        idade = input("Idade: ").strip()
        while not self.validar_idade(idade):
            print("Idade inválida. Digite um número positivo.")
            idade = input("Idade: ").strip()
        idade = int(idade)
       
        peso = input("Peso (kg): ").strip()
        while not self.validar_peso(peso):
            print("Peso inválido. Digite um número positivo.")
            peso = input("Peso (kg): ").strip()
        peso = float(peso)
       
        paciente = {
            'nome_paciente': nome_paciente,
            'cpf_paciente': cpf_paciente,
            'telefone_contato': telefone_contato,
            'endereco_completo': endereco_completo,
            'plano_saude': plano_saude,
            'idade': idade,
            'peso': peso
        }
       
        self.pacientes.append(paciente)
        print("\nPaciente cadastrado com sucesso!")
   
    def listar_pacientes(self):
        """Lista todos os pacientes cadastrados"""
        print("\n--- Lista de Pacientes ---")
        if not self.pacientes:
            print("Nenhum paciente cadastrado.")
            return
       
        for i, paciente in enumerate(self.pacientes, 1):
            print(f"\nPaciente {i}:")
            print(f"Nome: {paciente['nome_paciente']}")
            print(f"CPF: {paciente['cpf_paciente']}")
            print(f"Telefone: {paciente['telefone_contato']}")
            print(f"Endereço: {paciente['endereco_completo']}")
            print(f"Plano de saúde: {paciente['plano_saude']}")
            print(f"Idade: {paciente['idade']} anos")
            print(f"Peso: {paciente['peso']} kg")
   
    def buscar_paciente(self, cpf):
        """Busca um paciente pelo CPF"""
        for paciente in self.pacientes:
            if paciente['cpf_paciente'] == cpf:
                return paciente
        return None
   
    def editar_paciente(self):
        """Edita um paciente existente"""
        print("\n--- Editar Paciente ---")
        cpf = input("Digite o CPF do paciente que deseja editar: ").strip()
        paciente = self.buscar_paciente(cpf)
       
        if not paciente:
            print("Paciente não encontrado.")
            return
       
        print("\nDeixe em branco os campos que não deseja alterar.")
       
        novo_nome = input(f"Nome atual: {paciente['nome_paciente']}\nNovo nome: ").strip()
        if novo_nome:
            paciente['nome_paciente'] = novo_nome
       
        novo_telefone = input(f"Telefone atual: {paciente['telefone_contato']}\nNovo telefone: ").strip()
        if novo_telefone:
            paciente['telefone_contato'] = self.formatar_telefone(novo_telefone)
       
        novo_endereco = input(f"Endereço atual: {paciente['endereco_completo']}\nNovo endereço: ").strip()
        if novo_endereco:
            paciente['endereco_completo'] = novo_endereco
       
        novo_plano = input(f"Plano de saúde atual: {paciente['plano_saude']}\nNovo plano: ").strip()
        if novo_plano:
            paciente['plano_saude'] = novo_plano
       
        nova_idade = input(f"Idade atual: {paciente['idade']}\nNova idade: ").strip()
        if nova_idade:
            while not self.validar_idade(nova_idade):
                print("Idade inválida. Digite um número positivo.")
                nova_idade = input("Nova idade: ").strip()
            paciente['idade'] = int(nova_idade)
       
        novo_peso = input(f"Peso atual: {paciente['peso']} kg\nNovo peso (kg): ").strip()
        if novo_peso:
            while not self.validar_peso(novo_peso):
                print("Peso inválido. Digite um número positivo.")
                novo_peso = input("Novo peso (kg): ").strip()
            paciente['peso'] = float(novo_peso)
       
        print("\nPaciente atualizado com sucesso!")
   
    def excluir_paciente(self):
        """Exclui um paciente"""
        print("\n--- Excluir Paciente ---")
        cpf = input("Digite o CPF do paciente que deseja excluir: ").strip()
       
        for i, paciente in enumerate(self.pacientes):
            if paciente['cpf_paciente'] == cpf:
                confirmacao = input(f"Tem certeza que deseja excluir {paciente['nome_paciente']}? (S/N): ").strip().upper()
                if confirmacao == 'S':
                    del self.pacientes[i]
                    print("Paciente excluído com sucesso.")
                return
       
        print("Paciente não encontrado.")

def menu():
    gerenciador = GerenciadorPacientes()
   
    while True:
        print("\n--- Sistema de Gerenciamento de Pacientes ---")
        print("1. Cadastrar novo paciente")
        print("2. Listar todos os pacientes")
        print("3. Editar paciente")
        print("4. Excluir paciente")
        print("5. Sair")
       
        opcao = input("Escolha uma opção: ").strip()
       
        if opcao == '1':
            gerenciador.cadastrar_paciente()
        elif opcao == '2':
            gerenciador.listar_pacientes()
        elif opcao == '3':
            gerenciador.editar_paciente()
        elif opcao == '4':
            gerenciador.excluir_paciente()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    menu()
