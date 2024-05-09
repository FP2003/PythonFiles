def simplifyPath(path: str) -> str:
    # Initialize an empty stack to store valid parts of the path
    stack = []
    
    # Split the input path by '/' delimiter and iterate over each part
    for char in path.split('/'):
        # If the part is '..', pop the last element from the stack if it's not empty
        if char == '..':
            if stack:
                stack.pop()
        # If the part is not empty, not '.' and not '/', append it to the stack
        elif char and char != '.' and char != '/':
            stack.append(char)
    
    # Construct the simplified path by joining the parts in the stack with '/' and adding '/' at the beginning
    return '/' + '/'.join(stack)

print(simplifyPath('/Document/Files/../Downloads/'))