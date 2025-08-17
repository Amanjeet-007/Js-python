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

## Print something on terminal/console (js/python)

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
## Function
function is a block || set of code which perform some task and this is reusable things.

### Declaration
> In Javascript we can make function in mainly three ways
* function declaration
* function expression
* Arrow function
```js  
// javaScript

// function Declaration
  // making function with basic syntax
function greet(){
  console.log("Hello User.");
}
// -- -- -- -- -- -- -- -- -- -- -- -- -- -- - -- - - 
//function expression 
  // assiging a function to a variable 
const greet_2 = function(){
  console.log("Hello Bro");
} 
// -- -- -- -- -- -- -- -- -- -- -- -- -- -- - -- - - 
//Arrow function 
const sayHello = ()=>{
  console.log("Hello World");
}
 ```

 > In Python we can make function in two way
 * Normal function Declaration
 * lambda function
 ```py
 # Python

 # Function Declaration
 def greet():
  print("Hello User")

# lambda function
add = lambda a,b : a+b
print(add(3,2)) #5
  ```
### Parameter and Argument
>Parameter

It's a variable which is get listed in function while Declaration. 
initialy it's not have any value when we call the function then we have to pass it.

>Argument

Argument: a value which we pass to a function to work.

#### we also can set default value to Parameter > it will work when we don't get any value while calling.
Eample
```js 
// JavaScript
//declere any function
function greet(name){ // here name is parameter
 console.log(`hello ${name}`) // hello name(which we get while calling the function)
}

//call the function
greet("Amanjeet") // pass a name in it
//output will be > hello Amanjeet
```
> Default parameter
```js
// Javascript
function greet(name = "Guest") {
  console.log(`Hello, ${name}!`);
}
 ```
```py
def f(*args, **kwargs):
    print(args, kwargs)
f(1, 2, a=3)
 ```
we can set specific name for parameter
but in this example ***args** (which can accept multiple argument as parameter and return a tuple of argument value) and ***kwargs** which accept multiple argument as key:value pair
```py
 def my_function(
    100,             # first_arg
    1, 2, 3,         # *args
    name="Bob",      # **kwargs
    city="New York"  # **kwargs
):

```
### Return value
Every function returns some value by default and manually

```js
function sum(a,b){
  return (a+b) // return the value
}
//we can use it like following method
const answer = sum(3,4)
console.log(answer) // 7
// return statement return the value and we can assign the value into any varible we want and use it (if needed 😁)
```
In js if we don't return any value manually it will return
UNDEFINED itself.
```py
def multiply(a,b):
  return a*b
answer = multiply(4,6) # 24
print(answer) # 24
 ```
 In python if we don't return any value manually then it return NONE itself

>JavaScript specific things
* Function declarations are hoisted in Js : it means we can use the function before it's Declaration 
* But Function expressions and arrow functions not support hoisting it will throw error > TypeError/ReferenceError
> Hoisting is a Very Intrusting thing if you want to know more about it i Will Add the section for it.

>Python specific things
* Docstring : it's like comment but much more than comment
we can define it as the first statement
and we can see while runtime. 

(it's like we can make a document of the function information like what it does there Parameter etc.)
```py
def add_numbers(a, b):
    """
    This function takes two numbers as arguments and returns their sum.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

# You can access the docstring like this:
print(add_numbers.__doc__)
```
## Scope
so scope it a way to know which variable is accessable from where.
        
          we  have basically Two types of scope 
          1. Global scope
          2. Block scope
          Global scope :- these variable are accessable from anywhere because they are defined globally 

          Block scope :- these vaiable are only accessable in the block where they are defined
          let's see example:-
```js

let a = 10  // global scope variable
function block(){
  let b = 20; // block scope variable
  // we can access a and b here 
  // a cause it is a global variable
  // b cause it's created in the same block 
  // b can't be access from other block until it's send to that as argument
}
//here we can access a
console.log(a) // 10
console.log(b) // undefined
// we can't access b here 
// **** block means = {} 
```






   
  



