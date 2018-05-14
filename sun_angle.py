from datetime import datetime
from datetime import timedelta

def sun_angle(time):
    #replace this for solution
    now=datetime.strptime(time,"%H:%M")
    now_dt=timedelta( minutes=now.minute+now.hour*60 - 6*60)

    if now_dt < timedelta( minutes=0) or now_dt > timedelta(minutes=60*12):
        return "i cannot see sun"

    div_dt=timedelta(minutes=(int(12*60/180)))

    return now_dt/div_dt



r=sun_angle("07:00")

print(r)