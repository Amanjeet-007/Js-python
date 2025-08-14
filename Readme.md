# JavaScript and Python
LIST OF CONTENT you can see ➡️⬆️ (left top corner)  <svg
    xmlns="http://www.w3.org/2000/svg"
    width="16"
    height="16"
    fill="currentColor"
    style="vertical-align:text-bottom"
    viewBox="0 0 16 16">
    <path d="M5.75 2.5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5Zm0 5h8.5a.75.75 0 0 1 0 1.5h-8.5a.75.75 0 0 1 0-1.5ZM2 14a1 1 0 1 1 0-2 1 1 0 0 1 0 2Zm1-6a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM2 4a1 1 0 1 1 0-2 1 1 0 0 1 0 2Z"></path>
</svg> 
icon click and see

> Tip use  ;

## Print something on
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
Variables :- which ( store | | hold ) some value (like a container which can store something) 

we can divide the variables in two types 
* Changable variable
* Constant variables
>JS
* let (changable)
* const (contant)
#### example

```js
let age = 21;
const Admin = "Amanjeet"; 
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

## **JavaScript Data Types**

### **1. Primitive Types**
- **String** → `"Hello World"`, `'JS'`, `` `Template` ``
- **Number** → `42`, `3.14`, `-7`
- **BigInt** → `123456789012345678901234567890n`
- **Boolean** → `true`, `false`
- **Undefined** → `let x; console.log(x); // undefined`
- **Null** → `let y = null;`
- **Symbol** → `Symbol('unique')`

### **2. Non-Primitive (Reference) Types**
- **Object** → `{ name: "John", age: 30 }`
- **Array** → `[1, 2, 3, 4]`
- **Function** → `function greet() { console.log("Hi"); }`
- **Promise** → `new Promise((resolve, reject) => { /* ... */ }) / Promise.resolve(42)`
- **Date** → `new Date()`
- **RegExp** → `/\d+/g`
- **Map** → `new Map([["key", "value"]])`
- **Set** → `new Set([1, 2, 3])`
- **WeakMap** → `new WeakMap()`
- **WeakSet** → `new WeakSet()`

---

## **Python Data Types**

### **1. Basic Types**
- **int** → `42`, `-10`, `0`
- **float** → `3.14`, `-7.5`
- **complex** → `3+4j`
- **str** → `"Hello"`, `'World'`
- **bool** → `True`, `False`
- **NoneType** → `None`

### **2. Sequence Types**
- **list** → `[1, 2, 3]`
- **tuple** → `(1, 2, 3)`
- **range** → `range(5)`

### **3. Set Types**
- **set** → `{1, 2, 3}`
- **frozenset** → `frozenset([1, 2, 3])`

### **4. Mapping Type**
- **dict** → `{"name": "Alice", "age": 25}`

### **5. Other Built-in Types**
- **bytes** → `b"Hello"`
- **bytearray** → `bytearray([65, 66, 67])`
- **memoryview** → `memoryview(b"Hello")`

---

## 🆚 **Key Differences**
| Feature | JavaScript | Python |
|---------|-----------|--------|
| **Dynamic Typing** | ✅ | ✅ |
| **Null/None** | `null`, `undefined` | `None` |
| **BigInt Support** | ✅ | ❌ (Uses `int` for arbitrarily large numbers) |
| **Symbols** | ✅ | ❌ |
| **Complex Numbers** | ❌ | ✅ |
| **Functions as Values** | ✅ | ✅ (functions are first-class objects) |

---

> 💡 **Tip:** Both JavaScript and Python are **dynamically typed**, meaning variable types are determined at runtime.


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

### Common Operators (Both Languages)

| Type        | Python 🐍 Syntax / JS 🕸️ Syntax | Description |
|-------------|--------------------------------|-------------|
| **Arithmetic** | `+` | Addition |
|             | `-` | Subtraction |
|             | `*` | Multiplication |
|             | `/` | Division |
|             | `%` | Modulo (remainder) |
|             | `**` | Exponentiation (e.g., `2 ** 3` → 8) |
| **Comparison** | `==` | Equal to *(JS: compares values only)* |
|             | `!=` | Not equal *(JS: compares values only)* |
|             | `>` `<` `>=` `<=` | Greater/less than, etc. |
|             | `===` *(JS only)* | Equal (value + type) |
|             | `!==` *(JS only)* | Not equal (value + type) |
| **Logical** | `and` / `&&` | Logical AND |
|             | `or` /  ||   | Logical OR |
|             | `not` / `!`  | Logical NOT |
| **Assignment** | `=` | Assign value |
|               | `+=` | `a += b` → `a = a + b` |
|               | `-=` | `a -= b` → `a = a - b` |
|               | `*=` | `a *= b` → `a = a * b` |
|               | `/=` | `a /= b` → `a = a / b` |

---
>| | means OR in JavaScript 
### Python-Specific Operators
| Operator | Description |
|----------|-------------|
| `//` | Floor division (integer part of division, e.g., `7 // 3` → 2) |
| `is`, `is not` | Identity operators; check if two variables point to the same object in memory |
| `in`, `not in` | Membership operators; check if a value exists in a sequence |

