#because we spent all the matlab money on beer
import random
import numpy
from numpy import matrix
from numpy import arange
import matplotlib.pyplot as plt

def getSamplesXY(num):
	samples=[]
	for i in range(num):
		samples.append([])

	for i in range(num):
		x = random.uniform(-2,2)
		mean = 0.3*pow(x,3)-0.6*pow(x,2)+.05*x-3 
		variance = 0.25
		y = random.gauss(mean,variance)
		samples[i].append(x)
		samples[i].append(y)

	return samples

def GenerateX(samples,degree):
	X=[]
	num= len(samples)
	degree+=1
	for i in range(num):
		X.append([])
	for i in range(num):
		for j in range(degree):
			X[i].append(pow(samples[i][0],j))
	return matrix(X)

def GenerateY(samples):
	Y=[]
	num= len(samples)
	for i in range(num):
		Y.append(samples[i][1])
	return matrix(Y).T		
		
def Regression(samples,degree):
	
	X=GenerateX(samples,degree)
	Y=GenerateY(samples)
	
	w = (((X.T*X).I)*(X.T))*Y
	return w

def f(x,w):
	w = numpy.array(w).reshape(-1,).tolist()
	degree = len(w)
	num = len(x)
	y=[]
	
	for i in range(num):
		val = 0.0
		for j in range(degree):
			val+=w[j]*pow(x[i],j)
		y.append(val)
	return y
	
def plotPoints(samples,w1,w2,e1,e2):
	
	samples = matrix(samples).T
	Xpts = numpy.array(samples[0]).reshape(-1,).tolist()
	Ypts = numpy.array(samples[1]).reshape(-1,).tolist()
	
	plt.xlim(-2, 2)
	plt.ylim(-10, 0)
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.title('Regression')
	plt.grid(True)
	plt.scatter(Xpts, Ypts, s=50, marker='.', c='r')
	
	#Approximate
	Xapprox = arange(-2.0,2.0,0.01)
	Yapprox = f(Xapprox,w1)	
	plt.plot(Xapprox, Yapprox, linewidth=1.0, color='b')
	Yapprox = f(Xapprox,w2)
	plt.plot(Xapprox, Yapprox, linewidth=1.0, color='g')
	
	#Print Errors
	plt.text(0.0, -0.6, "3rd degree error:"+str(e1))
	plt.text(0.0, -1.2, "5th degree error:"+str(e2))
	
	plt.show()
	
	return
	
def SquareError(samples,w):
	num = len(samples)
	degree=len(numpy.array(w).reshape(-1,).tolist())-1
	Y=GenerateY(samples)
	X=GenerateX(samples,degree)
	Error=Y-(X*w)
	Error = numpy.array(Error.T*Error).reshape(-1,).tolist()
	
	return Error[0]
		
	
num=int(raw_input("Enter number of samples: "))
degree1= int(raw_input("Enter degree 1: "))
degree2= int(raw_input("Enter degree 2: "))

samples = getSamplesXY(num)
weights1 = Regression(samples,degree1)
weights2 = Regression(samples,degree2)

error1=SquareError(samples,weights1)
error2=SquareError(samples,weights2)

plotPoints(samples, weights1, weights2, error1, error2)