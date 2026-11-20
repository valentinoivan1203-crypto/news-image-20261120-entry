#!/usr/bin/env python3
"""news-image-20261120 entrypoint (Python 3.13, standard library only).

Copies the entry image beside this file to /output/entry.png
(or $MAKEFUN_OUTPUT_DIR/entry.png outside the grader's container).
Runs with no network and writes the same bytes every run.
The image itself was drawn from the day's reporting; this program only copies it.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
