#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py)"""
from fabric.api import run, put, env
from datetime import datetime
import os

env.hosts = ["34.139.187.216", "34.204.18.63"]


def do_deploy(archive_path):

    if not os.path.exists(archive_path):
        return False

    path = "/data/web_static/releases/"
    name = archive_path.split('.')[0].split('/')[1]
    dest = path + name

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(dest))

        run('tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))
        run('rm -f /tmp/{}.tgz'.format(name))
        run('mv {}/web_static/* {}/'.format(dest, dest))
        run('rm -rf {}/web_static'.format(dest))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(dest))

        return True

    except:
        return False
