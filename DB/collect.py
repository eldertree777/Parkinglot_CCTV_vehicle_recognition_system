import schedule
from DB import DB
import time

DataBase = DB()

def job():
    print("자연, 우리의 미래...")

# schedule.every(3).seconds.do(job) # 3초마다 job 실행
# schedule.every(3).minutes.do(job) # 3분마다 job 실행
# schedule.every(3).hours.do(job) # 3시간마다 job 실행
# schedule.every(3).days.do(job)  # 3일마다 job 실행
# schedule.every(3).weeks.do(job) # 3주마다 job 실행

# schedule.every().minute.at(":23").do(job) # 매분 23초에 job 실행
schedule.every().hour.at(":42").do(job) # 매시간 42분에 작업 실행

# # 5시간 20분 30초마다 작업 실행
# schedule.every(5).hours.at("20:30").do(job)

# # 매일 특정 HH:MM 및 다음 HH:MM:SS에 작업 실행
# schedule.every().day.at("10:30").do(job)
# schedule.every().day.at("10:30:42").do(job)

# # 주중 특정일에 작업 실행
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)