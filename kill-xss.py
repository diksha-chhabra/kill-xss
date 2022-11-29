
from bs4 import BeautifulSoup as bs 
from urllib.parse import urljoin
import requests 


def get_all_forms(url):
    soup = bs(requests.get(url).content,"html.parser")
    return soup.find_all("form")
    

def get_forms_details(form):
    details = {}

    action = form.attrs.get("action").lower()
    method = form.attrs.get("method","get").lower()

    inputs = [] 
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type","text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name":input_name})

    details["action"] = action 
    details["method"] = method
    details["inputs"] = inputs 

    return details 

def submit_forms(form_details,url,value):

    target_url = urljoin(url,form_details["action"])

    inputs = form_details["inputs"]
    data  = {}

#inputlar
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value 
            input_name = input.get("name")
            input_value = input.get("value")
            if input_name and input_value :
                data[input_name] = input_value 
            if form_details["method"] == "post":
                return requests.post(target_url,data=data)
            else:
                return requests.get(target_url,params=data)


def xss_scanner (url):
    forms = get_all_forms(url)
    print("Searching for XSS vulnerability or inputs not filtered out...")
    
    is_vuln = False 
    for form in forms:
        form_details = get_forms_details(form)

        file = open('Payloads.txt', 'r')
        XSS = file.readlines()

        for xss in XSS:
                xss_payload = xss.strip()

                content = submit_forms(form_details,url,xss_payload).content.decode()

                #print(content)

                if  xss_payload in content:
                    print("=" * 20)
                    print("XSS vulnerability or Unfiltered input detected!")
                    print("Payload: " + xss_payload)
                    print("=" * 20)
                    is_vuln = True

        return is_vuln

if __name__ == "__main__":
    url = input("Enter site address for XSS search: ")
    is_vuln = xss_scanner(url)
