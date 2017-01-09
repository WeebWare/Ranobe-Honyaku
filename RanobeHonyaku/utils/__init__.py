import sys
import ujson

try:
    with open("./config.json") as file:
        CONFIG = ujson.load(file)
except FileNotFoundError:
    print("config.json not found.")
    sys.exit(-1)
