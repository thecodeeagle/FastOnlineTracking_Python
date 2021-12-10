
import numpy as np

def saveas_txt(outDir=None,sequence_name=None,trackRes=None,*args,**kwargs):
    # transfer the result to adapt the devkit in MOT2015 https://motchallenge.net
    N = trackRes[0]
    D = trackRes[1]
    T_res= -1* np.ones((N,10))
    T_res[:][0:6] = trackRes[:][0:6]
    T_res= np.argsort(T_res, axis=1)
    np.savetxt(outDir+sequence_name+'.txt',T_res,delimiter=',')
    return

if __name__ == '__main__':
    saveas_txt()
