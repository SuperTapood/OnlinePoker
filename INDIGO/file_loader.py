import os

from INDIGO.exceptions import UnsupportedExtensionError
from INDIGO.image import Image

sound_extensions = []
video_extensions = []
image_extension = ["png", "jpeg", "jpg"]


def load_image(loc):
    return Image(loc)


def load_file(path, file):
    print(file)
    ext = file.split(".")[1]
    loc = path + "\\" + file
    out = ""
    if ext in sound_extensions:
        out = load_sound(loc)
    elif ext in video_extensions:
        out = load_video(loc)
    elif ext in image_extension:
        out = load_image(loc)
    elif ext != "ini":
        raise UnsupportedExtensionError(file, loc, ext)
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
