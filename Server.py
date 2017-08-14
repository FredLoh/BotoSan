import sys
import os
import logging
from Logging import BotoSanLogger
from BotoSanStack import BotoSanStack

CREDS = (os.environ["BOTO_NUMBER"], os.environ["BOTO_PASSWORD"])  # replace with your phone and password


class Server(object):
    def __init__(self, credentials):
        self.credentials = credentials
        BotoSanLogger.format_logger()
        self.logger = logging.getLogger("botosan.logger")

    def start_server(self):
        """Starts the connection with Whatsapp servers"""
        try:
            self.logger.info("#" * 50)
            self.logger.info("\tServer started. Phone number: %s" % self.credentials[0])
            self.logger.info("#" * 50)
            stack = BotoSanStack(self.credentials)
            stack.start()
        except KeyboardInterrupt:
            self.logger.info("\nYowsdown")
            sys.exit(0)


if __name__ == "__main__":

    server = Server(CREDS)
    while True:
        # In case of disconnect, keeps connecting...
        server.start_server()
        print ("Restarting..")
