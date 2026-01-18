import sys
import os

def setup_path():
    # Add code/raid to sys.path
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    raid_path = os.path.join(project_root, 'code', 'raid')
    if raid_path not in sys.path:
        sys.path.append(raid_path)
