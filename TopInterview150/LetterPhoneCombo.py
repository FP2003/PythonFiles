from typing import List


def letterCombinations(digits: str) -> List[str]:
        keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
        if not digits:
            return []
        
        def backtracking(indx, comb):
            if indx == len(digits):
                result.append(comb)
                return
            
            for letter in keyboard[digits[indx]]:
                backtracking(indx + 1, comb + letter)
        
        result = []
        backtracking(0, "")
        
        return result
    
print(letterCombinations("56"))