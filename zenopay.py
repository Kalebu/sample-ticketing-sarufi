import httpx
from sms import send_sms

BASE_URL = "https://api.zeno.africa"

async  def make_payment(amount:str, phone_number:str):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/payment", data={
            'create_order': 1,
            'buyer_email': 'vudozo@gmail.com',
            'buyer_name': 'Vudozo',
            'buyer_phone': phone_number ,
            'amount': amount,
            'account_id': 'zp63394',
            'api_key': '',
            'secret_key': '',
        })
        reponse = response.json()
        order_id = reponse.get('order_id', '')
        sms_to_send =f'Please click on this link to pay for your ticket: https://api.zeno.africa/pay/{order_id}'
        send_sms(sms_to_send, phone_number)
        print(reponse)

        # send an SMS to the user
