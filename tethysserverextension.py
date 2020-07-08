from subprocess import Popen


def load_jupyter_server_extension(nbapp):
    """start the tethys server"""
    Popen(["tethys", "manage", "start"])
