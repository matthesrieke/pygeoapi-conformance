import logging
import time 
from random import *
from pygeoapi.process.base import BaseProcessor, ProcessorExecuteError

#execute command
#curl -X POST "http://<host>:<port>/processes/echo/execution" -H "Content-Type: application/json" -d "{\"mode\": \"async\", \"inputs\":{\"echoInput\": \"42\", \"pause\": 10.0"}}"

LOGGER = logging.getLogger(__name__)

#: Process metadata and description
PROCESS_METADATA = {
  "id": "echo",
  "title": "Echo Process",
  "description": "This process accepts a string input value and echoes it back as a result. The processing time of the process may be controlled using the pause parameter.",
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
          "Value1",
          "Value2",
          "Value3"
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
            'echoOutput': echo
        }
        if pause is not None:
          if isinstance(pause, float):
            time.sleep(pause)

        return mimetype, outputs

    def __repr__(self):
        return '<echoProcessor> {}'.format(self.name)