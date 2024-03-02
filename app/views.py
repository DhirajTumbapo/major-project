from django.shortcuts import render
from pathlib import Path
import os
import tensorflow as tf
from tensorflow.keras.models import load_model

# Get the current working directory
working_dir_path = Path.cwd()


# Create your views here.
detection = load_model(os.path.join(working_dir_path, 'app', 'model', 'model.h5'))


def index(request):
    return render(request, "index.html")
