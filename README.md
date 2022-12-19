# dashboard-streamlit

Dataset: https://www.kaggle.com/datasets/deepu1109/star-dataset <br>
Reference about Hertzsprung-Russell Diagram: https://astronomy.swin.edu.au/cosmos/h/hertzsprung-russell+diagram <br>
At one point when I was trying to run app.py, I got this error: <br>
"OSError: [Errno 24] inotify instance limit reached." <br>
To resolve this, I used: sudo nano /etc/sysctl.conf  <br>
Then, I added: fs.inotify.max_user_instances = 1100000 to the bottom of file and saved changes <br>
Finally, I used sudo sysctl -p and was able to run my app.py <br>