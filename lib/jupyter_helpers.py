import os
import sys

def append_current_path():
    current_path = os.getcwd()
    print(f"current path {current_path}")
    relative_path=os.path.dirname(current_path)
    print(f"root path {relative_path}")
    sys.path.append(f"{relative_path}")