from celery import Celery

app = Celery('calculo_matriz', broker='redis://localhost:6379', backend='redis://localhost:6379', include=['calculo_matriz', 'msg'])
