#!/usr/bin/env python
"""
   OPenDCRE Logging Helpers
   Author:  andrew
   Date:    12/7/2015

        \\//
         \/apor IO

Copyright (C) 2015-16  Vapor IO

This file is part of OpenDCRE.

OpenDCRE is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

OpenDCRE is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenDCRE.  If not, see <http://www.gnu.org/licenses/>.
"""
import logging
import logging.config
import os
import json


def setup_logging(
    default_path='logging.json',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """
    Set up default logging configuration.
    :param default_path: The default logging path/
    :param default_level: The default logging level.
    :param env_key: Env key to logging info.
    :return: None.
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
