#!/usr/bin/python3
"""
Distributes an archive to my web servers using the function "do_deploy"
"""

from fabric.api import *
import os.path

env.hosts = ['34.229.124.172', '34.234.82.4']
env.user = "ubuntu"


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
