# note: on os x, you may need to install XCode from the app store, and then run this
# command to make sure it works:
# sudo /usr/bin/xcodebuild -version -sdk macosx Path

pyvenv venv
chmod +x ./venv/bin/activate
source ./venv/bin/activate
python3 ./pyvenvex.py ./venv
pip3.4 install -r requirements.txt
