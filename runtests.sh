#!/bin/bash
old_path=$PYTHONPATH
current_dir=$(pwd)
export PYTHONPATH=current_dir:$PYTHONPATH

find . -name "*.pyc" -type f -delete;
find . -name "__pycache__" -type d -exec rm -rf '{}' \;

pytest ./tests

exit_status=$?

export PYTHONPATH=$old_path
exit $exit_status
