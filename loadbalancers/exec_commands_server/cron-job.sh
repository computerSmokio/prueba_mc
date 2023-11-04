#!/bin/bash

haproxy_response=$(echo "show servers state" | socat stdio tcp-connect:localhost:8082)

echo "Server State Server Name"
awk 'NR>2 {print $6, $4}' <<< "$haproxy_response" | while read state server_name; do
  if [ "$state" == "2" ]; then
    echo "Server $server_name is up."
  elif [ "$state" == "0" ]; then
    echo "Server $server_name is down. Setting instance health to Unhealthy..."
    aws autoscaling set-instance-health --region us-east-1 --instance-id $server_name --health-status Unhealthy
  fi
done