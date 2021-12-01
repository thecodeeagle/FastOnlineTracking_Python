
def maxd(detections=None,*args,**kwargs):

    ## return the maximum of detections per frame
    N_frame=length(detections)
    pnum=0
    for i in arange(1,N_frame).reshape(-1):
        l=detections[i]
        pnum=max(pnum,size(l,1))

    return pnum

if __name__ == '__main__':
    maxd() #Test using random variables
