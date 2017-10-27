import numpy as np
import random
import scipy.stats as ss
import matplotlib.pyplot as plt

def distance(p1,p2):
    """
    This calculates the distance between two points.
    :param p1: x,y coordinate of first point as numpy array.
    :param p2: x,y coordinate of second point as numpy array.
    :return: distance between p1 and p2
    """
    return np.sqrt(np.sum(np.power(p2 - p1, 2)))

p1 = np.array([1,1])
p2 = np.array([4,4])

print(distance(p1,p2))


#Majority vote

def majority_vote(votes):
    vote_counts = {}
    for vote in votes:
        if vote in vote_counts:
            vote_counts[vote] += 1
        else:
            vote_counts[vote] = 1
    winners = []
    max_counts = max(vote_counts.values())
    for vote, count in vote_counts.items():
        if count == max_counts:
            winners.append(vote)
    return random.choice(winners)

def majority_votess(votes):
    """

    :param votes:
    :return: The most common element in an array
    """
    mode, count = ss.mstats.mode(votes)
    return mode

votes = [1,2,3,1,3,4,1,2,3,1,2,3,3,3,3,2,2,4]

vote_counts = majority_votess(votes)



print(vote_counts)






def find_nearest_neighbors(p, points, k=5):
    """
    Find the k nearest neighbors of point p
    :param p:
    :param points:
    :param k:
    :return:
    """
    distances = np.zeros(points.shape[0])
    for i in range(len(distances)):
        distances[i] = distance(p, points[i])
    ind = np.argsort(distances)
    return ind[:k]


def knn_predict(p, points, outcomes, k=5):
    """
    Find k nearest neighbors.
    Predict the class of p based on majority vote
    :param p:
    :param points:
    :param k:
    :return:
    """
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[ind])


points = np.array([[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]])
p = np.array([2.5,2])
outcomes = np.array([0,0,0,0,1,1,1,1,1])



plt.plot(points[:,0], points[:,1], "ro")
plt.plot(p[0], p[1], "bo")

plt.axis([0.5, 3.5, 0.5, 3.5])

plt.show(block=True)
ind = find_nearest_neighbors(p, points, 4)
print(knn_predict(p, points,outcomes, k=2))
