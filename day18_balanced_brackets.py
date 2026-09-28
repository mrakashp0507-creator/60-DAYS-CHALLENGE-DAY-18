# Day 18 - Stack
# Balanced Brackets Validator

def is_balanced(message):
    stack = []

    matching_brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in message:

        # Opening bracket
        if char in "([{":
            stack.append(char)

        # Closing bracket
        elif char in ")]}":

            # No opening bracket available
            if not stack:
                return False

            # Check whether the brackets match
            top = stack.pop()

            if top != matching_brackets[char]:
                return False

    # If stack is empty, all brackets were balanced
    return len(stack) == 0


print("=== Balanced Brackets Validator ===")

message = input("Enter a message with brackets: ")

if is_balanced(message):
    print("\nResult: Balanced")
    print("The message can be safely decoded.")
else:
    print("\nResult: Not Balanced")
    print("The message contains invalid bracket ordering.")