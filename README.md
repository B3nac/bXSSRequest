# bXSSRequest
When I was reading guides on how to find blind XSS I took their advice quite literally and made a tool that would spray payloads everywhere.

Still testing and will add more stuff later, form crawler etc.

###Example Commands

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

