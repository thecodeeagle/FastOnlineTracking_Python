import numpy as np
import os

def choose_video(base_path=None,*args,**kwargs):
    base_path.replace("\","/")
    if base_path(end()) != '/':
        base_path[end() + 1]='/'

    contents= dir(base_path)
    names= np.array([])
    for k in range(len(contents)):
        name=contents(k).name

        if isfolder(concat([base_path,name])) and logical_not(strcmp(name,'.')) and logical_not(strcmp(name,'..')):
            names[end() + 1]=name

    if isempty(names):
        video_name=[]

        return video_name

    #choice GUI
    choice=listdlg('ListString',names,'Name','Choose video','SelectionMode','single')
    if isempty(choice):
        video_name=[]

    else:
        video_name=names[choice]



    return video_name

if __name__ == '__main__':
    choose_video()
