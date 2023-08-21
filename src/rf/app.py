import flask
import structlog

from src import settings

log = structlog.get_logger(__name__)


class RFApp(flask.Flask):
    def __init__(self, *args, **kwargs):
        assert (
            "static_folder" in kwargs.keys()
        ), "static_folder must be set for RF to work"
        assert (
            "template_folder" in kwargs.keys()
        ), "template_folder must be set for RF to work"
        super().__init__(*args, **kwargs)

    def run(self, *args, **kwargs):
        if settings.in_dev_environment:
            log.info(f"URLs: {self.url_map}")

        return super().run(*args, **kwargs)
