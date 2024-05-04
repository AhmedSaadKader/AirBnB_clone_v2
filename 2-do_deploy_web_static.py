#!/usr/bin/python3
""" Distribute an archive to a web server
"""
import os.path
from fabric.api import env, put, run

env.user = "ubuntu"
env.key_filename = "/home/ahmedsaad/.ssh/id_rsa"
env.hosts = ["35.153.79.28", "100.24.74.193"]


def do_deploy(archive_path):
    """Distributes an archive to a web server

    Args:
        archive_path (str): path to the archive
    Return:
        True if successful False if not
    """
    if os.path.isfile(archive_path) is False:
        return False
    file_path = archive_path.split("/")[-1]
    directory = file_path.split(".")[0]

    if put(archive_path, "/tmp/{}"
           .format(file_path)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/"
           .format(directory)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/"
           .format(directory)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
           .format(file_path, directory)).failed is True:
        return False
    if run("rm /tmp/{}"
           .format(file_path)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/"
           .format(directory, directory)).failed is True:
           return False
    if run("rm -rf /data/web_static/releases/{}/web_static"
           .format(directory)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
           .format(directory)).failed is True:
        return False
    print("New version deployed!")

    return True
