import hashlib
import socket

__HOSTNAME = socket.gethostname()


def hash(*args, **kwargs):
  hash = hashlib.sha256()
  # hostname as salt
  hash.update((str(args) + str(kwargs) + __HOSTNAME).encode())
  return hash.hexdigest()[:10]