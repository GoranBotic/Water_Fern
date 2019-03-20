from math import sqrt

def magnitude(X):
        for x in X:
                if x == None:
                        return None
        return sqrt(sum([x**2 for x in X]))

def dot(X, Y):
    if len(X) == len(Y):
        return sum([X[i]*Y[i] for i in range(len(X))])

def cosineSimilarity(X, Y):
    return dot(X,Y)/(magnitude(X)*magnitude(Y))
