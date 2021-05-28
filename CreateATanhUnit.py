import numpy
import random

class TanhUnit():
    def __init__(self, inputs):
        self._inputDict = {}
        #Configures a dictionary where the key is the input number and the first value is the input value. Second value is the weight
        for i in range(inputs):
            self._inputDict[i]=[1,random.uniform(-1,1)]
        
    def classify(record):
        #Record should be formatted as a list
        for i in range(len(record)-1):
            self._inputDict[i][0] = record[i]
        return self.calculate()
        
    def train(expectedOutput, output, record):
        for i in range(len(record)-1):
            self._inputDict[i][0] = record[i]
        current = self.calculate()
        error = expectedOutput - current
        for i in range(len(self._inputDict)):
            self._inputDict[i][1] = self._inputDict[i][1] + (error * record[i])      
        
    def calculate():
        tanh = 0
        for i in self._inputDict:
            tanh = tanh + (i[0]*i[1])
        tanh = numpy.tanh(tanh)
        return tanh
