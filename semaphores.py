import threading
import time

semaphore = threading.BoundedSemaphore(value=5)


def access(thread_number):
    print("{} is trying to access".format(thread_number))
    semaphore.acquire()
    print("{} was granted access!".format(thread_number))
    time.sleep(10)
    print("{} is now releasing!".format(thread_number))
    semaphore.release()


for thread_numb in range(1, 11):
    t = threading.Thread(target=access, args=(thread_numb,))
    t.start()
    time.sleep(1)
