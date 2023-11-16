import argparse
from pathlib import Path

parser = argparse.ArgumentParser("Get arguments and validate from options")

# Mandatory arguments
parser.add_argument("action", help="Present an action that needs to be performed",
                    choices=["execute", "validate", "reaffirm"])

args = parser.parse_args()

print(args)