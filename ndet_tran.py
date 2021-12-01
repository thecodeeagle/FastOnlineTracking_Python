
def ndet_tran(detections=None,num=None,*args,**kwargs):
    ## divide the detection matrix into cells according to the frame number
    global params
    for flag in arange(1,num).reshape(-1):
        det[flag]=detections(detections(arange(),1) == flag,arange())
        det[flag][arange(),arange(1,2)]=[]
        # line below
        det[flag][arange(),arange(3,4)]=det[flag](arange(),arange(1,2)) + det[flag](arange(),arange(3,4))
        det[flag][arange(),arange(1,4)]=floor(det[flag](arange(),arange(1,4)))
        det[flag][arange(),arange(6,end())]=[]

    detections=copy(det)
    return detections

if __name__ == '__main__':
    pass
