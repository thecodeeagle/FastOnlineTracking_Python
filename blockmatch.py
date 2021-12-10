import os
import numpy as np
import math


def blockmatch(detections=None,objects=None,framenum=None,im_directory=None,images=None,params=None,pnum=5,*args,**kwargs):

    object_pnum= np.dot(math.ceil((pnum + 6) / 5),5)
    scores= np.zeros((object_pnum,object_pnum,np.size(images)))
    results= np.zeros((1,object_pnum,np.size(images)))
    resulttmp= np.zeros((1,object_pnum,np.size(images)))
    virobjects= np.array([])
    virresults= np.array(framenum)
    virscore= np.array(framenum)
    labels= np.zeros(1,object_pnum,framenum)
    flag=1
    virflag=0
    non_compressed_features= np.array(['gray'])
    compressed_features= np.array(['cn'])
    #temp= load('w2crs.mat')// Convert this
#    w2c=w2crs
    for frame in range(min(framenum,len(objects))):
        ## visualize process
        clear = lambda: os.system('cls')  # On Windows System
        clear()
        fprintf('Processing %.1f%%\n',dot(frame,100) / min(framenum,len(objects)))
        infor=objects[frame]

        m= infor.shape[0]

        if frame == 0:
            pre_m=copy(m)

            for i in range(m):
                scores[i][i][frame]=1
                results[0][i][frame]=i
                labels[0][i][frame]=flag
                flag=flag + 1

        else:
            # save previous information
            pre_im=now_im
            pre_pos=now_pos
            pre_sz=now_sz

        ## add virtual objects
        vm= virobjects.shape[0]
#--> Conversion done
        if vm>=0:
            fr=frame - virobjects[:,4]
            outd= fr[fr > 5]
            virobjects[outd]=[]

        vm= virobjects.shape[0]

        now_im=imread(os.path.join(im_directory,images[frame][0].name))
        now_pos= np.zeros((m,2))
        now_sz= np.zeros((m,2))

        for i in range(m):
            now_pos[i] = floor(np.array([infor[i][0],infor[i][1]]))
            now_sz[i]  = floor(np.array([infor[i][2],infor[i][3]]))
        ## model transformation and matching
        if frame > 0:
            for t1 in range(pre_m):
                for t2 in range(m):
                    scores[t1][t2][frame]=patchmatch(pre_im,pre_pos(t1,arange()),pre_sz(t1,arange()),now_im,now_pos(t2,arange()),now_sz(t2,arange()),non_compressed_features,compressed_features,w2c)

                resulttmp[0][t1][frame]
                tm=max(scores[t1][:][frame])

                if resulttmp[0][t1][frame] > params.eta1:
                    if logical_not(results[0][tm][frame]):
                        results[0][tm][frame]=t1
                        labels[0][tm][frame]=labels[0][t1][frame - 1]

                    else:
                        tn=results[0][tm][frame]
                        tmp=scores[tn][tm][frame]
                        if resulttmp[0][t1][frame] > tmp:
                            results[0][tm][frame]=t1
                            labels[0][tm][frame]=labels[0][t1][frame - 1]

                ## match virtual objects
                virscore[frame]=np.zeros((vm,m))
                vtms= np.zeros((1,vm))
                vtmn=1
                if vm != 0:
                    for t2 in range(m):
                        if logical_not(results[0][t2][frame]):
                            for ii in range(vm):
                                frameno=virobjects[ii][4]
                                vir_im=imread(os.path.join(im_directory,images[frameno][1].name))
                                virscore[frame][ii][t2]=pmatch(vir_im,virobjects(ii,arange()),now_im,now_pos(t2,arange()),now_sz(t2,arange()),non_compressed_features,compressed_features,w2c)
                        vrt,vtm=max(virscore[frame][:][t2])
                        if vrt > params.zeta:
                            if logical_not(find(vtms == vtm)):
                                results[0][t2][frame]=min(max(results[0][:][frame] + 1,object_pnum))
                                labels[0][t2][frame]=virobjects[vtm][6])
                                vtms[vtmn]=vtm
                                vtmn=vtmn + 1
                            else:
                                v11=find(labels[0][:][frame] == virobjects[vtm][7])
                                if virscore[frame][vtm][t2] > virscore[frame][vtm][v11]:
                                    results[0][t2][frame]=min(max(results[0][:][frame] + 1,object_pnum))
                                    labels[0][t2][frame]=virobjects[vtm][6]
                                    results[0][v11][frame]= 0
                                    labels[0][v11][frame]= 0

            ## build virtual objects
            t1n= pre_m
            pre_m= m
#conversion done
            for t1 in range(t1n):
                if max(scores[t1][:][frame]) < params.eta2:
                    if labels[0][t1][frame - 1]:
                        det,obj,ff=missdetection(now_im,pre_im,pre_pos[t1][:],pre_sz[t1][:],non_compressed_features,compressed_features,w2c)

                        if ff:
                            objects[frame] = np.concatenate((objects[frame], obj), axis = 0)
                            detections[frame] = np.concatenate((detections[frame], det), axis=0)
                            infor = np.concatenate((infor, obj), axis = 0)
                            now_pos = np.concatenate((now_pos,np.array([obj(1),obj(2)])), axis=0)
                            now_sz = np.concatenate((now_sz, np.array([obj(3), obj(4)])), axis=0)


                            if m >= object_pnum:
                                fprintf('wrong')
                            else:
                                scores[t1][m + 1][frame]=det[4]
                                results[0][m + 1][frame]=t1
                                labels[0][m + 1][frame]=labels[0][t1][frame - 1]
                                m = m + 1

                        else:
                            if labels[0][t1][frame - 1]:
                                if len(virobjects)==0:
                                    alternative =altersave(now_im,frame,pre_im,pre_pos[t1],pre_sz[t1],t1,labels[0][t1][frame - 1],virflag,non_compressed_features,compressed_features,w2c)
                                    virobjects = alternative
                                    virflag = virflag + 1

                                else:
                                    alternative = altersave(now_im,frame,pre_im,pre_pos[t1],pre_sz[t1],t1,labels[1][t1][frame - 1],virflag,non_compressed_features,compressed_features,w2c)
                                    virobjects = np.concatenate((virobjects,alternative), axis=0)
                                    virflag = virflag + 1

            ## clear overlap region
            m1= objects[frame].shape[0]
            overlap= np.zeros((m1,m1))

            for tt1 in range(m1):
                for tt2 in range(m1):
                    overlap[tt1,tt2]=com_overlap(objects[frame][tt1][0:2],objects[frame][tt2][0:2],objects[frame][tt1][2:4],objects[frame][tt2][2:4])

            for iii in range(m):
                if !results[0][iii][frame]:
                    if max(scores[:][iii][frame]) < params.eta2 and detections[frame][iii][4] > params.sigma:
                        labels[0][iii][frame]=flag
                        flag = flag + 1


    flag = flag - 1

    return detections,objects,labels,flag,scores,resulttmp,results,virscore,virobjects,virresults

if __name__ == '__main__':
    blockmatch()
