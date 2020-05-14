from authenticate.tasks import myTask
from apscheduler.schedulers.background import BackgroundScheduler

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(myTask,'interval',days = 1,max_instances = 100)
    scheduler.start()
