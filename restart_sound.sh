#!/bin/bash

# Stop the ALSA sound system
sudo alsa force-reload

# Optionally, you can add a delay to give the system some time to stop the services properly
sleep 2

# Start the ALSA sound system again
sudo alsactl init

echo "Sound system has been restarted."
