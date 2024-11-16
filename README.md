
# Gemini-Script Documentation

## Overview

Gemini-Script (GS) is a lightweight and modern programming language with static typing, designed to be simple and intuitive. Its syntax is inspired by languages like Python and JavaScript but with a more robust flow control structure, as well as support for basic types such as `Number`, `String`, and `Boolean`.

Gemini-Script allows for variable manipulation, flow control, functions, lists, and more. The language focuses on simplicity and code clarity.

---

## Basic Syntax

### 1. Variables

In Gemini-Script (GS), variables are declared using the `let` keyword, followed by the variable type, name, and value.

```text
let <Type> <variable_name> = <value>
```

- Variable Types:
  - `Number`: Numeric type used for integers.
  - `String`: Text type used for strings (text between quotes).
  - `Boolean`: Logical type used for `True` or `False` values.

**Example:**
```text
let Number age = 30
let String name = "Alice"
let Boolean is_active = True
```

---

### 2. Control Flow

#### Conditional `if`

The `if` statement checks if a condition is true and executes the corresponding block of code.

```text
if (<condition>)
    <statements>
```

- Example:
  ```text
  if (True)
      print("This will print because the condition is True")
  ```

#### Conditional `else`

The `else` block executes when the `if` condition is false.

```text
if (<condition>)
    <statements>
else
    <statements>
```

- Example:
  ```text
  if (False)
      print("This will not print")
  else
      print("This will print because the condition is False")
  ```

---

### 3. Functions

Functions can be defined using the `func` keyword, followed by the function name and body.

```text
func <function_name>()
    <statements>
```

**Example:**
```text
func greet()
    print("Hello, Gemini-Script!")
```

To call the function:
```text
greet()
```

---

### 4. Printing

The `print()` function is used to display values or variables to the console.

```text
print(<value>)
```

**Example:**
```text
print("Hello, Gemini-Script!")
```

---

### 5. Variable Assignment

Variables can be reassigned after their declaration using the `=` operator.

```text
<variable_name> = <new_value>
```

**Example:**
```text
age = 31
name = "Bob"
```

---

### 6. List Manipulation

You can manipulate lists with the `push` and `pop` commands.

- `push(<value>)`: Adds a value to the list.
- `pop()`: Removes the last value from the list.

**Example:**
```text
let List numbers = []
push(numbers, 10)
push(numbers, 20)
pop(numbers)
```

---

## Types

### 1. `Number`
Used for storing integer values.

- Example:
  ```text
  let Number age = 25
  ```

### 2. `String`
Used for storing text between quotes.

- Example:
  ```text
  let String name = "Gemini"
  ```

### 3. `Boolean`
Used for storing logical values: `True` or `False`.

- Example:
  ```text
  let Boolean is_active = True
  ```

---

## Control Flow

### 1. `if`

The `if` statement checks a boolean condition and executes the corresponding block of code.

```text
if (<condition>)
    <statements>
```

**Example:**
```text
if (True)
    print("Condition is true")
```

### 2. `else`

The `else` statement is used to execute an alternative block of code when the `if` condition is false.

```text
if (<condition>)
    <statements>
else
    <statements>
```

**Example:**
```text
if (False)
    print("This will not execute")
else
    print("This will execute")
```

---

## Errors and Debugging

Gemini-Script has a simple error control structure, including type checks and undeclared variable handling.

Example errors:
- **Type Error**: Attempting to assign a value of an incompatible type to a variable.
  ```text
  let Number age = "twenty"  # Error: Invalid value for age. Expected a Number.
  ```

- **Undeclared Variable Error**:
  ```text
  print(undeclared_variable)  # Error: undeclared_variable not defined.
  ```

---

## Examples

### 1. Hello World

```text
let String greeting = "Hello, Gemini-Script!"
print(greeting)
```

### 2. Simple Function

```text
func greet()
    print("Hello!")
greet()
```

### 3. Flow Control with `if` and `else`

```text
let Boolean is_logged_in = True

if (is_logged_in)
    print("Welcome!")
else
    print("Please log in.")
```

---

## Additional Information

- **Creator**: Izathoth
- **Contributors**: Izathoth
- **Version**: 0.12
- **Release Date**: 16/11/2024
- **License**: Apache 2.0

---

## Conclusion

Gemini-Script (GS) is an intuitive and simple language ideal for learning programming logic and for lightweight applications where static typing and flow control are required. Its syntax is easy to understand, and the language provides essential programming fundamentals in a clear manner.

---

### Next Steps
- Try writing your own programs in Gemini-Script!
- Explore more features, such as list manipulation and creating more complex functions.
