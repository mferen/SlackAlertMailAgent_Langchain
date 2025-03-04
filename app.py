import os
from slack_bolt import App
from slack_bolt.adapter.fastapi import SlackRequestHandler

import AiAgent

app = App(token=os.environ.get("SLACK_BOT_TOKEN"), signing_secret=os.environ.get("SLACK_SIGNING_SECRET"))
app_handler = SlackRequestHandler(app)



@app.event("app_mention")
def handle_app_mentions(body, say, logger):
    logger.info(body)
    say("What's up?")


@app.event("message")
def handle_message(body, say, logger):
    jsn_obj=body.get('event', {})
    logger.info(body)
    slackMessage = jsn_obj.get('text')
     
    return AiAgent.main(slackMessage)
    

from fastapi import FastAPI, Request
api = FastAPI()

@api.post("/slack/events")
async def endpoint(req: Request):
    return await app_handler.handle(req)

@api.get("/slack/install")
async def install(req: Request):
    return await app_handler.handle(req)

@api.get("/slack/oauth_redirect")
async def oauth_redirect(req: Request):
    return await app_handler.handle(req)

@api.get("/", status_code=201)
async def callback(req: Request):
    return {"http":"ok"}

@api.get("/ai", status_code=201)
async def deneme(req: Request):
    return AiAgent.main("aaaaaaaaaa")
    #return {"http":"bbbb"}   
