from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.code import CheckiORefereeCode

from tests import TESTS

api.add_listener(
    ON_CONNECT,
    CheckiORefereeCode(
        tests=TESTS,
        #check_result=None,
        # add_allowed_modules=[],
        # add_close_builtins=[],
        # remove_allowed_modules=[]
    ).on_ready)
