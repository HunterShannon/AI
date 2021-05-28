import random
#Algorithm in Perceptron taken from https://en.wikipedia.org/wiki/Perceptron
#Neuron Object
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

#Neuron Training Function
def trainNeuron(neuron, filename, numTrain):
    #Open the document and create an array of all lines in the document
    doc = open(filename, 'r')
    lines = doc.readlines()
    for x in range(numTrain):
        #Iterate through every line
        for i in range(len(lines)):
            #If line is a comment, pass
            if lines[i][0:2] == '//':
                pass
            else:
                #Create record for training
                record = []
                #Loop through the file line length -1 as we do not want to factor in the party affiliation yet
                for j in range(len(lines[i])-1):
                    #Only select the proper pairs - if j is not modulusable by 2, it is an odd position and would give an improper pair
                    if j%2 != 0:
                        pass
                    else:
                        #01 is a -1, 10 is a +1. Anything else we add to the record as a 0.
                        if lines[i][j:j+2] == '01':
                            record.append(-1)
                        elif lines[i][j:j+2] == '10':
                            record.append(1)
                        else:
                            record.append(0)
                neuron.train(lines[i][32],lines[i][32], record)

#Train and check accuracy
republican = Perceptron(16)
democrat = Perceptron(16)
general = Perceptron(16)
trainNeuron(republican, 'vote-rep.txt', 90)
trainNeuron(democrat, 'vote-dem.txt', 99)
trainNeuron(general, 'vote-gen.txt', 189)
doc = open('vote-gen.txt', 'r')
lines = doc.readlines()
num = 0
repubAverage = 0
demoAverage = 0
genAverage = 0
for i in range(len(lines)):
    if lines[i][0:2] == '//':
        pass
    else:
        #Create record for classifying
        record = []
        #Loop through the file line length -1 as we do not want to factor in the party affiliation yet
        for j in range(len(lines[i])-1):
            #Only select the proper pairs - if j is not modulusable by 2, it is an odd position and would give an improper pair
            if j%2 != 0:
                pass
            else:
                #01 is a -1, 10 is a +1. Anything else we add to the record as a 0.
                if lines[i][j:j+2] == '01':
                    record.append(-1)
                elif lines[i][j:j+2] == '10':
                    record.append(1)
                else:
                    record.append(0)
        num = num + 1
        repubAverage = repubAverage + republican.classify(record)
        demoAverage = demoAverage + democrat.classify(record)
        genAverage = genAverage + general.classify(record)
repubError = abs(99-repubAverage)/99
demoError = abs(99-demoAverage)/99
genError = abs(99-genAverage)/99

print("Republican Neuron Average: " + str(repubAverage))
print("Democrat Neuron Average: " + str(demoAverage))
print("General Neuron Average: " + str(genAverage))
print("Actual Average: " + str(99))
print("==============")
print("Accuracy:")
print("Republican Neuron: "+ str(100*(1-repubError)))
print("Democrat Neuron: " + str(100*(1-demoError)))
print("General Neuron: " + str(100*(1-genError)))
