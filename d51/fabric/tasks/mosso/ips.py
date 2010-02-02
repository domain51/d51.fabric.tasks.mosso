FABRIC_TASK_MODULE = True
from d51.fabric.tasks.mosso.utils import get_server_api

def list(id, public=False, private=False):
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

def share(id, address):
    raise Exception("Not yet implemented")

def unshare(id, address):
    raise Exception("Not yet implemented")
