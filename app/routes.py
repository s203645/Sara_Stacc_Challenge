from flask import render_template
from app import app
import urllib.request, json


url1 = "https://future-of-fintech-v2023.vercel.app/api/consumption"
url2 = "https://future-of-fintech-v2023.vercel.app/api/providers"

response1 = urllib.request.urlopen(url1)
response2 = urllib.request.urlopen(url2)

data1 = response1.read()
data2 = response2.read()

dict1 = json.loads(data1)
dict2 = json.loads(data2)

# API 1
consumption = []
time = []
for i in dict1:
    consumption.append(i["consumption"])
    time.append(i["from"][8:13])


@app.route("/")
@app.route("/home")
def home():
    url = "https://future-of-fintech-v2023.vercel.app/api/providers"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    provider = []
    for i in dict:
        provider.append(i)
    mConsumption = int(sum(consumption) * 0.5 * 1.5)
    for i in provider:
        if i == provider[0]:
            i["total_consumption"] = mConsumption - 1
        else:
            i["total_consumption"] = mConsumption
    print(provider[0]["total_consumption"])

    return render_template(
        "home.html", labels=time, values=consumption, provider=provider
    )


@app.route("/developer")
def developer():
    return render_template("developer.html", title="Developer")


@app.route("/CV")
def CV():
    return render_template("cv.html", title="CV")