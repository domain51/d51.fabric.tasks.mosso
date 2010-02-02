FABRIC_TASK_MODULE = True
from d51.fabric.tasks.mosso.utils import detail_output, list_output, get_server_api

def list():
    list_output(path='servers', title='Servers')

def detail(id=None):
    detail_output(path='servers', id=id, title='Servers', key='server')

def ips(id, public=False, private=False):
    mosso = getattr(get_server_api().servers, id)

    if public:
        result = mosso.ips.public()
        title = 'Public IPs'
    elif private:
        result = mosso.ips.private()
        title = 'Private IPs'

    if public or private:
        print "%s:" % title
        for address in result[public and 'public' or 'private']:
            print '    %s' % address
    else:
        result = mosso.ips()
        print "IPs:"
        for key, addresses in result['addresses'].items():
            print " - %s" % key.capitalize()
            for address in addresses:
                print "    %s" % address

