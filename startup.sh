kill `ps -ef | grep lifeTracker | cut -f2- -d' ' | grep -v "grep"`

gunicorn lifeTracker.index:server --bind=0.0.0.0:8000 &> output.log &

