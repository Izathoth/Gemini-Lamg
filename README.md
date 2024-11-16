
# Documentação da Linguagem de Programação **Gemini**

## Acrônimo de **Gemini**

**G.E.M.I.N.I.**  
**G**eneral-purpose  
**E**xplicit  
**M**emory-manipulating  
**I**nterpreted  
**N**ew-age  
**I**nnovative  

## Visão Geral

Gemini é uma linguagem de programação projetada para ser simples e eficiente, com foco em manipulação básica de memória, incluindo variáveis e listas, e com tipagem estática. A linguagem foi inspirada por TypeScript e PHP, mas com uma sintaxe simplificada e moderna, ideal para desenvolvedores que desejam controle direto sobre a memória sem complexidade excessiva.

A tipagem estática oferece segurança ao código, garantindo que as variáveis sejam manipuladas de forma eficiente e sem erros de tipo. Gemini é uma linguagem interpretada, o que permite testes rápidos e uma experiência de desenvolvimento ágil.

## Características Principais

1. **Tipagem Estática**: Suporte para tipos básicos como `Number` e `String`, garantindo que o tipo da variável seja especificado na declaração e validado durante a execução.
2. **Manipulação de Memória**: Capacidade de trabalhar diretamente com variáveis e listas, permitindo fácil armazenamento e acesso a dados.
3. **Controle de Fluxo Básico**: Estruturas condicionais como `if (True)` e `if (False)` para controle de fluxo.
4. **Simplicidade e Clareza**: Sintaxe fácil de entender, baseada em conceitos de linguagens como PHP e TypeScript.

## Sintaxe

### Declaração de Variáveis

A declaração de variáveis em Gemini segue a estrutura:
```gemini
let <tipo> <nome_variavel> = <valor>;
```

- **Tipos disponíveis**:
  - `Number`: Tipo numérico (inteiros).
  - `String`: Tipo de texto (strings).

Exemplo:
```gemini
let Number age = 30;
let String name = "Alice";
```

### Atribuição de Valor

Após a declaração, você pode atribuir novos valores a uma variável já existente, como:
```gemini
age = 31;
name = "Bob";
```

Se tentar atribuir um valor de tipo incompatível, o interpretador gerará um erro.

### Controle de Fluxo

Gemini suporta estruturas condicionais simples, como `if`, que podem avaliar expressões booleanas:
```gemini
if (True)
    print("This will be printed!");

if (False)
    print("This will not be printed.");
```

A condição pode ser `True` ou `False`, ou também pode envolver uma variável booleana.

### Função de Impressão

Para exibir valores, a linguagem utiliza a função `print`, que pode ser usada da seguinte forma:
```gemini
print(age);  // Imprime o valor de 'age'
print(name); // Imprime o valor de 'name'
```

### Manipulação de Listas

Gemini também suporta manipulação de listas simples. As operações básicas como `push` e `pop` são utilizadas para adicionar e remover elementos de listas.

Exemplo de uso:
```gemini
let Number my_list = [1, 2, 3];
push(my_list, 4);  // Adiciona 4 à lista
pop(my_list);      // Remove o último item da lista
```

### Exemplo Completo

```gemini
let Number age = 30;
let String name = "Alice";
let Number balance = 1000;

print(age);
print(name);
print(balance);

if (True)
    print("Condition is True");

if (False)
    print("Condition is False");

age = 31;  // Atualizando a variável age
name = "Bob";  // Atualizando a variável name

print(age);
print(name);
```

## Funcionalidades e Funções

### Função `print`

- **Descrição**: Imprime o valor de uma variável ou expressão no console.
- **Sintaxe**: `print(<expressao>);`
- **Exemplo**:
  ```gemini
  print(age);  // Imprime o valor de 'age'
  ```

### Função `push`

- **Descrição**: Adiciona um valor ao final de uma lista.
- **Sintaxe**: `push(<lista>, <valor>);`
- **Exemplo**:
  ```gemini
  push(my_list, 5);  // Adiciona 5 à lista
  ```

### Função `pop`

- **Descrição**: Remove o último valor de uma lista.
- **Sintaxe**: `pop(<lista>);`
- **Exemplo**: 
  ```gemini
  pop(my_list);  // Remove o último item da lista
  ```

## Erros Comuns

### Erro de Tipo

Ao tentar atribuir um valor de tipo incompatível, o interpretador irá gerar um erro de tipo. Exemplo:

```gemini
let Number age = "Alice";  // Erro: Esperado um número, mas foi fornecida uma string
```

### Erro de Variável Não Declarada

Se você tentar acessar uma variável não declarada, o interpretador gerará um erro:
```gemini
print(unknown_var);  // Erro: variável 'unknown_var' não foi declarada
```

---


## Conclusão

A linguagem **Gemini** é projetada para ser simples, eficiente e segura, com foco em manipulação de memória, como variáveis e listas, e um sistema de tipagem estática que permite controle rigoroso sobre os tipos de dados. A linguagem é ideal para quem procura uma maneira eficiente de programar com um conjunto básico de funcionalidades, mas com a possibilidade de expandir conforme necessário.

Ao utilizar Gemini, os desenvolvedores podem escrever códigos simples e claros enquanto mantêm o controle total sobre as variáveis e seus tipos, tornando-a uma escolha ideal para aprendizado ou aplicações simples.



---


## Gemini - Informações

**Criador: Izathoth**

**Colaboradores: Izathoth**

**Versão: 0.12**

**Data de Publicação: 16/11/2024**

**Licença: Apache 2.0**
