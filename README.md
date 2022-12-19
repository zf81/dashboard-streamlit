# dashboard-streamlit

Dataset: https://www.kaggle.com/datasets/deepu1109/star-dataset
Reference about Hertzsprung-Russell Diagram: https://astronomy.swin.edu.au/cosmos/h/hertzsprung-russell+diagram
At one point when I was trying to run app.py, I got this error: 
"OSError: [Errno 24] inotify instance limit reached."
To resolve this, I used: sudo nano /etc/sysctl.conf  
Then, I added: fs.inotify.max_user_instances = 1100000 to the bottom of file and saved changes
Finally, I used sudo sysctl -p and was able to run my app.py 