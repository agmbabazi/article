#!/bin/bash

echo "Stopping and removing existing containers..."
sudo docker-compose down

echo "Building images..."
sudo docker-compose build

echo "Starting containers in detached mode..."
sudo docker-compose up -d

echo "Waiting for services to start..."
sleep 5

echo "All services are up. Showing container status:"
sudo docker-compose ps
