
def saveas_txt(outDir=None,sequence_name=None,trackRes=None,*args,**kwargs):
    # transfer the result to adapt the devkit in MOT2015 https://motchallenge.net

    N,D= trackRes[0:2]
    T_res=- ones(N,10)
    T_res[arange(),arange(1,6)]=trackRes(arange(),arange(1,6))
    T_res=sortrows(T_res)
    dlmwrite(concat([outDir,sequence_name,'.txt']),T_res,',')
    return

if __name__ == '__main__':
    saveas_txt()
