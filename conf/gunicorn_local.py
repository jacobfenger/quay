import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import logging

from Crypto import Random
from util.log import logfile_path
from util.workers import get_worker_count


logconfig = logfile_path(debug=True)
bind = '0.0.0.0:5000'
workers = get_worker_count('local', 2, minimum=2, maximum=8)
worker_class = 'gevent'
daemon = False
pythonpath = '.'
preload_app = True

def post_fork(server, worker):
  # Reset the Random library to ensure it won't raise the "PID check failed." error after
  # gunicorn forks.
  Random.atfork()

def when_ready(server):
  logger = logging.getLogger(__name__)
  logger.debug('Starting local gunicorn with %s workers and %s worker class', workers, worker_class)
