from api import API

app = API()

@app.route("/home/")
def home(request, response):
    response.text = "Test home end point"

@app.route("/about/")
def about(request, response):
    response.text = "Test about end point"