import easy_tasks as et
from time import sleep

print(et.__version__)


for i in range(10):
    et.progress_printer(i + 1, 10)
    sleep(0.5)
