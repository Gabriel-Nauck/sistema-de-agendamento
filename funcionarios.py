import re

class GerenciadorFuncionarios:
    def __init__(self):
        self.funcionarios = []
    
    def validar_email(self, email):
        """Valida o formato do email corporativo"""
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(padrao, email) is not None
    
    def formatar_telefone(self, telefone):
        """Remove caracteres não numéricos do telefone"""
        return ''.join(filter(str.isdigit, telefone))
    
    def validar_horas_trabalho(self, horas):
        """Valida se as horas de trabalho são positivas"""
        try:
            horas_float = float(horas)
            return 0 <= horas_float <= 168  # Máximo de horas em uma semana
        except ValueError:
            return False
    
    def validar_salario(self, salario):
        """Valida se o salário é positivo"""
        try:
            salario_float = float(salario)
            return salario_float > 0
        except ValueError:
            return False
    
    def cadastrar_funcionario(self):
        """Cadastra um novo funcionário"""
        print("\n--- Cadastro de Novo Funcionário ---")
        
        nome_funcionario = input("Nome completo do funcionário: ").strip()
        cargo_funcao = input("Cargo/Função: ").strip()
        telefone_pessoal = self.formatar_telefone(input("Telefone pessoal: ").strip())
        endereco_residencial = input("Endereço residencial: ").strip()
        
        email_corporativo = input("E-mail corporativo: ").strip()
        while not self.validar_email(email_corporativo):
            print("E-mail inválido. Por favor, insira um e-mail válido.")
            email_corporativo = input("E-mail corporativo: ").strip()
        
        # Verificar se e-mail já existe
        if any(func['email_corporativo'] == email_corporativo for func in self.funcionarios):
            print("Erro: Já existe um funcionário cadastrado com este e-mail corporativo.")
            return
        
        horas_trabalho = input("Horas de trabalho por semana: ").strip()
        while not self.validar_horas_trabalho(horas_trabalho):
            print("Horas inválidas. Digite um número entre 0 e 168.")
            horas_trabalho = input("Horas de trabalho por semana: ").strip()
        horas_trabalho = float(horas_trabalho)
        
        salario_mensal = input("Salário mensal: R$ ").strip()
        while not self.validar_salario(salario_mensal):
            print("Salário inválido. Digite um número positivo.")
            salario_mensal = input("Salário mensal: R$ ").strip()
        salario_mensal = float(salario_mensal)
        
        funcionario = {
            'nome_funcionario': nome_funcionario,
            'cargo_funcao': cargo_funcao,
            'telefone_pessoal': telefone_pessoal,
            'email_corporativo': email_corporativo,
            'endereco_residencial': endereco_residencial,
            'horas_trabalho_semana': horas_trabalho,
            'salario_mensal': salario_mensal
        }
        
        self.funcionarios.append(funcionario)
        print("\nFuncionário cadastrado com sucesso!")
    
    def listar_funcionarios(self):
        """Lista todos os funcionários cadastrados"""
        print("\n--- Lista de Funcionários ---")
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado.")
            return
        
        for i, func in enumerate(self.funcionarios, 1):
            print(f"\nFuncionário {i}:")
            print(f"Nome: {func['nome_funcionario']}")
            print(f"Cargo/Função: {func['cargo_funcao']}")
            print(f"Telefone pessoal: {func['telefone_pessoal']}")
            print(f"E-mail corporativo: {func['email_corporativo']}")
            print(f"Endereço residencial: {func['endereco_residencial']}")
            print(f"Horas de trabalho por semana: {func['horas_trabalho_semana']}h")
            print(f"Salário mensal: R$ {func['salario_mensal']:.2f}")
    
    def buscar_funcionario(self, email):
        """Busca um funcionário pelo e-mail corporativo"""
        for func in self.funcionarios:
            if func['email_corporativo'] == email:
                return func
        return None
    
    def editar_funcionario(self):
        """Edita um funcionário existente"""
        print("\n--- Editar Funcionário ---")
        email = input("Digite o e-mail corporativo do funcionário que deseja editar: ").strip()
        funcionario = self.buscar_funcionario(email)
        
        if not funcionario:
            print("Funcionário não encontrado.")
            return
        
        print("\nDeixe em branco os campos que não deseja alterar.")
        
        novo_nome = input(f"Nome atual: {funcionario['nome_funcionario']}\nNovo nome: ").strip()
        if novo_nome:
            funcionario['nome_funcionario'] = novo_nome
        
        novo_cargo = input(f"Cargo atual: {funcionario['cargo_funcao']}\nNovo cargo: ").strip()
        if novo_cargo:
            funcionario['cargo_funcao'] = novo_cargo
        
        novo_telefone = input(f"Telefone atual: {funcionario['telefone_pessoal']}\nNovo telefone: ").strip()
        if novo_telefone:
            funcionario['telefone_pessoal'] = self.formatar_telefone(novo_telefone)
        
        novo_endereco = input(f"Endereço atual: {funcionario['endereco_residencial']}\nNovo endereço: ").strip()
        if novo_endereco:
            funcionario['endereco_residencial'] = novo_endereco
        
        novo_email = input(f"E-mail atual: {funcionario['email_corporativo']}\nNovo e-mail: ").strip()
        if novo_email:
            while not self.validar_email(novo_email):
                print("E-mail inválido. Por favor, insira um e-mail válido.")
                novo_email = input("Novo e-mail: ").strip()
            # Verificar se o novo e-mail já existe (exceto para o próprio funcionário)
            if any(func['email_corporativo'] == novo_email for func in self.funcionarios if func['email_corporativo'] != funcionario['email_corporativo']):
                print("Erro: Já existe um funcionário com este e-mail corporativo.")
                return
            funcionario['email_corporativo'] = novo_email
        
        novas_horas = input(f"Horas de trabalho atual: {funcionario['horas_trabalho_semana']}h\nNovas horas: ").strip()
        if novas_horas:
            while not self.validar_horas_trabalho(novas_horas):
                print("Horas inválidas. Digite um número entre 0 e 168.")
                novas_horas = input("Novas horas de trabalho: ").strip()
            funcionario['horas_trabalho_semana'] = float(novas_horas)
        
        novo_salario = input(f"Salário atual: R$ {funcionario['salario_mensal']:.2f}\nNovo salário: R$ ").strip()
        if novo_salario:
            while not self.validar_salario(novo_salario):
                print("Salário inválido. Digite um número positivo.")
                novo_salario = input("Novo salário: R$ ").strip()
            funcionario['salario_mensal'] = float(novo_salario)
        
        print("\nFuncionário atualizado com sucesso!")
    
    def excluir_funcionario(self):
        """Exclui um funcionário"""
        print("\n--- Excluir Funcionário ---")
        email = input("Digite o e-mail corporativo do funcionário que deseja excluir: ").strip()
        
        for i, func in enumerate(self.funcionarios):
            if func['email_corporativo'] == email:
                confirmacao = input(f"Tem certeza que deseja excluir {func['nome_funcionario']}? (S/N): ").strip().upper()
                if confirmacao == 'S':
                    del self.funcionarios[i]
                    print("Funcionário excluído com sucesso.")
                return
        
        print("Funcionário não encontrado.")

def menu():
    gerenciador = GerenciadorFuncionarios()
    
    while True:
        print("\n--- Sistema de Gerenciamento de Funcionários ---")
        print("1. Cadastrar novo funcionário")
        print("2. Listar todos os funcionários")
        print("3. Editar funcionário")
        print("4. Excluir funcionário")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == '1':
            gerenciador.cadastrar_funcionario()
        elif opcao == '2':
            gerenciador.listar_funcionarios()
        elif opcao == '3':
            gerenciador.editar_funcionario()
        elif opcao == '4':
            gerenciador.excluir_funcionario()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    menu()
