import schedule
import time
import os
import subprocess
import yaml

templates=dict()
flag=True

def job():
	global templates
	with open('test.yml','r') as f:
		templates = yaml.safe_load(f)
		print(str(templates))
		#schedule.every().day.at(templates['screensaver_settings']['start_time']).do(os.system(f'./a'))
		#subprocess.run(['python','screen.py'])


def job2():
	global templates
	print("HW")
	subprocess.run(['python', 'screen.py'])
	print(str(templates['screensaver_settings']['start_time']))

with open('test.yml','r') as f:
	templates = yaml.safe_load(f)
	print(str(templates))
schedule.every().day.at(templates['screensaver_settings']['start_time']).do(job) 
schedule.every(10).minutes.do(job2)

while True:
    schedule.run_pending()
	#time.sleep(1)
