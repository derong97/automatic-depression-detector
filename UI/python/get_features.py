import numpy as np

X = np.load("python/X_audio_librosa.npy")
""" print(X.shape) """

y = np.load("python/Y_test_audio.npy")
""" print(y.shape)
print(X[0])
print(y[0]) """
def get(id):
    return X[id], y[id]