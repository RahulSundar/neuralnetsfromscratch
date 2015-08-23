# Get data
from loader import loadmat
from neural_word_prediction import Neural

matrix = loadmat('data.mat')
training_data = matrix['data']['trainData'].transpose()
#training_data = training_data.reshape(training_data.shape+(1,))
test_data = matrix['data']['testData'].transpose()
#test_data = test_data.reshape(test_data.shape+(1,))
vocab = matrix['data']['vocab']

sentences = [[vocab[i-1] for i in data] for data in test_data]

#import pdb; pdb.set_trace()

nn = Neural([50*3, 70, 250], vocab, 3)
output = nn.feedforward(training_data[0][:-1])
output = nn.SGD(training_data, test_data, 3, 25, 100)
#import pdb; pdb.set_trace()
#input = np.ones((784, 1))
#nn.feedforward(input)
#nn.SGD(training_data, test_data, 3, 25, 50)
# wap to predict with random weights and word vectors

# while passing vocab only, matrix with weights should be initialized

# measure accuracy in this case

# should be pretty random but generate prediction for next word using it
# write backpropogation then
# make mistakes, write basic program, then see answer

# modify feedforward for sigmoid