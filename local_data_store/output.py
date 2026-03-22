"""
Formatted output for LocalDataStore
"""

def output(message: str = None):
    if message:
        print(r"[LDS] " + message)