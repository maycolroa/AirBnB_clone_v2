#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py)"""
from fabric.api import run, put, env, local
import os
from datetime import datetime


env.hosts = ["34.139.187.216", "34.204.18.63"]
env.user = "ubuntu"

def do_pack():
    """fuction"""
    try:
        local("mkdir -p versions")
        d_t = datetime.now().strftime("%Y%m%d%H%M%S")
        compr_file = "versions/web_static_{}.tgz".format(d_t)
        local("tar -cvzf {} web_static".format(compr_file))
        return compr_file
    except:
        return None


def do_deploy(archive_path):
    """funtion"""
    name_dir = archive_path[9:-4]
    if os.path.exists(archive_path):
        put(archive_path, '/tmp/')
        run("sudo mkdir -p /data/web_static/releases/{}/".format(name_dir))
        run("sudo tar -xzf /tmp/{}.tgz -C \
        /data/web_static/releases/{}/".format(name_dir, name_dir))
        run("sudo rm /tmp/{}.tgz".format(name_dir))
        run("sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".
            format(name_dir, name_dir))
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(name_dir))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ \
            /data/web_static/current".format(name_dir))
        print("New version deployed!")
        return True
    else:
        return False
