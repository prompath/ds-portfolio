import os
import sys

from dotenv import find_dotenv

def append_env_path():
    sys.path.append(os.path.dirname(find_dotenv()))