#  Copyright (c)
#  Project : project2-E19
#
#  --
#
#  Author : thibault
#  File : tazmouApp.py
#  Description : *Enter description here*
#
#  --
#
#  Last modification : 2022/4/1
#
#  --
#
#  Author : thibault
#  File : tazmouApp.py
#  Description : File to start the web app
#
#  --
#
#  Last modification : 2022/3/30

# Import needed packages


# Import personal packages
from App import create_app

# Start app if file is not imported
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5454)
