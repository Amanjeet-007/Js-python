# JavaScript and Python

> Tip use  ;

Print something on
terminal/console (js/python)
---

```js
// JavaScript
console.log("Hello World");
```
```py
# python
print("Hello World");
```
## Variable and Constants
Variables :- which store/hold some value (like a container which can store something) 

we can divide the variables in two types 
* Changable variable
* Constant variables
>JS
* let (changable)
* const (contant)
#### example

```js
let name = "Amanjeet";
const role = "Admin"; 
```

>python
* just_name = ""  (changable)
* For contants use UPPERCASE for name 
```py
PI = 3.14;
name = "Rikky";
```

But you can change it also so it's like a polite agreement among programmers. if you see Uppercase Variable name so you have to know that it is a constant.

That's why yuu should declear it on the top of the file where imports are. it helps you to find it easily.,

## Data Types

| Python Datatypes 🐍   | JavaScript Datatypes 🕸️ | Description                                                                                                  |
|-----------------------|-------------------------|--------------------------------------------------------------------------------------------------------------|
| **Numeric Types**     |                         |                                                                                                              |
| `int`                 | `Number`                | Represents integer values (e.g., `10`, `-5`).                                                                |
| `float`               | `Number`                | Represents floating-point numbers (e.g., `3.14`, `-0.5`).                                                    |
| `complex`             |                         | Represents numbers with a real and imaginary part (e.g., `1 + 2j`).                                          |
| **Text Type**         |                         |                                                                                                              |
| `str`                 | `String`                | Represents sequences of characters enclosed in quotes (e.g., `"hello"`).                                     |
| **Boolean Type**      |                         |                                                                                                              |
| `bool`                | `Boolean`               | Represents one of two values: `True` or `False`.                                                             |
| **Sequence Types**    |                         |                                                                                                              |
| `list`                |                         | An ordered, mutable collection of items (e.g., `[1, 2, "a"]`).                                               |
| `tuple`               |                         | An ordered, immutable collection of items (e.g., `(1, 2, "a")`).                                             |
| `range`               |                         | Represents an immutable sequence of numbers.                                                                |
| **Mapping Type**      |                         |                                                                                                              |
| `dict`                | `Object`                | A collection of key-value pairs (e.g., `{"name": "Alice", "age": 30}`).                                      |
| **Set Types**         |                         |                                                                                                              |
| `set`                 |                         | An unordered collection of unique, immutable items.                                                          |
| `frozenset`           |                         | An immutable version of a set.                                                                               |
| **None Type**         |                         |                                                                                                              |
| `NoneType` (`None`)   | `null`                   | Represents the absence of a value or a null object.                                                          |
| **Symbol Type**       |                         |                                                                                                              |
|                       | `Symbol`                 | A unique, immutable value introduced in ES6, often used as object property keys.                             |
| **BigInt Type**       |                         |                                                                                                              |
|                       | `BigInt`                 | Used to represent integers with arbitrary precision, introduced in ES2020.                                   |
| **Undefined Type**    |                         |                                                                                                              |
|                       | `undefined`              | A primitive value that is automatically assigned to variables that have been declared but not yet initialized. |

### * How to check DataType
```js
// JavasSript
typeof()
```
```py
# Python
type()
```


## Input (users)

>Javascript
```js
// javascipt
prompt("What's your name?") //while using browser
// in Node
//first you have to import a module named readline
import readline from 'readline' //ES6
const readline = require('readline') //commonJS
//then create a interface
const rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
})
//then use question method to get input and show output
rl.question("What's your name? ",(data)=>{
    console.log(data);
    rl.close() // it' very important
})
```
>Python
```py
name = input("what's your name? ")
print(name);
# it's very simple in Python 😁
```

## Comment

comments are likes tagging code or commention something that javascript engines or interpreter(python) ignores. it's only writen for humans to make code more readable and understandable.

```py
// JavaScript

// 1. single line comment 

/*
2.
multi
line 
comment
*/
```
```js
// python
1. # single line comment
2. '''multiline comment'''
3. """multiline comment"""
 ```
## Operators
### Common Operator
```py
# these supports both languages (all languages)
Common_Operators = [
    Arithmetic :[
    + : "Addition",
    - : "Substraction",
    * : "Multiplication",
    / : "Division"
    % : "Modulo (returns the remainder)"],
    Comparison :[
        == : "Equal",
        != : "Not equal to",
        # >, <, >=, <=
    ],
    Logical:[
        # python / js formate
        "and / &&" : Logical AND
        "or / ||"  : Logical OR
        "not / !"  : Logical NOT
    ],
    Assignment:[
        =   : "simple assigment",
        +=  : "a += b means a = a + b",
        -=  : "a += b means a = a - b",
        *=  : "a += b means a = a * b",
        /=  : "a += b means a = a / b",
    ]
]
```
> In JS == (compares values) || === (compares values and datatype)
    same for != and !==

### Python specific Operators
** : Exponentiation (e.g., 2 ** 3 is 8)

// : Floor division (divides and returns the integer part; e.g., 7 // 3 is 2)

[ is, is not ] : Identity operators; check if two variables point to the same object in memory.

[ in, not in ]: Membership operators; check if a value is present in a sequence (like a list, tuple, or string).

### JavaScript specific Operators
[ ++, -- ] : Increment and decrement operators (add or subtract 1 from a number).

?:  : Ternary operator; a shorthand for an if/else statement (e.g., condition ? valueIfTrue : valueIfFalse).

