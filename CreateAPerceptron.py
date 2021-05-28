import random
#Algorithm taken from https://en.wikipedia.org/wiki/Perceptron
class Perceptron():
    def __init__(self, inputs):
        self._inputDict = {}
        #Configures a dictionary where the key is the input number and the first value is the input value. Second value is the weight
        for i in range(inputs):
            self._inputDict[i]=[1,random.uniform(-1,1)]
        
    def classify(self, record):
        #Record should be formatted as a list
        #Only use the first 16 values of record, as the 17th is the party affiliation
        for i in range(len(record)-1):
            if record[i] != -1 and record[i] != 1:
                record[i] = 0
            self._inputDict[i][0] = record[i]
        return self.calculate()
        
    def train(self, expectedOutput, output, record):
        #Expected output/output are a -1 or 1, record is a list
        for i in range(len(record)-1):
            if record[i] != -1 and record[i] != 1:
                record[i] = 0
            self._inputDict[i][0] = record[i]
        current = self.calculate()
        error = int(expectedOutput) - int(current)
        for i in range(len(self._inputDict)):
            self._inputDict[i][1] = self._inputDict[i][1] + (error * record[i])      
        
    def calculate(self):
        total = 0
        for i in self._inputDict:
            total = total + (self._inputDict[i][0]*self._inputDict[i][1])
        if total >= 0:
            return 1
        else:
            return 0
        
