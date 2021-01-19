import numpy as np
import pandas as pd
import logging
import requests
import os
import csv

from pathlib import Path

ROOTDIR = Path(os.path.dirname(__file__)) / '..'