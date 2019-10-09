# Messaging Service

A messaging service that can be used to send messages to different service providers.

1; Requirements

    ``` 
    python>=3.6
    gunicorn==19.9.0
    WebOb==1.8.5
    parse==1.12.1
    pycodestyle==2.5.0
    celery==4.3.
    redis==3.3.8
    requests
    ```

## SetUp

Clone project `git clone https://github.com/pmutua/sms-service.git`

Make sure  you have already installed [virtualenv](https://pypi.org/project/virtualenv/)

`cd` into directory then  run:

`virtualenv -p python3 env`

`source env/bin/activate`

`pip install -r requirements.txt`

Then run: `gunicorn app:app`

### Making requests

Sending SMS

**Example:**

**POST** `https://sms-serv.herokuapp.com/api/send_sms/`

HEADERS   `Content-Typeapplication/json`

BODY `raw`:
    {
        "msg":"Text containing message",
        "phoneNumber":["+2547XXXXXX"]
    }

The postman collection can be found [here](https://documenter.getpostman.com/view/8315062/SVtTz8wH?version=latest)
