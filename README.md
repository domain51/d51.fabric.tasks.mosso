d51.fabric.tasks.mosso
=========================
Fabric tasks for handling basic management tasks on Mosso/Rackspace Cloud Servers


Requirements
------------
This has been built to be used with the 1.0a version of the [Fabric fork][]
maintained by [Travis Swicegood][].  It might be usable with other versions of
Fabric, but your mileage may vary.


Installation
------------
Create a clone of the repository:

    git clone git://github.com/domain51/d51.fabric.tasks.mosso.git

Then, inside that directory you can install it using either the `setup.py` file
directly, or via Fabric:

    prompt> python setup.py install
    ... or ...
    prompt> fab install

Usage
-----
You can import the individual tasks into your current fabfile:

    from d51.fabric.tasks.mosso import *

Or, you can import the module and execute the tasks that way:

    from d51.fabric.tasks import mosso

### Providing Credentials
You must provide the tasks with a way to authenticate with Mosso.  To do this,
you need your username and your API key.  You can provide these via the
`mosso.user` and `mosso.key` tasks at runtime:

    prompt> fab mosso.user:some_user mosso.key:some_generated_api_key ... rest of tasks ...

Or, you can specify them as `env` variables inside your fabfile.

    from fabric.api import env
    env.mosso_user = "some_user"
    env.mosso_key = "some_generated_api_key"


Tasks
-----
* `mosso.flavors.detail`
* `mosso.flavors.detail_output`
* `mosso.flavors.list`
* `mosso.flavors.list_output`
* `mosso.images.detail`
* `mosso.images.detail_output`
* `mosso.images.get_server_api`
* `mosso.images.list`
* `mosso.images.list_output`
* `mosso.ips.get_server_api`
* `mosso.ips.list`
* `mosso.ips.share`
* `mosso.ips.unshare`
* `mosso.key`
* `mosso.servers.create`
* `mosso.servers.delete`
* `mosso.servers.detail`
* `mosso.servers.detail_output`
* `mosso.servers.get_server_api`
* `mosso.servers.list`
* `mosso.servers.list_output`
* `mosso.servers.update`
* `mosso.user`

[Fabric fork]: http://github.com/tswicegood/fabric
[Travis Swicegood]: http://www.travisswicegood/
