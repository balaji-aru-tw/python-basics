import pickle
import os

def store(data, file_name):
    binary_file = open(file_name, 'wb')
    pickle.dump(data, binary_file)
    binary_file.close()

def load(file_name):
    if os.path.exists(file_name):
        binary_file = open(file_name, "rb")
        result = pickle.load(binary_file)
        binary_file.close()
        return result
    return None


x = [1,2,3,4,5,6,7]
print("original")
print(x)
store(x, "x.pkl")
y = load("x.pkl")
print("\n reloaded")
print(y)

class test:
    counter = 10
    
obj = test()

print("original")
print(dir(obj))
store(obj, "class.pkl")



load_obj = load("class.pkl")
print("\n reloaded")
print(dir(load_obj))