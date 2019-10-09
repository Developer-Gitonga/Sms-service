from . SMS import SMSService as sms

import celery

app = celery.Celery('tasks')

import os
import africastalkingwrapper



app.conf.update(BROKER_URL=os.environ['REDIS_URL'],
                CELERY_RESULT_BACKEND=os.environ['REDIS_URL'])
