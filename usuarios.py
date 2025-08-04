import re
from datetime import datetime

class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []
   
    def validar_email(self, email):
        """Valida o formato do email"""
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(padrao, email) is not None
   
    def validar_cpf(self, cpf):
        """Valida o formato do CPF (apenas dígitos, 11 caracteres)"""
        return cpf.isdigit() and len(cpf) == 11
   
    def validar_data(self, data_str):
        """Valida o formato da data (DD/MM/AAAA)"""
        try:
            datetime.strptime(data_str, '%d/%m/%Y')
            return True
        except ValueError:
            return False
   
    def formatar_telefone(self, telefone):
        """Remove caracteres não numéricos do telefone"""
        return ''.join(filter(str.isdigit, telefone))
   
    def cadastrar_usuario(self):
        """Cadastra um novo usuário"""
        print("\n--- Cadastro de Novo Usuário ---")
       
        nome_completo = input("Nome completo: ").strip()
        email = input("E-mail: ").strip()
        while not self.validar_email(email):
            print("E-mail inválido. Por favor, insira um e-mail válido.")
            email = input("E-mail: ").strip()
       
        telefone = self.formatar_telefone(input("Telefone: ").strip())
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
        while not self.validar_data(data_nascimento):
            print("Data inválida. Use o formato DD/MM/AAAA.")
            data_nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()
       
        cpf = input("CPF (apenas números): ").strip()
        while not self.validar_cpf(cpf):
            print("CPF inválido. Deve conter exatamente 11 dígitos numéricos.")
            cpf = input("CPF (apenas números): ").strip()
       
        # Verificar se CPF já existe
        if any(user['cpf'] == cpf for user in self.usuarios):
            print("Erro: Já existe um usuário cadastrado com este CPF.")
            return
       
        status_ativo = input("Status ativo (S/N): ").strip().upper()
        while status_ativo not in ['S', 'N']:
            print("Por favor, digite 'S' para ativo ou 'N' para inativo.")
            status_ativo = input("Status ativo (S/N): ").strip().upper()
       
        salario_base = input("Salário base: ").strip()
        while not salario_base.replace('.', '').isdigit():
            print("Salário inválido. Digite apenas números.")
            salario_base = input("Salário base: ").strip()
        salario_base = float(salario_base)
       
        usuario = {
            'nome_completo': nome_completo,
            'email': email,
            'telefone': telefone,
            'data_nascimento': data_nascimento,
            'cpf': cpf,
            'status_ativo': status_ativo == 'S',
            'salario_base': salario_base
        }
       
        self.usuarios.append(usuario)
        print("\nUsuário cadastrado com sucesso!")
   
    def listar_usuarios(self):
        """Lista todos os usuários cadastrados"""
        print("\n--- Lista de Usuários ---")
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
       
        for i, usuario in enumerate(self.usuarios, 1):
            status = "Ativo" if usuario['status_ativo'] else "Inativo"
            print(f"\nUsuário {i}:")
            print(f"Nome: {usuario['nome_completo']}")
            print(f"E-mail: {usuario['email']}")
            print(f"Telefone: {usuario['telefone']}")
            print(f"Data de Nascimento: {usuario['data_nascimento']}")
            print(f"CPF: {usuario['cpf']}")
            print(f"Status: {status}")
            print(f"Salário Base: R$ {usuario['salario_base']:.2f}")
   
    def buscar_usuario(self, cpf):
        """Busca um usuário pelo CPF"""
        for usuario in self.usuarios:
            if usuario['cpf'] == cpf:
                return usuario
        return None
   
    def editar_usuario(self):
        """Edita um usuário existente"""
        print("\n--- Editar Usuário ---")
        cpf = input("Digite o CPF do usuário que deseja editar: ").strip()
        usuario = self.buscar_usuario(cpf)
       
        if not usuario:
            print("Usuário não encontrado.")
            return
       
        print("\nDeixe em branco os campos que não deseja alterar.")
       
        novo_nome = input(f"Nome atual: {usuario['nome_completo']}\nNovo nome: ").strip()
        if novo_nome:
            usuario['nome_completo'] = novo_nome
       
        novo_email = input(f"E-mail atual: {usuario['email']}\nNovo e-mail: ").strip()
        if novo_email:
            while not self.validar_email(novo_email):
                print("E-mail inválido. Por favor, insira um e-mail válido.")
                novo_email = input("Novo e-mail: ").strip()
            usuario['email'] = novo_email
       
        novo_telefone = input(f"Telefone atual: {usuario['telefone']}\nNovo telefone: ").strip()
        if novo_telefone:
            usuario['telefone'] = self.formatar_telefone(novo_telefone)
       
        nova_data = input(f"Data de nascimento atual: {usuario['data_nascimento']}\nNova data (DD/MM/AAAA): ").strip()
        if nova_data:
            while not self.validar_data(nova_data):
                print("Data inválida. Use o formato DD/MM/AAAA.")
                nova_data = input("Nova data de nascimento (DD/MM/AAAA): ").strip()
            usuario['data_nascimento'] = nova_data
       
        novo_status = input(f"Status atual: {'Ativo' if usuario['status_ativo'] else 'Inativo'}\nNovo status (S/N): ").strip().upper()
        if novo_status:
            while novo_status not in ['S', 'N']:
                print("Por favor, digite 'S' para ativo ou 'N' para inativo.")
                novo_status = input("Novo status (S/N): ").strip().upper()
            usuario['status_ativo'] = novo_status == 'S'
       
        novo_salario = input(f"Salário atual: R$ {usuario['salario_base']:.2f}\nNovo salário: ").strip()
        if novo_salario:
            while not novo_salario.replace('.', '').isdigit():
                print("Salário inválido. Digite apenas números.")
                novo_salario = input("Novo salário: ").strip()
            usuario['salario_base'] = float(novo_salario)
       
        print("\nUsuário atualizado com sucesso!")
   
    def excluir_usuario(self):
        """Exclui um usuário"""
        print("\n--- Excluir Usuário ---")
        cpf = input("Digite o CPF do usuário que deseja excluir: ").strip()
       
        for i, usuario in enumerate(self.usuarios):
            if usuario['cpf'] == cpf:
                confirmacao = input(f"Tem certeza que deseja excluir {usuario['nome_completo']}? (S/N): ").strip().upper()
                if confirmacao == 'S':
                    del self.usuarios[i]
                    print("Usuário excluído com sucesso.")
                return
       
        print("Usuário não encontrado.")

def menu():
    gerenciador = GerenciadorUsuarios()
   
    while True:
        print("\n--- Sistema de Gerenciamento de Usuários ---")
        print("1. Cadastrar novo usuário")
        print("2. Listar todos os usuários")
        print("3. Editar usuário")
        print("4. Excluir usuário")
        print("5. Sair")
       
        opcao = input("Escolha uma opção: ").strip()
       
        if opcao == '1':
            gerenciador.cadastrar_usuario()
        elif opcao == '2':
            gerenciador.listar_usuarios()
        elif opcao == '3':
            gerenciador.editar_usuario()
        elif opcao == '4':
            gerenciador.excluir_usuario()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":        
    menu()
