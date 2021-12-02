class FullAdderCircuit : 
    def __init__(self, firstNumber, secondNumber) : 
        self.firstNumber = self.convertToBinary(firstNumber)
        self.secondNumber = self.convertToBinary(secondNumber)
        self.result = []

    def add(self) : 
        carry = 0
        firstNumberIterator = 0
        secondNumberIterator = 0

        print(self.firstNumber[::-1])
        print(self.secondNumber[::-1])

        while(firstNumberIterator < len(self.firstNumber) or secondNumberIterator < len(self.secondNumber) or carry) :
            firstDigit = 0 if firstNumberIterator >= len(self.firstNumber) else self.firstNumber[firstNumberIterator]
            secondDigit = 0 if secondNumberIterator >= len(self.secondNumber) else self.secondNumber[secondNumberIterator]
            
            sum, carry = FullAdder(firstDigit, secondDigit, carry).getResult()

            self.result = [*self.result, sum]

            firstNumberIterator += 1
            secondNumberIterator += 1
        
        if(len(self.result) > 4) : 
            tempResult = self.result[0:4]
            self.result = tempResult[::-1]

    def convertToBinary(self, numberInString) : 
        binary = []
        i = 0
        while(i < len(numberInString)) :
            binary = [*binary, int(numberInString[i])]
            i += 1
        
        return binary[::-1]
        

class FullAdder:
    def __init__(self, firstDigit, secondDigit, carry) : 
        self.firstDigit = firstDigit
        self.secondDigit = secondDigit
        self.carry = carry

    def getResult(self) :
        sum = self.firstDigit ^ self.secondDigit ^ self.carry
        carry = (self.firstDigit & self.secondDigit) | (self.secondDigit & self.carry) | (self.carry & self.firstDigit)
        return sum, carry

    
firstNumber = input("Enter the first number: ")
secondNumber = input("Enter the second number: ")

FullAdderObject = FullAdderCircuit(firstNumber, secondNumber)
FullAdderObject.add()
print(FullAdderObject.result)