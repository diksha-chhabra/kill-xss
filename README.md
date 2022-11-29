# kill-xss
XSS Exploitation Tool/ Finding Unfiltered Inputs 
This tool is an XSS detection tool that uses manual techniques to look for reflected cross-site scripting (XSS) vulnerabilities.
This tool does not take a list of known XSS vectors and fuzz its way through the target site. Instead, the tool takes a surgical approach and follows the same process that a human pen tester follows when looking for reflected XSS vulnerabilities. 
1. Tools ask for the target url
2. List of payloads which one by one itirated on all the inputs
3. Observes the response to see if any of the parameters are present (a "reflection");
4. Test if payload(s) directly reflects in response or not that detects its unfiltered or filtered respectively.

# Prerequisites 
Install BeautifulSoup Module

```$ pip install beautifulsoup4```

```$ python -m pip install beautifulsoup4```

```$ python -m pip install requests```

# Running the tool
Make /xss directory in your pwd, then

```$ python3 <path-to-code>/kill-xss.py```
