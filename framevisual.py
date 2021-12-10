import numpy as np
import math
import os

def framevisual(objects=None,framenum=None,im_directory=None,images=None,*args,**kwargs):

    global scores
    for frame in range(min(framenum,len(objects))):
        info=objects[frame]
        m = info.shape[0]
        n = info.shape[1]
        now_im=imread(os.path.join(im_directory,images[frame][0].name))
        now_pos = np.zeros((m,2))
        now_sz = np.zeros((m,2))
        for i in range(m):
            now_pos[i] = floor(np.array([info[i][0],info[i][1]))
            now_sz[i] =  floor(np.array([info[i][2],info[i][3]))
        imshow(now_im)
        hold('on')
        for i in range(m):
            if scores[0][i][frame] != 0:
                rect_position= np.array([now_pos[i] - now_sz[i] / 2,now_sz[i]])
                rectangle('Position',rect_position,'EdgeColor','r','LineWidth',1.5)
                fx = now_pos[i][0]
                fy = now_pos[i][1] - now_sz[i][1] / 2 - 10
                text_handle=text(fx,fy,int2str(scores[0][i][frame]))
                set(text_handle,'color',np.array([1,0,0]))
        drawnow


if __name__ == "__main__":
    framevisual()
