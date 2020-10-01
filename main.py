from deta import App, Deta
from fastapi import FastAPI, Request, responses
from fastapi.staticfiles import StaticFiles

deta = Deta()
db = deta.Base("people")  # init the DB

# We are wrapping FastAPI with a Deta wrapper to be able to use `deta run`
# See line 31. It's optional.
app = App(FastAPI())
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def index():
    return responses.HTMLResponse(open("./index.html").read())


@app.post("/data")
async def post(r: Request):
    items = await r.json()
    for item in items:
        db.put(item)
    return item


@app.get("/data")
async def get():
    return next(db.fetch())


# This command removes all the data frm the DB
# To trigger it, run `deta run` in the project's root
@app.lib.run()
def reset_db(event):
    for item in next(db.fetch()):
        db.delete(item["key"])
