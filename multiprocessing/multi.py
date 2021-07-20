import dearpygui.core as core
import time
import multiprocessing


def t1():
    core.set_vsync(True)
    core.add_window("##base", no_background=True)
    core.start_dearpygui(primary_window="##base")

def t2():
    core.set_vsync(True)
    core.add_window("##base")
    core.start_dearpygui(primary_window="##base")

if __name__ == "__main__":
    multiprocessing.Process(target=t1).start()
    # multiprocessing.Process(target=t2).start()
    t2()