class PalindromeNumber:

    def __init__(self, number: int):
        self.number = abs(number)

    def is_palindrome(self) -> bool:
        stringified = self.__stringify()
        print(stringified)
        stop = len(stringified) // 2

        left = 0
        right = -1
        answer = True
        while left <= stop and answer == True:
            if stringified[left] != stringified[right]:
                answer = False
            left += 1
            right -= 1
        return answer

    def __stringify(self) -> str:
        return str(self.number)
