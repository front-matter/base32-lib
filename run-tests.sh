#!/bin/sh
# SPDX-FileCopyrightText: 2019 CERN.
# SPDX-FileCopyrightText: 2019 Northwestern University.
# SPDX-License-Identifier: MIT

pydocstyle base32-lib tests && \
isort --recursive --check-only --diff **/*.py && \
check-manifest --ignore ".travis-*" && \
sphinx-build -qnNW docs docs/_build/html && \
python setup.py test
