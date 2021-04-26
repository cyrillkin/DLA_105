import logging
import log_config

def log(func_for_log):
    def func(*args):
        return func_for_log(*args)
    return func

@log
def func_in(x, y):
    return x * y

attr = func_in(1, 2)

log = logging.getLogger('app')
log.info("%s", attr)