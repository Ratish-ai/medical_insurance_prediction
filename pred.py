import pickle

reg = pickle.load(open('model.pkl','rb'))

def predict(arr):
    global reg
    return int(reg.predict(arr))