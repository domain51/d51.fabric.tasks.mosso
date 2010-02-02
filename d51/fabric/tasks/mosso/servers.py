FABRIC_TASK_MODULE = True
from d51.fabric.tasks.mosso.utils import detail_output, list_output, get_server_api

def list():
    list_output(path='servers', title='Servers')

def detail(id=None):
    detail_output(path='servers', id=id, title='Servers', key='server')

def create(name, imageId, flavorId, metadata={}, personality=[]):
    mosso = get_server_api()
    response = mosso.servers.POST(
        name=name,
        imageId=int(imageId),
        flavorId=int(flavorId),
        metadata=metadata,
        personality=personality
    )

    result = {"servers": [response['server'], ]}
    detail_output(result=result, title="New Server", key='server')

def delete(id):
    mosso = get_server_api()
    print getattr(mosso.servers, id).DELETE()
