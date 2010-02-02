from dolt.apis.mosso import MossoServers
from fabric.api import env


def list_output(path=None, title=None, key=None):
    result = getattr(get_server_api(), path)()
    print "%s:" % title
    for entry in result[path]:
        print " - %s (%s)" % (entry['name'], entry['id'])


def get_detail_result(path=None, key=None, id=None):
    api = getattr(get_server_api(), path)
    if not id:
        result = api.detail()
    else:
        result = getattr(api, id)()
        result[key+'s'] = [result[key], ]
    return result
 
def detail_output(path=None, title=None, key=None, id=None, result=None):
    def detail_out(iter, indent=2):
        max_len = reduce(lambda a, b: max(a, len(b)), iter.keys(), 0)
        def title(string):
            return "%s%s" % (" " * indent, key.capitalize().rjust(max_len + indent))

        for key, value in iter.items():
            if type(value) is dict:
                print title(key)
                detail_out(value, indent+2)
            else:
                print "%s : %s" % (title(key), value)
    result = result if result else get_detail_result(path=path, key=key, id=id)

    print "%s:" % title
    for detail in result[key+'s']:
        print " - %s (%s)" % (detail['name'], detail['id'])
        del detail['name']
        del detail['id']
        detail_out(detail)

def get_server_api(user=None, key=None):
    user = env.mosso_user if user is None else user
    key = env.mosso_key if key is None else key
    return MossoServers(user, key)
