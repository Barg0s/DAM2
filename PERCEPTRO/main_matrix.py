from perceptron import initialize_weights, train, test_accuracy


EPOCHS_LIST = [1, 5, 10, 20]

def generate_all_matrices():
    matrices = []
    
    for i in range(512):
        binary = format(i, '09b')
        matrix = [int(bit) for bit in binary]
        matrices.append(matrix)
    
    return matrices

'''0 0 0
   0 0 0
   0 0 0'''

def perceptronDiagonal(matriu):
    if (matriu[0] == matriu  [4] == matriu[8] == 1) or( matriu[2] == matriu[4] == matriu[6] == 1):
        return 1
    return 0
    
def perceptroHorizontal(matriu):
    for i in range(0,9,3):
        if matriu[i] == matriu[i + 1] == matriu[i + 2] == 1:
            return 1
    return 0


def perceptroVertical(matriu):
    for i in range(0,3):
        if matriu[i] == matriu[i + 3] == matriu[i + 6] == 1:
            return 1
    return 0


LEARNING_RATE = 0.1
INPUT_SIZE = 9

inputs = generate_all_matrices()

labels = []
for matriu in inputs:
    x = perceptroHorizontal(matriu)
    y = perceptroVertical(matriu)
    z = perceptronDiagonal(matriu)
    if x == 1:
        labels.append(x)
    elif y == 1:
        labels.append(y)
    elif z == 1:
        labels.append(z)
    else:
        labels.append(0)
weights = initialize_weights(INPUT_SIZE)
bias = 0.0

for epoch in EPOCHS_LIST:
    weights, bias = train(weights, bias, inputs, labels, LEARNING_RATE, epoch)
    accuracy = test_accuracy(weights, bias, inputs, labels)
    print(f"\nPercentatge d'encert dels perceptrons entrenats amb {epoch} EPOCHS: {accuracy}%\n")


