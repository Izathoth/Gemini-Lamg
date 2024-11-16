class GeminiScriptInterpreter:
    # Inicializa a classe com um dicionário de variáveis
    def __init__(self):
        self.variables = {}  # Armazena variáveis e seus valores

    # Função principal que executa o código linha por linha
    def execute(self, code):
        lines = code.strip().split('\n')  # Divide o código em linhas
        block_stack = []  # Pilha para controlar blocos de if/else
        for line in lines:
            line = line.strip()  # Remove espaços extras

            if line.startswith("let"):  # Declaração de variável
                self.handle_declaration(line)
            elif line.startswith("func"):  # Declaração de função (não implementado)
                self.handle_function(line)
            elif line.startswith("if"):  # Condição if
                self.handle_if(line, block_stack)
            elif line.startswith("else"):  # Bloco else
                self.handle_else(line, block_stack)
            elif "print" in line:  # Comando print
                self.handle_print(line)
            elif "=" in line:  # Atribuição de valor
                self.handle_assignment(line)

    # Lida com a declaração de variáveis
    def handle_declaration(self, line):
        """Declara variáveis com tipos específicos (Number, String, Boolean)"""
        parts = line.split('=')
        var_declaration = parts[0].replace("let", "").strip()
        var_type, var_name = var_declaration.split(' ', 1)
        value = parts[1].strip()

        # Atribui valor com base no tipo
        if var_type == "Number" and value.isdigit():
            self.variables[var_name] = int(value)
        elif var_type == "String" and value.startswith('"') and value.endswith('"'):
            self.variables[var_name] = value.strip('"')
        elif var_type == "Boolean" and value.lower() in ["true", "false"]:
            self.variables[var_name] = value.lower() == "true"
        else:
            print(f"Error: Unsupported type or invalid value for {var_name}.")

    # Lida com a atribuição de valor a variáveis já declaradas
    def handle_assignment(self, line):
        """Atribui valor a uma variável existente"""
        var_name, value = line.split('=')
        var_name = var_name.strip()
        value = value.strip()

        if var_name in self.variables:
            current_type = type(self.variables[var_name])
            if current_type == int and value.isdigit():
                self.variables[var_name] = int(value)
            elif current_type == str and value.startswith('"') and value.endswith('"'):
                self.variables[var_name] = value.strip('"')
            elif current_type == bool and value.lower() in ["true", "false"]:
                self.variables[var_name] = value.lower() == "true"
            else:
                print(f"Error: Type mismatch for {var_name}.")
        else:
            print(f"Error: {var_name} not declared.")

    # Lida com o comando print para exibir valores de variáveis
    def handle_print(self, line):
        """Imprime o valor de uma variável"""
        var_name = line.split('(')[1].split(')')[0].strip()
        if var_name in self.variables:
            print(self.variables[var_name])
        else:
            print(f"Error: {var_name} not defined.")

    # Lida com o comando if para verificar condições
    def handle_if(self, line, block_stack):
        """Avalia uma condição e executa o bloco if se for verdadeira"""
        condition = line.split('(')[1].split(')')[0].strip()
        condition_value = self.evaluate_condition(condition)

        if condition_value:
            block_stack.append('if')
            print("Condition is True")
        else:
            block_stack.append('else')
            print("Condition is False")

    # Lida com o comando else, executando o bloco quando o if não é verdadeiro
    def handle_else(self, line, block_stack):
        """Executa o bloco else se o if anterior for falso"""
        if block_stack and block_stack[-1] == 'if':
            print("Executing else block")
        else:
            print("Error: Else without corresponding If block")

    # Avalia a condição para o comando if
    def evaluate_condition(self, condition):
        """Verifica se a condição é verdadeira ou falsa"""
        if condition == "True":
            return True
        elif condition == "False":
            return False
        elif condition in self.variables:
            return self.variables[condition]
        else:
            print(f"Error: Condition {condition} not recognized.")
            return False

# Código de exemplo a ser executado
code = """
let Number age = 30
let String name = "Alice"
let Number balance = 1000
let String message = "Hello, World!"
let Number height = 5

print(age)
print(name)
print(balance)
print(message)

if (True)
    print("This should be printed because the condition is True")

if (False)
    print("This should not be printed because the condition is False")

let Boolean is_active = True
if (is_active)
    print("The user is active")
else
    print("The user is not active")
"""

# Cria uma instância do interpretador e executa o código
interpreter = GeminiScriptInterpreter()
interpreter.execute(code)
