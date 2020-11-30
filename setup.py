#! /usr/bin/env python

#
# Licensed to Elasticsearch under one or more contributor
# license agreements. See the NOTICE file distributed with
# this work for additional information regarding copyright
# ownership. Elasticsearch licenses this file to you under
# the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
#

import re
import io
from setuptools import find_namespace_packages, setup

with io.open("dorothy/__init__.py", "rt", encoding="utf8") as f:
    __version__ = re.search(r'__version__ = "(.*?)"', f.read()).group(1)


setup(
    name="dorothy",
    version=__version__,
    description="Dorothy is a tool to test security monitoring and detection for Okta environments",
    author="David French",
    maintainer="Elastic",
    license="Apache License 2.0",
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Security",
    ],
    packages=find_namespace_packages(include=["dorothy*"]),
    include_package_data=True,
    install_requires=open("requirements.txt", "r").read(),
    entry_points={
        "console_scripts": [
            "dorothy=dorothy.main:main",  # this registers a command line tool "dorothy"
        ],
    },
)