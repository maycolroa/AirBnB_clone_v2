#!/usr/bin/python3
"""Write a Fabric script (based on the file 2-do_deploy_web_static"""

from fabric.api import local, settings, abort, run, cd, env, put, get
from fabric.decorators import task, hosts, with_settings
from os import path
from datetime import datetime


env.hosts = ["34.139.187.216", "34.204.18.63"]
env.user = "ubuntu"
