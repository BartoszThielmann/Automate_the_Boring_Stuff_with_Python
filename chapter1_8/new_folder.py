import os
from pathlib import Path

for i in range(0,5):
    os.makedirs(Path('C:\\Users\\Bartosz\\Desktop') / str(i))
