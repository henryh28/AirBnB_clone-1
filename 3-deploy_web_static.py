#!/usr/bin/python3
"""
Creates & distributes an archive to my web servers using "deploy" function
"""

from fabric.api import *
from datetime import datetime
import os.path

env.hosts = ['34.229.124.172', '34.234.82.4']
env.user = "ubuntu"


def do_pack():
    current = datetime.now().strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".format(
            current))
        return ("versions/web_static_{}.tgz".format(current))
    except:
        return None


def do_deploy(archive_path):
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        archive_dir = archive_path.split("/")[-1]
        base_dir = "/data/web_static/releases/"
        target_dir = base_dir + archive_dir.split(".")[0]

        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}/".format(target_dir))
        run("sudo tar -xzf /tmp/{} -C {}/".format(archive_dir, target_dir))
        run("sudo rm /tmp/{}".format(archive_dir))
        run("sudo mv {}/web_static/* {}/".format(target_dir, target_dir))
        run("sudo rm -rf {}/web_static".format(target_dir))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(target_dir))
        return True
    except:
        return False


def deploy():
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False
