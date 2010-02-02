import pkg_resources
pkg_resources.declare_namespace(__name__)

FABRIC_TASK_MODULE = True

from fabric.api import env

def user(user):
    env.mosso_user = user

def key(key):
    env.mosso_key = key

from d51.fabric.tasks.mosso import flavors, images, servers

