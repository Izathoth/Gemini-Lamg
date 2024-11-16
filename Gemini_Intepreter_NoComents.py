class GeminiScriptInterpreter:
    def __init__(self):
        self.variables = {}  # Dicionário para armazenar variáveis e listas

    def execute(self, code):
        lines = code.strip().split('\n')
        block_stack = []  # Pilha para controlar os blocos de if/else
        for line in lines:
            line = line.strip()
            if line.startswith("let"):  # Declaração de variável com tipo
                self.handle_declaration(line)
            elif line.startswith("func"):  # Declaração de função
                self.handle_function(line)
            elif line.startswith("if"):  # Controle de fluxo
                self.handle_if(line, block_stack)
            elif line.startswith("else"):  # Controle de fluxo - else
                self.handle_else(line, block_stack)
            elif "print" in line:  # Comando de print
                self.handle_print(line)
            elif "=" in line:  # Atribuição
                self.handle_assignment(line)
            elif "push" in line or "pop" in line:  # Manipulação de listas
                self.handle_list_operations(line)

    def handle_declaration(self, line):
        """Declara variáveis com tipagem estática"""
        parts = line.split('=')
        # Remover a palavra 'let' e dividir corretamente o tipo e o nome da variável
        var_declaration = parts[0].replace("let", "").strip()
        var_type, var_name = var_declaration.split(' ', 1)
        value = parts[1].strip()

        if var_type == "Number":  # Tipo Number
            if value.isdigit():
                self.variables[var_name] = int(value)
            else:
                print(f"Error: Invalid value for {var_name}. Expected a Number.")
        elif var_type == "String":  # Tipo String
            if value.startswith('"') and value.endswith('"'):
                self.variables[var_name] = value.strip('"')
            else:
                print(f"Error: Invalid value for {var_name}. Expected a String.")
        elif var_type == "Boolean":  # Tipo Boolean
            if value.lower() == "true":
                self.variables[var_name] = True
            elif value.lower() == "false":
                self.variables[var_name] = False
            else:
                print(f"Error: Invalid value for {var_name}. Expected True or False.")
        else:
            print(f"Error: Unsupported type {var_type} for variable {var_name}.")

    def handle_assignment(self, line):
        """Atribui valor a uma variável, com verificação de tipo"""
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
                print(f"Error: Type mismatch for {var_name}. Expected {current_type}.")
        else:
            print(f"Error: {var_name} not declared.")

    def handle_print(self, line):
        """Imprime o valor de uma variável"""
        var_name = line.split('(')[1].split(')')[0].strip()
        if var_name in self.variables:
            print(self.variables[var_name])
        else:
            print(f"Error: {var_name} not defined.")

    def handle_if(self, line, block_stack):
        """Controle de fluxo básico (if)"""
        condition = line.split('(')[1].split(')')[0].strip()
        condition_value = self.evaluate_condition(condition)

        # Se a condição for verdadeira, adiciona à pilha e executa o bloco
        if condition_value:
            block_stack.append('if')
            print("Condition is True")
        else:
            block_stack.append('else')
            print("Condition is False")

    def handle_else(self, line, block_stack):
        """Controle de fluxo básico (else)"""
        if block_stack and block_stack[-1] == 'if':
            print("Executing else block")
        else:
            print("Error: Else without corresponding If block")

    def evaluate_condition(self, condition):
        """Avalia uma condição, considerando valores booleanos e variáveis"""
        if condition == "True":
            return True
        elif condition == "False":
            return False
        elif condition in self.variables:
            return self.variables[condition]
        else:
            print(f"Error: Condition {condition} not recognized.")
            return False

    def handle_list_operations(self, line):
        """Manipulação de listas (push, pop)"""
        if "push" in line:
            var_name = line.split('(')[1].split(')')[0].strip()
            self.variables[var_name].append(int(line.split('=')[1].strip()))
        elif "pop" in line:
            var_name = line.split('(')[1].split(')')[0].strip()
            self.variables[var_name].pop()

# Código Gemini-Script com controle de fluxo e condições True/False
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

let Number another_age = 25
another_age = "twenty five"  # This should trigger a type error
"""

# Inicializar e executar o interpretador
interpreter = GeminiScriptInterpreter()
interpreter.execute(code) #
