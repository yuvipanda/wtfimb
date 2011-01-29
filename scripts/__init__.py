import os
import sys

SCRIPTS_DIR = os.path.dirname(sys.argv[0])
ROOT_DIR = os.path.normpath(os.path.join(os.path.abspath(SCRIPTS_DIR), '..'))
PARENT_DIR = os.path.normpath(os.path.join(os.path.abspath(ROOT_DIR), '..'))
sys.path.append(os.path.abspath(SCRIPTS_DIR))
sys.path.append(ROOT_DIR)
sys.path.append(PARENT_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

