import pickle

cars = ["Audi", "BMW", "Lamborgini"]
file = "mycar.pkl"
fileobj = open(file, 'rb')
pickle.dump(cars, fileobj)
fileobj.close()

