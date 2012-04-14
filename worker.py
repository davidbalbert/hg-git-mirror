import os
import urlparse

from redis import Redis
from rq import Worker, Queue, Connection

from constants import *

listen = ['high', 'default', 'low']

conn = Redis(host=REDIS_URL.hostname, port=REDIS_URL.port, db=0, password=REDIS_URL.password)

with Connection(conn):
    worker = Worker(map(Queue, listen))
    worker.work()
