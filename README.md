# Messaging Service

A messaging service that can be used to send messages to different service providers. Developed the API without using a framework.

1; Requirements

    python>=3.6
    gunicorn==19.9.0
    WebOb==1.8.5
    parse==1.12.1
    pycodestyle==2.5.0
    requests

## SetUp

Clone project `git clone https://github.com/Developer-Gitonga/sms-service.git`

Make sure  you have already installed [virtualenv](https://pypi.org/project/virtualenv/)

`cd` into directory then  run:

`python3 -m venv env`

`source venv/bin/activate`

`pip install -r requirements.txt`

Then run: `gunicorn app:app`

### Making a Request

1;Postman Collection
The postman collection can be found [here](https://documenter.getpostman.com/view/8315062/SVtTz8wH?version=latest)

2;Making requests

Sending SMS

**Example:**

**POST** `https://sms-serv.herokuapp.com/api/send_sms/`

HEADERS   `Content-Typeapplication/json`

BODY `raw`:
    {
        "msg":"Text containing message",
        "phoneNumber":["+2547XXXXXX"]
    }
