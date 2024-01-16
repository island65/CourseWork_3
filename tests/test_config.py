import os

ROOT_DIR = os.path.dirname(__file__)


def test_config():
    assert ROOT_DIR == os.path.dirname(__file__)