#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive"""


from fabric.api import local
import datetime
def do_pack():
    local("mkdir -p versions")
    k = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    archive_1 = local("tar -czvf versions/web_static_{}\
.tgz web_static".format(k))
    if archive_1:
        return ("versions/web_static_{}".format(k))
    else:
        return None
