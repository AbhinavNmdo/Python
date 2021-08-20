import pickle

# cars = ["Audi", "BMW", "Lamborgini"]
# file = "mycar.pkl"
# fileobj = open(file, 'rb')
# pickle.dump(cars, fileobj)
# fileobj.close()

file = "mycar.pkl"
fileobj = open(file, 'rb')
cars = pickle.loads(fileobj)
print(cars)