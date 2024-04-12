def decodeString(s: str) -> str:
    # Initialize an empty stack to store (string, repetition_count) tuples
    stack = []
    # Initialize variables to track current substring and its repetition count
    curr_num = 0
    curr_str = ''

    # Iterate through each character in the input string
    for char in s:
        # If the character is a digit, accumulate it to form a multi-digit number
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)
        # If the character is an opening bracket '[', push current substring and repetition count onto the stack
        elif char == '[':
            stack.append((curr_str, curr_num))
            # Reset current substring and repetition count
            curr_str = ''
            curr_num = 0
        # If the character is a closing bracket ']', pop previous substring and its repetition count from the stack
        elif char == ']':
            prev_str, num = stack.pop()
            # Update current substring by repeating it num times and concatenating with previous substring
            curr_str = prev_str + curr_str * num
        # If the character is a regular character, append it to the current substring
        else:
            curr_str += char
    
    # Return the final decoded string
    return curr_str
