import schedule
import yaml
import time
import os
import sys
import subprocess

timeout=5
data=dict()

def EXIT():
    print('Exit')
    os.system('sudo rm -R videos')
    sys.exit()

def analyse():
    global data
    d=reader()
    if are_dicts_unique(data,d):
        data=d
        print("Изменение данных")
        restart_program()
    return
    
def reader():
    with open('test.yml','r') as f:
        data = yaml.safe_load(f)
        return data
        
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def format_data(data):
    global timeout
    count_img=0
    count_v=0
    res=[]
    res_v=[]
    d=dict()
    for i in data['media_files']:
        if i['type']=='image':
            res.append(i["path"])
            count_img+=1
        if i['type']=='video':
            res_v.append(i["path"])
            count_v+=1
    d['image']=res
    d['video']=res_v
    timeout=count_img*10
    d['img_size']=count_img
    d['video_size']=count_v
    return d

def are_dicts_unique(dict1, dict2):
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())
    if keys1 != keys2:
        return True
    for key in dict1:
        if dict1[key] != dict2.get(key):
            return True  # если хотя бы одно значение отличается, словари уникальны
    return False

def job1():
    global timeout
    try:
        subprocess.run(['sudo','./gtk1', '3'],timeout=timeout*12)
    except Exception as ex:
        subprocess.run(['sudo','./gtk3', '3'])

with open('test.yml','r') as f:
    data = yaml.safe_load(f)

print(data)
start=data['screensaver_settings']['start_time']
end=data['screensaver_settings']['end_time']
fd=format_data(data)
print(fd)
timeout=fd['img_size']*4
os.system('python3 parser.py')
schedule.every().day.at(start).do(job1) 
schedule.every(45).seconds.do(analyse)
schedule.every().day.at(end).do(EXIT) 

while True:
  schedule.run_pending()
  time.sleep(1)
