from slack_logger import SlackHandler, SlackFormatter
import logging
import os


class BotoSanLogger:
    def __init__(self):
        pass

    @staticmethod
    def format_logger():
        hook_url = os.environ["SLACK_HOOK_URL"]
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger("botosan.logger")
        logger.setLevel(logging.INFO)

        sh = SlackHandler(username='logger', icon_emoji=':robot_face:',
                          url=hook_url)
        sh.setLevel(logging.INFO)

        f = SlackFormatter()
        sh.setFormatter(f)
        logger.addHandler(sh)
        return logger
