FABRIC_TASK_MODULE = True
from d51.fabric.tasks.mosso.utils import detail_output, list_output

def list():
    list_output(path='servers', title='Servers')

def detail(id=None):
    detail_output(path='servers', id=id, title='Servers', key='server')