---

### JavaScript-Specific Operators
| Operator | Description |
|----------|-------------|
| `++`, `--` | Increment or decrement by 1 |
| `? :` | Ternary operator (e.g., `condition ? valueIfTrue : valueIfFalse`) |

## Controle Flow

> Controle is mainly divided into two Parts these are
* Conditionals
* Loops

### 1. Conditionals
    if
    if else
    if else if else
    -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
    switch (js) || match (py)

But how we write in the JS and Python
```js
// JavaScript
//- -- - - - - - - - - - - - - - - - - -- - - - - - - - - 
// if statement
let temperature = 25;
if (temperature > 20) {
  // This code runs if the condition is true
  console.log("It's a warm day.");
}

//- -- - - - - - - - - - - - - - - - - -- - - - - - - - - 
// if else statement
let age = 17;
if (age >= 18) {
  // This code runs if the condition is true
  console.log("You can vote.");
} else {
  // This code runs if the condition is false
  console.log("You cannot vote yet.");
}

//- -- - - - - - - - - - - - - - - - - -- - - - - - - - - 
// if else if else statement
let score = 85;
if (score >= 90) {
  // Checks if the score is 90 or higher
  console.log("Grade: A");
} else if (score >= 80) {
  // Checks if the score is 80-89
  console.log("Grade: B");
} else {
  // Runs if all previous conditions are false
  console.log("Grade: C");
}
```

```py
# Python
#- -- - - - - - - - - - - - - - - - - -- - - - - - - - - 
# if statement
temperature = 25
if temperature > 20:
    # This code runs if the condition is true
    print("It's a warm day.")

#- -- - - - - - - - - - - - - - - - - -- - - - - - - - - 
# if else statement
age = 17
if age >= 18:
    # This code runs if the condition is true
    print("You can vote.")
else:
    # This code runs if the condition is false
    print("You cannot vote yet.")

#- -- - - - - - - - - - - - - - - - - -- - - - - - - - - 
# if elif else statement
score = 85
if score >= 90:
    # Checks if the score is 90 or higher
    print("Grade: A")
elif score >= 80:
    # Checks if the score is 80-89
    print("Grade: B")
else:
    # Runs if all previous conditions are false
    print("Grade: C")
```

#### Switch Case
```js
// JavaScript
let day = "Tue";                    // A variable
switch (day) {
  case "Mon":                // Compare in cases
    console.log("It's Monday.");  // Result by cases
    break;          // break if find one case true
  case "Tue":
    console.log("It's Tuesday.");
    break;
  case "Wed":
    console.log("It's Wednesday.");
    break;
  default:
    console.log("It's another day.");
}
```
> break

The break keyword is crucial. Without it, the code will "fall through" and execute the code for the next case as well.
> default

The default keyword is optional but recommended; it specifies the code to run if none of the case clauses match.

> continue

```py
# Python
day = "Tue"
match day:
  case "Mon":
    print("It's Monday.")
  case "Tue":
    print("It's Tuesday.")
  case "Wed":
    print("It's Wednesday.")
  case _:
    print("It's another day.")
 ```
 >No need of Break

 The match statement does not need a break statement; it automatically stops after the first successful match.
 >_

 The _ (underscore) is used as a wildcard pattern. It acts like the default clause in a JavaScript switch statement, matching anything if no other pattern has matched.
 > Important

 Python's match is more flexible than JavaScript's switch; it can match on more than just simple values, including tuples, lists, and objects.

### 2. Loops
      JavaScript
      - for loop
      - for-of loop
      - for-in loop
      - while
      - do-while

      Python
      - for loop
      - while loop

```js
// JavaScript

   // for loops
for(let i = 0 ;i <5; i++){
  console.log(i) //this loop will print 1 to 5
}
//-  -  -  -  -  -  -  -   -  -  -  -  -  -  -  --  
    // for of loop
const arr = [1, 2, 3];
for (const item of arr) {
  console.log(item); //will print all iteam from arr
}
//-  -  -  -  -  -  -  -   -  -  -  -  -  -  -  --  
    // for in loop
const obj = {a: 1, b: 2};
for (const key in obj) {
  console.log(key); //will return the indexes
}
//-  -  -  -  -  -  -  -   -  -  -  -  -  -  -  --  
    // while
let i = 0;
while (i < 5) {
  console.log(i) // 0 tp 4 (run 5 times)
  i++;
}
//-  -  -  -  -  -  -  -   -  -  -  -  -  -  -  --  
    // do while
    //--> this loop will run minimun one change then check the conditon
let i = 0;
do {
  console.log(i)
  i++;
} while (i < 5);

 ```
 ```py
 # Python
    # for Loop
for i in range(5):
  print(i) # 0 to 4 (5 times)
# in arr 
arr = [4,2,1];
for i in arr:
  print(i) # print all the iteams from arr
#-  -  -  -  -  -  -  -   -  -  -  -  -  -  -  -
    # while Loop  
i = 0
while i < 5:
  print(i) # 0 to 4 (5 times)
  i += 1 # here you can't use i++ (as you know it's not support in python)


  ```



   
  



