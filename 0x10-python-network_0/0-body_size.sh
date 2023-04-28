#!/bin/bash
# Display the size of body of the response in bytes
curl -s "$1" | grep Content-Length | awk '{print $2}'
