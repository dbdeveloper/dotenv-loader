#!/bin/bash

set -e

cd "$(dirname "$0")"

rm -rf ../build ../dist ../.pytest_cache ../.coverage

cd ..

echo "Creating build..."
python -m build

echo "Check package..."
twine check dist/*

echo "Uploading to PyPI..."
twine upload dist/*

