# -*- coding: utf-8 -*-
"""
Created on Tue May 17 12:30:11 2022

@author: OPO068499
"""


import logging
from kiteconnect import KiteConnect
import requests

from fastapi import FastAPI,Request

app = FastAPI()
    
apikey=""
apisecret=""


@app.get("/getdata")
async def getInformation(info : Request):
    req_info = await info.json()
    requests.get('https://1point1.in/test/index.php?data='+str(req_info))
    return {
        "status" : "SUCCESS",
        "data" : req_info
    }


@app.get("/")
def buyit(data:str):
    #loginzerodha(symbol,qn,tp)
    print(Request.json())
    req_info = Request.json()
    print(req_info)
    #requests.get('https://1point1.in/test/index.php?data='+req_info)
    
    return "Added data"


logging.basicConfig(level=logging.DEBUG)

def loginzerodha(symbol,qn,tp):
    kite = KiteConnect(api_key=apikey)
    requesttoken=kite.login_url()
    data = kite.generate_session(requesttoken, api_secret=apisecret)
    kite.set_access_token(data["access_token"])
    placeorder(symbol,qn,tp,kite)


def placeorder(symbol,qn,kite,tp):
    try:
        if tp==0:
            ttype=kite.TRANSACTION_TYPE_BUY
        else:
            ttype=kite.TRANSACTION_TYPE_SELL
            
        order_id = kite.place_order(tradingsymbol="INFY",
                                exchange=kite.EXCHANGE_NSE,
                                transaction_type=ttype,
                                quantity=1,
                                variety=kite.VARIETY_AMO,
                                order_type=kite.ORDER_TYPE_MARKET,
                                product=kite.PRODUCT_CNC,
                                validity=kite.VALIDITY_DAY)

        logging.info("Order placed. ID is: {}".format(order_id))
    except Exception as e:
        logging.info("Order placement failed: {}".format(e.message))
    
    




# Redirect the user to the login url obtained
# from kite.login_url(), and receive the request_token
# from the registered redirect url after the login flow.
# Once you have the request_token, obtain the access_token
# as follows.



