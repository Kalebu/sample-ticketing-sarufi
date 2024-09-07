from utilities import build_menu
from zenopay import make_payment
from fastapi import FastAPI
from sms import call_agent

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


TICKET_PRICES = {
    "business": '2000',
    "economy": '1000',
    "royal": '3000'
}


@app.post('/pickup')
async def pickup(data:dict):
    print(data)
    return {
      "medias": {
        "images": [
          {
            "link": "https://developers.amadeus.com/PAS-EAS/api/v1/cms-gateway/sites/default/files/inline-images/React-seat-map_wings.png",
            "caption": "Office Location"
          }
        ]
      },
    "text": "Bike is picked up"
    }

@app.post('/drop')
async def drop(data:dict):
    print(data)
    return {
            "send_reply_button": {
                    "type": "button",
                    "body": {"text": "Choose your destination"},
                    "action": {
                        "buttons": [
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "1",
                                    "title": "Dar es Salaam"
                                },
                            },
                            {
                                "type": "reply",
                                "reply": {
                                    "id": "2",
                                    "title": "Morogoro"
                                },
                            },

                            ],
                    },
                },
            }

@app.post('/travel-class')
async def travel_class(data:dict, route_str:str='dar-moro'):
    print(data)
    rows=[]
    if route_str == 'dar-moro':
        rows=[
            {
                "id": "economy",
                "title": "Economy",
                "description": "Economy class",
            },
            {
                "id": "business",
                "title": "Business",
                "description": "Business class",
            },
            {
                "id": "royal",
                "title": "Royal",
                "description": "Royal class",
            }
        ]
    else:
        rows=[
            {
                "id": "economy",
                "title": "Economy",
                "description": "Economy class",
            },
            {
                "id": "business",
                "title": "Business",
                "description": "Business class",
            }
        ]
    return build_menu(
        body="Please select your travel class",
        button="Travel class",
        title="Travel Class",
        rows=rows
    )

@app.post('/seat')
async def seat(data:dict):
    print(data)
    return {
        "send_reply_button": {
            "type": "button",
            "body": {"text": "Choose your seat"},
            "action": {
                "buttons": [
                    {
                        "type": "reply",
                        "reply": {
                            "id": "1",
                            "title": "Window"
                        },
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "2",
                            "title": "Aisle"
                        },
                    },
                    {
                        "type": "reply",
                        "reply": {
                            "id": "3",
                            "title": "Middle"
                        },
                    }
                ],
            },
        },
    }


@app.post('/payment')
async def payment(data:dict):
    print(data)
    travel_class = data.get('travel_date', '')
    amount = TICKET_PRICES.get(travel_class, '1000')
    phone_number = data.get('trigger_payment_confirmation', '')
    reponse = await make_payment(amount, phone_number)
    print(reponse)
    return {'text': ""}

@app.post('/ticket')
async def ticket(data:dict):
    print(data)
    return {"text": "Your ID is 1234. Your ticket is confirmed. Have a safe journey."}


@app.post('/call-agent')
async def call_our_agent(data:dict):
    print(data)
    # call agents
    phone_number = data.get('piga_simu', '')
    response = call_agent(phone_number)
    print(response)
    return {
    "text": ""
    }
