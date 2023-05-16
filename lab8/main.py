from abc import ABC, abstractmethod

class FileHandler(ABC):
    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass
class ListCount(FileHandler):
    def calculateFreqs(self):
        firstList = [0] * 26

        with open(self.address, 'r') as file:
            for row in file:
                for char in row:
                    if char.isalpha():
                        index = ord(char.lower()) - ord('a')
                        firstList[index] += 1


        for i, frequent in enumerate(firstList):
            if frequent > 0:
                letter = chr(i + ord('a'))
                print(f"{letter} = {frequent}")
class DictCount(FileHandler):
    def calculateFreqs(self):
        second_dict = {}

        with open(self.address, 'r') as file:
            for row2 in file:
                for char in row2:
                    if char.isalpha():
                        char = char.lower()
                        second_dict[char] = second_dict.get(char, 0) + 1


        for letter, freq in second_dict.items():
            print(f'"{letter}" {freq}')

list_count = ListCount("weirdWords.txt")
dict_count = DictCount("weirdWords.txt")


print("ListCount:")
list_count.calculateFreqs()

print("\nDictCount:")
dict_count.calculateFreqs()
