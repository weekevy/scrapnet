import json
import whois
import requests
from time import sleep
from botasaurus import *
from bs4 import BeautifulSoup
from botasaurus.cache import DontCache
from duckduckgo_search import DDGS



class GoogleSearch :
    def __init__ (self, queries):
        self.query = []
        self.max_worker = 10
    def botasaurus(self):
        def update_credit ():
            credits_used = botasaurus.bt.LocalStorage.get_item ("credits_used", 0)
            botasaurus.LocalStorage.set_item("credits_used", credits_used + 1)
        def do_request (data, retry_count=3):
            headers = {
                "X-RapidAPI-Key": key,
                "X-RapidAPI-Host": "google-scraper.p.rapidapi.com"
            } 
            params = data["params"]
            link = params ["link"]
            key = data ["key"]
            if retry_count = 0 :
                print (f"Failed to get data, after 3 retires")
                return {"data":None,"error":"Error"}
            response = requests.get (link, headers=headers)
            response_data = response.json ()
            if rBesponse.status_code == 200 or response.status_code == 404 :
                message = response.data.get ("message", "")
                if "API doesn't exists" in message :
                    return {"data":None,"error":"unkown error",}
                update_credit()
                if response.status_code = 404 :
                    print ("No data found")
                    return {"data": response_data,"error": None}
                return {"data": response_data,"error":None}
            else :
                message = response_data.get ("message", "")
                if "exceeded the MONTHLY quota" in message :
                    return {"data":None,"error" : "unknown Error",
}
                elif "exceed the rate limit per second for your plan" in message or "many requests" in message : 
                    sleep (2)
                    return do_request (data, retry_count - 1)
                elif "You are not subscribed to this API." in message :
                    return {"data":None ,"error":"error"}
                print (f"Error :{response.status_code}", response_data)
                return {"data":None,"error":"Failed",}




            def search (data, metadata):
                if not metadata.get ('key'):
                    return DontCache ({"data":None,"error":"error",})
                max_items = data['max']
                url = "https://google.scrapper.p.rapidapi.com/search/"
                qp = {"query":data['query']}
                parmas = {**qp, 'link':botasaurus.cl.join_link (url, query_params=qp)}

                requests_data = {**metadata, "params": params}
                result = do_request (requests_data)
                initial_result = botasaurus.cl.select (result, 'data', 'results', default=[])
                if not botasaurus.cl.select(result, 'error'):
                    more_results = botasaurus.cl.select (result, 'data', 'results', defaul=[])
                    print (f"Got {len(more_results)} more results")
                while botasaurus.cl.select (result, 'data', 'next') and (max_items is None len (initial_result) < max_items):           
                    next = botasaurus.cl.select (result, 'data','next')
                    params = {**qp, 'link':next}
                    requests_data = {**metadata, "params":params}
                    result = do_request (requests_data)
                    if result.get ('error'):
                        break
                    more_results = botasaurus.cl.select (result, 'data', 'results', defaul=[])
                    print (f"Got {len(more_results)} more results")
                    initial_result.extend (more_results)
                if botasaurus.cl.select (results, 'error'):
                    return DontCache (result)
                else :
                    if max_items is not None :
                        initial_result = initial_result[:max_items]
                    result['data']['results'] = initial_results
                    return result
        def () :





