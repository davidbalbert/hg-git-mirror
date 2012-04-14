import os
import sys
import urlparse

from redis import Redis
from rq import Worker, Queue, Connection

import logbook
from logbook import handlers

from constants import *

def format_colors(record, handler):
    from rq.utils import make_colorizer
    if record.level == logbook.WARNING:
        colorize = make_colorizer('darkyellow')
    elif record.level >= logbook.ERROR:
        colorize = make_colorizer('darkred')
    else:
        colorize = lambda x: x
    return '%s: %s' % (record.time.strftime('%H:%M:%S'), colorize(record.msg))

def setup_loghandlers():
    loglevel = logbook.INFO
    formatter = format_colors

    handlers.NullHandler(bubble=False).push_application()
    handler = handlers.StreamHandler(sys.stdout, level=loglevel, bubble=False)
    if formatter:
        handler.formatter = formatter
    handler.push_application()
    handler = handlers.StderrHandler(level=logbook.WARNING, bubble=False)
    if formatter:
        handler.formatter = formatter
    handler.push_application()

def main():
    listen = ['high', 'default', 'low']

    setup_loghandlers()

    conn = Redis(host=REDIS_URL.hostname, port=REDIS_URL.port, db=0, password=REDIS_URL.password)

    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()

if __name__ == '__main__':
    main()
