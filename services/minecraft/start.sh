#!/bin/bash

# This loop replicates your :start label
while true
do
    echo "Starting Purpur Server..."
    # We use the same flags and jar name from your .bat
    java -Xmx8G -Xms8G -XX:+UseG1GC -jar purpur-1.21.11-2561.jar nogui

    echo "Server crashed! Restarting in 5 seconds..."
    echo "Press Ctrl+C to stop this loop."
    sleep 5
done
