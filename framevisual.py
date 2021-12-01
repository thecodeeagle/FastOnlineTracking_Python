import numpy as np
import math
import os

def framevisual(objects=None,framenum=None,im_directory=None,images=None,*args,**kwargs):

    global scores
    for frame in range(min(framenum,len(objects))):
        info=objects[frame]
        m,n=size(info,nargout=2)
        now_im=imread(fullfile(im_directory,images(frame,1).name))
        now_pos=zeros(m,2)
        now_sz=zeros(m,2)
        for i in arange(1,m).reshape(-1):
            now_pos[i,arange()]=floor(concat([info(i,1),info(i,2)]))
            now_sz[i,arange()]=floor(concat([info(i,3),info(i,4)]))
        imshow(now_im)
        hold('on')
        for i in arange(1,m).reshape(-1):
            if scores(1,i,frame) != 0:
                rect_position=concat([now_pos(i,arange()) - now_sz(i,arange()) / 2,now_sz(i,arange())])
                rectangle('Position',rect_position,'EdgeColor','r','LineWidth',1.5)
                fx=now_pos(i,1)
                fy=now_pos(i,2) - now_sz(i,2) / 2 - 10
                text_handle=text(fx,fy,int2str(scores(1,i,frame)))
                set(text_handle,'color',concat([1,0,0]))
        drawnow
        hold('off')
