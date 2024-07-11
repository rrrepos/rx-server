cd ~/rx-server
sudo cp ./shell/rx-server.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable rx-server.service
sudo systemctl start rx-server.service