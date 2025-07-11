# Периодические задачи
import datetime
import schedule

i = 1

def job():
    global  i
    print(f'Skript zapustilsyz {i} - raz')
    i += 1
    t = datetime.datetime.now()
    print('Vremya', t.strftime('%H:%M:%S'))

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()