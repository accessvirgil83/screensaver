import shutil
import yaml
import os

def rs():
    with open('test.yml','r') as f:
        templates = yaml.safe_load(f)
    return templates

def parse(data):
    count_img=0
    count_audio=0
    res=[]
    for i in data['media_files']:
        if i['type']=='image':
            shutil.copyfile(i['path'],f'img/{count_img}.jpg')
            res.append(i['path'])
            count_img+=1
        if i['type']=='video':
            if not os.path.exists('videos/{count_audio}/video'):
                os.makedirs(f'videos/{count_audio}/video')
            shutil.copyfile(i['path'],f'videos/{count_audio}.mp4')
            os.system(f'sudo ffmpeg -i videos/{count_audio}.mp4 videos/{count_audio}/video/%d.jpg')
            shutil.copyfile('gtk3',f'videos/{count_audio}/gtk3')
            os.chmod(f'videos/{count_audio}/gtk3',755)
            count_audio+=1
    return 


data=rs()
parse(data)
