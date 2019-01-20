#Api-caller

Script that calls in a loop to an endpoint with a bulk of data (generally ids)

Writes the response of each call in an outfile.

Logs the calls and response status to verify on the go.

## Options and modifications

The current script accepts OAuth2 token
(If it's not needed it can be left as it is)

The current script has a method to clean cache
(Comment the call to the method if it is not needed)

##Requirements

Python3

Install requests library

    pip3 install requests

Execute

    ./api_caller.py
