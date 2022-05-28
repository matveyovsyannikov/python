time = int(input('Type time in sec: '))
hours = time//3600
minutes = (time-hours*3600)//60
sec = time % 60
print(f"time: {hours}:{minutes}:{sec}")
