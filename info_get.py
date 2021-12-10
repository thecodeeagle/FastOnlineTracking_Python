
def info_get(x=None,*args,**kwargs):

    ## change detection format
    m = x.shape[0]
    n = x.shape[1]

    if m == 1:
        object= x

        for num in range(n):
            detectionresult=x[0][num]

            m1 = detectionresult[0]
            n1 = detectionresult[1]

            if n1 == 5:
                tempresult = np.zeros((m1,4))
                tempresult[:][0] = floor(dot(1 / 2,(detectionresult[:][0]) + detectionresult(arange(),3))))
                tempresult[:][1] = floor(dot(1 / 2,(detectionresult(arange(),2) + detectionresult(arange(),4))))
                tempresult[:][2] = detectionresult[:][2] - detectionresult[:][0]
                tempresult[:][3] = detectionresult[:][3] - detectionresult[:][1]
            else:
                error('wrong detection format')
            object[num]=tempresult
    else:
        error('wrong detection format')

    return object

if __name__ == '__main__':
    info_get()
