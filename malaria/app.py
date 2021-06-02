from __future__ import division, print_function
import sys
import os
import glob
import re
import numpy as np
from tensorflow.keras.applications.imagenet_utils import preprocess_input, decode_predictions
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename
from flask import Flask, redirect, url_for, request, render_template


