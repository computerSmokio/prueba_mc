#!/bin/sh
HAPROXY_SOCKET="/var/run/haproxy/haproxy.sock"
while true; do                                                                                                                                                                                              
        # Read the incoming command from the client                                                                                                                                                             
        read -r command                                                                                                                                                                                         
                                                                                                                                                                                                                
        # Execute the HAProxy command and send its output to the client                                                                                                                                         
        echo "Executing HAProxy command: $command"                                                                                                                                                              
        echo "$command" | socat - UNIX-CONNECT:"$HAPROXY_SOCKET"                                                                                                                                                
done