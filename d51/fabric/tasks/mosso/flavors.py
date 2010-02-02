FABRIC_TASK_MODULE = True

from d51.fabric.tasks.mosso.utils import detail_output, list_output
from dolt.apis.mosso import MossoServers
from fabric.api import env

def list():
    list_output(path='flavors', title='Flavors')

def detail(id=None):
    detail_output(path='flavors', id=id, title="Flavors", key='flavor')
