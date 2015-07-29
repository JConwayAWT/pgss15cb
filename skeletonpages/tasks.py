import celery, os

app = celery.Celery("skeletonpages")

app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])

@app.task
def add(x, y):
  from time import sleep
  print "sleeping!"
  sleep(5)
  print "done sleeping"
  return x + y