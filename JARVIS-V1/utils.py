"""
Small reusable helpers. call_with_retry wraps any network call
so a temporary connection drop (idle-connection resets, brief
network hiccups) doesn't crash the whole program - it just
retries automatically before giving up.
"""
import time


def call_with_retry(func, *args, max_retries=3, **kwargs):
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            print(f"Retrying after error: {e}")
            time.sleep(1)