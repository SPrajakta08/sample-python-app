pip3 install Flask
pip3 install requests
ps -ef | grep flaskapp | grep -v grep | awk '{print $2}' | xargs kill
nohup python3 flaskapp.py &
