from apscheduler.schedulers.background import BackgroundScheduler
from api.management.commands import pull_ethereum, pull_neo_mainnet

def start_pull_neo_job():
    scheduler = BackgroundScheduler()
    scheduler.add_job(pull_neo_mainnet.fetch_neo(), "interval", minutes=5, id="neo", replace_existing=True)
    scheduler.start()

def start_pull_ethereum_job():
    scheduler = BackgroundScheduler()
    scheduler.add_job(pull_ethereum.fetch_ethereum(), "interval", minutes=5, id="ethereum", replace_existing=True)
    scheduler.start()