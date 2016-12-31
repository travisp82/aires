print("Hello world!")
print("Hello Travis. You're doing well!")

x=11
print(x)
print(x+5)

y=x+9
print(y)
z="success"
print(z)

#list command not printing
list(range(12))

for n in range(10):
    print(n)
    print("The square of", n, "is", n*n)
    pass
print("done")

#the following prints out the cube of 2
print(2**3)


#functions

def avg(x,y):
    print("first input is", x)
    print("second input is", y)
    a=(x+y)/2.0
    print("average is",a)
    return a

avg(3,4)


import numpy

a=numpy.zeros([3,2])
print(a)

a[0,0]=1
a[0,1]=2
a[1,0]=9
a[2,1]=16
print(a)

print(a[0,1])
v=a[1,0]
print(v)

#graphs?

import matplotlib.pyplot
%matplotlib

matplotlib.pyplot.imshow(a, interpolation="nearest")
#need help with this graph


# class for a dog object
class Dog:

    #initilize method with internal data
    def __init__(self, petname, temp, age):
        self.name = petname;
        self.temperature = temp;
        self.age = age;

    #get status
    def status(self):
        print("Dog name is ", self.name)
        print("Dog temperature is ", self.temperature, "degrees Celcius")
        print("Dog age is", self.age, "years old")
        pass

    #set temperature
    def setTemperature(self, temp):
        self.temperature = temp;
        pass

    #set age
    def setAge(self, age):
        self.age = age;
        pass

    #dogs can bark()
    def bark(self):
        print("Woof!")
        pass

    #dog has a name
    def paw(self):
        print(self.name, " says 'Nice to meet you!'")
        print(self.name, " is ", self.age ," years old.")
        print(self.name, "'s temperature is ", self.temperature)

    pass


hulky = Dog("Hulky", 37, 5)
hulky.status()

hulky.setTemperature(13)
hulky.status()

hulky.setAge(3)
hulky.setTemperature(15)
hulky.status()

hulky.paw()



#neural network class definition
class neuralNetwork:

    #initilize
    def  __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        #set number of nodes
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        #learning rate
        self.lr = learningrate
        pass

    #train the neural neuralNetwork
    def train():
        pass

    #qry the neuralNetwork
    def query():
        pass

#number of input, hidden and output nodes
input_nodes = 3
hidden_nodes = 3
output_nodes =3

#learning rate
learning_rate = 0.3

#create instance of neural network
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

#random numbers with numpy
#link weight matrices, wih and who
#weights inside the arrays are w_i_j, where link is node i to node j in the next layer
#w11 w21
#w12 w22 etc
import numpy
self.wih = (numpy.random.rand(self.hnodes, self.inodes) - 0.5)
self.who = (numpy.random.rand(self.onodes, self.hnodes) - 0.5)


self.wif = numpy.random.normal(0.0, pow(self.hnodes, -0.5),(self.hnodes, self.inodes))
self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

hidden_inputs = numpy.dot(self.wif, inputs)

#scipy.special for the sigmoid function expit()
import scipy.special

#activation function is the sigmoid function
self.activation_function = lambda x: scipy.special.expit(x)


#calculate the signals emerging from hidden layer
hidden_outputs = self.activiation_function(hidden_inputs)

#calculate signals into hidden layer
hidden_inputs = numpy.dot(self.wih, inputs)

#calculate the signals emerging from hidden layer
hidden_outputs = self.activiation_function(hidden_inputs)

#calculate signals into final output layer
final_inputs = numpy.dot(self.who, hidden_outputs)
#calculate the signals emerging from final out layer
final_outputs = self.activation_function(final_inputs)
