import os


def clean_output(func, bypass_hit_enter: bool = False):
    os.system("clear")

    def decorator(*args):
        func(*args)
        if bypass_hit_enter:
            input("Press Enter to continue...")
            os.system("clear")
        return

    return decorator
