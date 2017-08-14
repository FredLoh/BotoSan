from slack_logger import SlackHandler, SlackFormatter
import logging


class BotoSanLogger:
    def __init__(self):
        pass

    @staticmethod
    def format_logger():
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger("botosan.logger")
        logger.setLevel(logging.INFO)

        sh = SlackHandler(username='logger', icon_emoji=':robot_face:',
                          url='https://hooks.slack.com/services/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')
        sh.setLevel(logging.INFO)

        f = SlackFormatter()
        sh.setFormatter(f)
        logger.addHandler(sh)
        return logger
