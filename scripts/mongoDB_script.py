#!/bin/bash

# Update and upgrade packages
sudo apt update
sudo apt upgrade -y

# Acquire the MongoDB 3.2 key
wget -qO - https://www.mongodb.org/static/pgp/server-3.2.asc | sudo apt-key add -
echo "Acquired MongoDB 3.2 key successfully."

# Add MongoDB repository to sources.list
echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list

# Update packages to fetch MongoDB 3.2
sudo apt update

# Install MongoDB 3.2 packages
sudo apt-get install -y mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20
echo "MongoDB 3.2 installed successfully."

# Modify MongoDB configuration to allow all connections
sudo sed -i 's/bindIp: 127.0.0.1/bindIp: 0.0.0.0/' /etc/mongod.conf
echo "Modified MongoDB configuration to allow all connections."

# Start MongoDB and enable auto-start
sudo systemctl start mongod
sudo systemctl enable mongod

# Check MongoDB service status
sudo systemctl status mongod