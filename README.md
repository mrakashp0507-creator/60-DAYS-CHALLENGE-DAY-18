# Day 18 - Balanced Brackets Validator

## 📌 Overview

This project implements a Balanced Brackets Validator using a Stack.

An ancient civilization stored messages using nested brackets.
Before decoding the message, we need to verify whether the brackets
are properly balanced.

The program supports:

- Round brackets: ()
- Square brackets: []
- Curly brackets: {}

---

## 🎯 Objective

The program validates whether a message contains properly balanced
and correctly ordered brackets.

Example:

{[()]}

is balanced.

But:

([)]

is not balanced.

---

## 🧠 Stack Concept

A Stack follows the LIFO principle:

Last In, First Out

When an opening bracket is found, it is pushed into the stack.

When a closing bracket is found:

1. Check whether the stack is empty.
2. Remove the top element.
3. Compare it with the expected opening bracket.
4. If they do not match, the sequence is invalid.

At the end, the stack must be empty for the message to be balanced.

---

## 🔄 Algorithm

1. Create an empty stack.
2. Read the message character by character.
3. If the character is an opening bracket:
   - Push it into the stack.
4. If the character is a closing bracket:
   - Check if the stack is empty.
   - Pop the top bracket.
   - Compare it with the matching opening bracket.
5. If any mismatch occurs, return False.
6. After processing the complete message:
   - Empty stack → Balanced
   - Non-empty stack → Not Balanced

---

## 🧪 Examples

### Valid

{[()]}

Output:

Balanced

### Invalid

([)]

Output:

Not Balanced

### Invalid

{[()]

Output:

Not Balanced

---

## ⏱️ Complexity

### Time Complexity

O(n)

Each character is processed once.

### Space Complexity

O(n)

In the worst case, all opening brackets can be stored in the stack.

---

## 🌍 Real-World Applications

Stacks are commonly used in:

- Compilers
- HTML validation
- IDE syntax checking
- Parsing engines
- Expression evaluation
- Programming language interpreters

---

## ▶️ How to Run

Open the terminal in VS Code.

Run:

python day18_balanced_brackets.py

Enter a message containing brackets.

Example:

{[()]}

The program will display whether the brackets are balanced.

---

## 📂 Project Structure

day18/
│
├── day18_balanced_brackets.py
└── README.md

---

## 🚀 Learning Outcome

Through this project, I learned:

- Stack data structure
- LIFO principle
- Push and pop operations
- Bracket matching
- Edge-case handling
- Time and space complexity
