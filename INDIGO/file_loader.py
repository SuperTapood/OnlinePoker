import os

from INDIGO.exceptions import UnsupportedExtensionError
from INDIGO.image import Image

sound_extensions = []
video_extensions = []
image_extension = ["png", "jpeg", "jpg"]


def load_image(loc, x, y):
    return Image(loc, x, y)


def load_file(path, x, y):
    ext = path.split(".")[1]
    out = ""
    if ext in sound_extensions:
        out = load_sound(path)
    elif ext in video_extensions:
        out = load_video(path)
    elif ext in image_extension:
        out = load_image(path, x, y)
    elif ext != "ini":
        raise UnsupportedExtensionError(path, path, ext)
    return out


def load_all(path):
    out = []
    for file in os.listdir(path):
        out.append(load_file(path, file))
    return out


def load_type(path, ext):
    out = []
    for file in os.listdir(path):
        if file.split(".")[1] == ext:
            out.append(load_file(path, file))
    return out


def load_prefix(path, prefix):
    out = []
    for file in os.listdir(path):
        if file != "desktop.ini":
            if file.split(".")[0][:len(prefix)] == prefix:
                out.append(load_file(path, file))
    return out


def load_type_prefix(path, prefix, ext):
    out = []
    for file in os.listdir(path):
        if file.split(".")[0][:len(prefix)] == prefix and file.split(".")[1] == ext:
            out.append(load_file(path, file))
    return out
