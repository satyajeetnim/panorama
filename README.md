# Panorama
===========

1. Install python version 3.x: brew install python3
2. Install pip3: brew install pip3
3. Make sure python is working fine
    -- Open a terminal window and enter: python3 --version and you see something like this: satyajeet@SNIMGAON-M-V2A1:~/Documents/Personal/company-product/panorama (satyajeet)$ python3 --version
       Python 3.5.1
4. Make sure pip3 is working fine
    -- satyajeet@SNIMGAON-M-V2A1:~/Documents/Personal/company-product/panorama (satyajeet)$ pip3 --version
       pip 9.0.1 from /usr/local/lib/python3.5/site-packages (python 3.5)
5. Install and Run MongoDB with Homebrew: https://treehouse.github.io/installation-guides/mac/mongo-mac.html
6. Start mongodb by entering this in a terminal window: mongod
7. Go to the cloned directory for panorama and enter this on a separate terminal: pip install -r requirements.txt
8. Then run panorama: python3 app.py
    You should see something like this - satyajeet@SNIMGAON-M-V2A1:~/Documents/Personal/company-product/panorama (satyajeet)$ python3         app.py
    app.py:4: ExtDeprecationWarning: Importing flask.ext.pymongo is deprecated, use flask_pymongo instead.
      from flask.ext.pymongo import PyMongo
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
     * Restarting with stat
    app.py:4: ExtDeprecationWarning: Importing flask.ext.pymongo is deprecated, use flask_pymongo instead.
      from flask.ext.pymongo import PyMongo
     * Debugger is active!
     * Debugger PIN: 183-791-518
9. Goto http://localhost:5000 and start testing.
