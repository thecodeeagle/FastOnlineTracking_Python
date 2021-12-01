import numpy as np


def scores_resize_myversion(objects=None,*args,**kwargs):

    ## change score to the same format as object
    global scores
    for i in range(scores.shape[2]):
        max= objects[i].shape[0]+1
        scores[0][max:scores.shape[1]][i] = 0


    return

if __name__ == '__main__':
    scores_resize_myversion()  #Add temporary variables to test
