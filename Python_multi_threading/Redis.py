from redis import Redis
from rq import Queue
import time

c = Redis()
q = Queue(connection=Redis())




