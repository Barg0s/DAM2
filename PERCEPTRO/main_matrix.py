from perceptron import initialize_weights, train, test_accuracy


def generate_all_matrices():
    matrices = []
    
    for i in range(512):
        binary = format(i, '09b')
        matrix = [int(bit) for bit in binary]
        matrices.append(matrix)
    
    return matrices



def perceptronDiagonal(matriu):
    if (matriu[0] == matriu  [4] == matriu[8] == 1) or( matriu[2] == matriu[4] == matriu[6] == 1):
        return 1
    return 0
    
def perceptroHorizontal(matriu):
    for i in(0,9,3):
        if matriu[i] == matriu[i + 1] == matriu[i + 2] == 1:
            return 1
    return 0


def perceptroVertical(matriu):
    for i in(0,3):
        if matriu[i] == matriu[i + 3] == matriu[i + 6] == 1:
            return 1
    return 0


EPOCHS = 500 
LEARNING_RATE = 0.1
INPUT_SIZE = 9

inputs = generate_all_matrices()

labels = []
for matriu in inputs:
    labels.append(perceptronDiagonal(matriu))
weights = initialize_weights(INPUT_SIZE)
bias = 0.0

weights, bias = train(weights, bias, inputs, labels, LEARNING_RATE, EPOCHS)
accuracy = test_accuracy(weights, bias, inputs, labels)
print(f"\nPercentatge d'encert del Perceptró (Diagonal) entrenat amb {EPOCHS} EPOCHS: {accuracy}%\n")


'''labels = []
for matriu in inputs:
    labels.append(perceptroVertical(matriu))
weights = initialize_weights(INPUT_SIZE)
bias = 0.0

weights, bias = train(weights, bias, inputs, labels, LEARNING_RATE, EPOCHS)
accuracy = test_accuracy(weights, bias, inputs, labels)
print(f"\nPercentatge d'encert del Perceptró (Vertical) entrenat amb {EPOCHS} EPOCHS: {accuracy}%\n")
'''

'''labels = []
for matriu in inputs:
    labels.append(perceptroHorizontal(matriu))
weights = initialize_weights(INPUT_SIZE)
bias = 0.0


weights, bias = train(weights, bias, inputs, labels, LEARNING_RATE, EPOCHS)
accuracy = test_accuracy(weights, bias, inputs, labels)
print(f"\nPercentatge d'encert del Perceptró (Horizontal) entrenat amb {EPOCHS} EPOCHS: {accuracy}%\n")
'''