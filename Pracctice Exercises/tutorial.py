import os
from pathlib import Path

for p in Path().iterdir():
    print(p.stem)