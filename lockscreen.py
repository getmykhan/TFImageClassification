import filelock

lock = filelock.FileLock("yala.txt")

lock.timeout = 20

with lock: # 20s timeout
    pass

with lock.acquire(): # 20s timeout
    pass

with lock.acquire(timeout = 10): # 10s timeout
    pass

# If you can not use the *with* statement, use a try-finally construct
# instead:
lock.acquire()
try:
    pass
finally:
    lock.release()

# If you want to use a timeout value, you should consider to catch
# a Timeout exception:
try:
    with lock.acquire(timeout = 10):
        pass
except filelock.Timeout:
    pass

# If you can not use the with statement, you can again use a try-final
# construct instead.
try:
    lock.acquire()
except filelock.Timeout:
    pass
else:
    try:
        pass
    finally:
        lock.release()

# Please note, that you can acquire the lock multiple times without
# blocking. The lock will count, how often it has been acquired and releases
# the lock, as soon as the counter is 0.
with lock:
    assert lock.is_locked
    with lock:
        assert lock.is_locked
    assert lock.is_locked
assert (not lock.is_locked)