FABRIC_TASK_MODULE = True

from d51.fabric.tasks.mosso.utils import detail_output, get_server_api, list_output
from dolt.apis.mosso import MossoServers
from fabric.api import env

def list():
    list_output(path='images', title='Images', key='images')

def detail(id=None):
    detail_output(path='images', id=id, title="Images", key='image')

