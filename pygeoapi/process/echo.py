# =================================================================
#
# Authors: Alexander Pilz <a.pilz@52north.org>
#
# Copyright (c) 2023 Alexander Pilz
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================
import logging
import time 
from random import *

from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError

LOGGER = logging.getLogger(__name__)

#: Process metadata and description
PROCESS_METADATA = {
  "id": "echo",
  "title": "Echo Process",
  "description": "This process accepts a string input value and echoes it back as a result.",
  "version": "1.0.0",
  "jobControlOptions": [
    "async-execute",
    "sync-execute"
  ],
  "outputTransmission": [
    "value",
    "reference"
  ],
  "inputs": {
    "echoInput": {
      "title": "Echo value",
      "description": "This is an example of a String literal input.",
      "minOccurs": 1,
      "maxOccurs": 1,
      "schema": {
        "type": "string",
        "enum": [
          "Echo",
          "Test",
          "42"
        ]
      }},
    "pause": {
      "title": "Pause value",
      "description": "This parameter may be used to control the processing time of the echo process.",
      "minOccurs": 1,
      "maxOccurs": 1,
      "schema": {
        "type": "float",
        "enum": [
          5.5,
          10.25,
          42.0
        ]
      }
    }
  },
  "outputs": {
    "echoOutput": {
      "schema": {
        "type": "string"
      }
    }
  },
  "links": [
    {
      "href": "https://processing.example.org/oapi-p/processes/echo/execution",
      "rel": "http://www.opengis.net/def/rel/ogc/1.0/execute",
      "title": "Execute endpoint",
      "type": "endpoint"
    }
  ],
    'example': {
        'inputs': {
            'echo': 'echoValue',
            'pause': 10.0
        }
    }
}

class echoProcessor(BaseProcessor):
    """Echo Processor example"""

    def __init__(self, processor_def):
        """
        Initialize object

        :param processor_def: provider definition

        :returns: pygeoapi.process.echo.echoProcessor
        """

        super().__init__(processor_def, PROCESS_METADATA)

    def execute(self, data):

        mimetype = 'application/json'

        echo = data.get('echoInput', None)
        pause = data.get('pause', None)

        if echo is None:
            raise ProcessorExecuteError('Cannot run process without echo value')
        if not isinstance(echo, str):
            raise ProcessorExecuteError('Cannot run process with echo not of type String')

        outputs = {
            'id': 'echoOutput',
            'value': echo
        }
        if pause is not None:
          if isinstance(pause, float):
            time.sleep(pause)

        return mimetype, outputs

    def __repr__(self):
        return '<echoProcessor> {}'.format(self.name)