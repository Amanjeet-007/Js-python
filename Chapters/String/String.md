# String 
## > Examples are in /index.py and script.js
- *Immutability*:  
  In both languages, strings are **immutable** data types, meaning once a string is created, its content cannot be changed.
  
   Any method that appears to "modify" a string actually returns a **new string** with the desired changes.

#### Creating Strings
- **JavaScript**: 
>* single quotes (`'`)
>* double quotes (`"`)
>* backticks (`` ` ``) for template literals.
- **Python**: 
>* using single quotes (`'`)
>* double quotes (`"`)
>* Multi-line strings can be created using triple quotes (`""" """` or `''' '''`).

#### Accessing Characters
>**JS & Py**

 Both use zero-based indexing to access individual characters.  
  Example: `my_string[0]` gives you the first character.
> **Python only**: Supports negative indexing, e.g., `my_string[-1]` gives the last character. (JS does not support this natively.)

---

### Common String Methods

| Functionality         | JavaScript (JS)                    | Python (Py)                      |
|-----------------------|------------------------------------|----------------------------------|
| **Length**            | `str.length` (property)            | `len(str)` (function)            |
| **Case Conversion**   | `str.toUpperCase()`, `str.toLowerCase()` | `str.upper()`, `str.lower()` |
| **Trim Whitespace**   | `str.trim()`, `str.trimStart()`, `str.trimEnd()` | `str.strip()`, `str.lstrip()`, `str.rstrip()` |
| **Split String**      | `str.split(separator)`             | `str.split(separator)`            |
| **Join Array/List**   | `arr.join(separator)`              | `separator.join(list)`            |
| **Replace Substring** | `str.replace(old, new)`            | `str.replace(old, new)`           |
| **Find Substring**    | `str.indexOf(sub)`, `str.includes(sub)` | `str.find(sub)`, `sub in str`   |
| **Prefix/Suffix**     | `str.startsWith(sub)`, `str.endsWith(sub)` | `str.startswith(sub)`, `str.endswith(sub)` |

---

### Detailed Method Comparisons

**Finding and Checking**

>JS `indexOf()` || Py `find()`
- Both return the starting index of the first occurrence of a substring.
- If not found:
  - JS `indexOf()` → `-1`
  - Py `find()` → `-1`

>JS `includes()` || Py `in` operator
- JS: `includes()` returns `true`/`false`.
- Py: `in` is an operator that directly checks for membership.