import os

from src import write

path = r'bye\prout\big_list.json'
write(os.path.join(os.getenv('LOCALAPPDATA'), path), "HELLO")