
def ndet_tran(detections=None,num=None,*args,**kwargs):
    ## divide the detection matrix into cells according to the frame number
    global params
    for flag in range(num):
        det[flag]=detections[detections[:][0] == flag][:]
        det[flag][:][0:2]=[]
        # line below
        det[flag][:][2:4] = det[flag][:][0:2] + det[flag][:][2:4]
        det[flag][:][0:4] = floor(det[flag][:][0:4])
        det[flag][:][5:]=[]

    detections = det
    return detections

if __name__ == '__main__':
    ndet_tran() #Test using random variables
