
def info_get(x=None,*args,**kwargs):

    ## change detection format
    m,n=size(x,nargout=2)

    if m == 1:
        object=copy(x)

        for num in arange(1,n).reshape(-1):
            detectionresult=x[1,num]

            m1,n1=size(detectionresult,nargout=2)

            if n1 == 5:
                tempresult=zeros(m1,4)
                tempresult[arange(),1]=floor(dot(1 / 2,(detectionresult(arange(),1) + detectionresult(arange(),3))))
                tempresult[arange(),2]=floor(dot(1 / 2,(detectionresult(arange(),2) + detectionresult(arange(),4))))
                tempresult[arange(),3]=detectionresult(arange(),3) - detectionresult(arange(),1)
                tempresult[arange(),4]=detectionresult(arange(),4) - detectionresult(arange(),2)
            else:
                error('wrong detection format')
            object[num]=tempresult
    else:
        error('wrong detection format')

    return object

if __name__ == '__main__':
    info_get()
