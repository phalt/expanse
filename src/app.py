from os.path import abspath, dirname, join

from src.rf.app import RFApp

app = RFApp(
    __name__,
    static_folder=abspath(join(dirname(__file__), "static")),
    template_folder=abspath(join(dirname(__file__), "template")),
)

from src import views  # noqa
