from datetime import datetime
import time
from playsound import playsound
def set_alarm(alarm_time,current_time):
    while alarm_time!=current_time:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)
    else:
        print('alarm ringing.....')
        playsound('alarm.wav')

alarm_time=input('enter time you wan to set your alarm(24 hr format):')
current_time=datetime.now().strftime("%H:%M:%S")

set_alarm(alarm_time,current_time)
