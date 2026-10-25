import os
import signal

from granmagotchi.app import Granmagotchi

import subprocess
from threading import Thread

root = Granmagotchi()

def run_llama():
    print(subprocess.run("ollama run gemma4:e4b Give no output."))
    print(subprocess.run("ollama run smollm2:135m Give no output."))

thread = Thread(target = run_llama)
thread.start()

root.mainloop()
os.kill(os.getpid(), signal.SIGINT)