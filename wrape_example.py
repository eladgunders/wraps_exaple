from functools import wraps

flag = False


def check_flag(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not flag:
            print('Not executing the function')
            return
        else:
            return f(*args, **kwargs)
    return decorated


@check_flag
def print_name(name):
    print(name)


print_name('itay')
