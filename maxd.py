
def maxd(detections=None,*args,**kwargs):

    ## return the maximum of detections per frame
    N_frame = len(detections)
    pnum=0
    for i in range(N_frame):
        l=detections[i]
        pnum=max(pnum,l.shape[0])

    return pnum

if __name__ == '__main__':
    maxd() #Test using random variables
