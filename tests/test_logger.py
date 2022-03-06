from logging import getLogger, DEBUG, INFO, WARNING, ERROR
import time
import threading
from mlib.output_log import func, worker

logger = getLogger(__name__)


def test_func(caplog):
    """
    caplog.record_tuples:[
    ('mlib.output_log', 10, 'This is debug.'),
    ('mlib.output_log', 20, 'This is info.'),
    ('mlib.output_log', 30, 'This is warning.'),
    ('mlib.output_log', 40, 'This is error.')
    ]

    """

    caplog.set_level(DEBUG)

    func()

    assert ('mlib.output_log', DEBUG, 'This is debug.') in caplog.record_tuples
    assert ('mlib.output_log', INFO, 'This is info.') in caplog.record_tuples
    assert ('mlib.output_log', WARNING, 'This is warning.') in caplog.record_tuples
    assert ('mlib.output_log', ERROR, 'This is error.') in caplog.record_tuples


def test_threading(caplog):
    caplog.set_level(DEBUG)
    t = threading.Thread(target=worker, args=())
    t.start()
    t.join()  # workerより先にassertを実行すると失敗する(実際にやると成功したり失敗したりする)

    assert ('mlib.output_log', INFO, 'from worker') in caplog.record_tuples
