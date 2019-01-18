# bXSSRequest
When I was reading guides on how to find blind XSS I took their advice quite literally and made a tool that would spray payloads at a list of urls or endpoints in request headers.

#### Advisory: This is meant for ethical purposes, I don't condone any bafoonery. 

### What do I need to do to make this work?

Add your payloads to the `payloads = ['','']` in the script from XSSHunter or your server.

Still testing and will add more stuff later, like a form crawler etc.

### Example Commands

`python3 bXSSRequest.py -help`

`python3 bXSSRequest.py file.txt -e -get -user-agent`

`python3 bXSSRequest.py file.txt -e -post -referer`

`python3 bXSSRequest.py test.txt -ne -post -cookie`

`python3 bXSSRequest.py test.txt -e -post -all`

---

#### Encoding options: 

-ne : Plaintext request.

-e  : URL encoded request.

---

#### Request types:

-get : Get request

-post : Post request

---

#### Payload options:

-user-agent : User agent injecton.

-referer : Referer injection.

-cookie : Cookie injection.

-all : Inject all useragent, referer, and cookie.

### F.A.Q.

Why is this not in Go?

Because I'm not the kind of person that follows the trend.