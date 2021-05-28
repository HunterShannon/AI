neuron = Perceptron(16)
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
