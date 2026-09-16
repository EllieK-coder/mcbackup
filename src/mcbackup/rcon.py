import logging
from contextlib import contextmanager

from mcrcon import MCRcon

log = logging.getLogger(__name__)


@contextmanager
def paused_saving(host: str, password: str, port: int = 25575):
    with MCRcon(host, password, port=port) as client:
        log.info("Pausing world saves")
        client.command("save-off")
        client.command("save-all flush")
        try:
            yield
        finally:
            log.info("Resuming world saves")
            client.command("save-on")