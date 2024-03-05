def reverseWords(s: str) -> str:
        # Split the string into words
        words = s.split()
        # Join the words back together with single spaces
        cleaned_sentence = ' '.join(words)
        # Split the cleaned sentence into words again
        words_reversed = cleaned_sentence.split(' ')
        # Reverse the order of the words
        reversed_sentence = words_reversed[::-1]
        # Concatenate the reversed words into a single string
        result = ''
        for i in range(len(reversed_sentence)):
            result += reversed_sentence[i]
            # Add a space after each word except the last one
            if i != len(reversed_sentence) - 1:
                result += ' '
        return result

print(reverseWords('Name my favourite song?'))