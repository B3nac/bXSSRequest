import requests
import sys
import urllib.parse
import tc

payloads = ['','']
url_array = []
payload_array = []

def populate_array():
    with open(str(sys.argv[1])) as f:
        for line in f:
            url_array.append(str(line))
    f.close()

def encoded_request(rt):
    if sys.argv[4] in {"-user-agent"}:
        for line in range(len(url_array)):
            for pay in payloads:
                url = line
                try:
                    if sys.argv[2] in {"-e"}:
                        encpay = urllib.parse.quote(pay)
                        headers = {'user-agent': encpay}
                        gr = requests.get(url_array[url], headers=headers, timeout=3)
                        pr = requests.post(url_array[url], headers=headers, timeout=3)
                    else:
                        headers = {'user-agent': pay, 'referer': pay}
                        gr = requests.get(url_array[url], headers=headers, timeout=3)
                        pr = requests.post(url_array[url], headers=headers, timeout=3) 
                    if rt == "-get":
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                        print(tc.tcolors.SYNTAX + str(gr.url) + tc.tcolors.ENDC)
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                        print(tc.tcolors.SYNTAX + str(gr.request.headers) + tc.tcolors.ENDC)
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                    if rt == "-post":
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                        print(tc.tcolors.SYNTAX + str(pr.url) + tc.tcolors.ENDC)
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                        print(tc.tcolors.SYNTAX + str(pr.request.headers) + tc.tcolors.ENDC)
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                except Exception as e:
                    print(tc.tcolors.WARNING + "OH NO! :" + repr(e) + tc.tcolors.ENDC)
                finally:
                    print("Request complete!")
    if sys.argv[4] in {"-referer"}:
        for line in range(len(url_array)):
            for pay in payloads:
                try:
                    encpay = urllib.parse.quote(pay)
                    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36','referer': encpay}
                    url = line
                    gr = requests.get(url_array[url], headers=headers, timeout=3)
                    pr = requests.post(url_array[url], headers=headers, timeout=3) 
                    if rt == "-get":
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                        print(tc.tcolors.SYNTAX + str(gr.url) + tc.tcolors.ENDC)
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                        print(tc.tcolors.SYNTAX + str(gr.request.headers) + tc.tcolors.ENDC)
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                    if rt == "-post":
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                        print(tc.tcolors.SYNTAX + str(pr.url) + tc.tcolors.ENDC)
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                        print(tc.tcolors.SYNTAX + str(pr.request.headers) + tc.tcolors.ENDC)
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                except Exception as e:
                    print(tc.tcolors.WARNING + "OH NO! :" + repr(e) + tc.tcolors.ENDC)
                finally:
                    print("Request complete!")
    if sys.argv[4] in {"-cookie"}:
        for line in range(len(url_array)):
            for pay in payloads:
                try:
                    encpay = urllib.parse.quote(pay)
                    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
                    cookies = {'session': encpay}
                    url = line
                    gr = requests.get(url_array[url], headers=headers, cookies=cookies, timeout=3)
                    pr = requests.post(url_array[url], headers=headers, cookies=cookies, timeout=3) 
                    if rt == "-get":
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                        print(tc.tcolors.SYNTAX + str(gr.url) + tc.tcolors.ENDC)
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                        print(tc.tcolors.SYNTAX + str(gr.request.headers) + tc.tcolors.ENDC)
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                    if rt == "-post":
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                        print(tc.tcolors.SYNTAX + str(pr.url) + tc.tcolors.ENDC)
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                        print(tc.tcolors.SYNTAX + str(pr.request.headers) + tc.tcolors.ENDC)
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                except Exception as e:
                    print(tc.tcolors.WARNING + "OH NO! :" + repr(e) + tc.tcolors.ENDC)
                finally:
                    print("Request complete!")
    if sys.argv[4] in {"-all"}:
        for line in range(len(url_array)):
            for pay in payloads:
                try:
                    encpay = urllib.parse.quote(pay)
                    cookies = {'session': encpay}
                    headers = {'user-agent': encpay, 'referer': encpay}
                    url = line
                    gr = requests.get(url_array[url], headers=headers, cookies=cookies, timeout=3)
                    pr = requests.post(url_array[url], headers=headers, cookies=cookies, timeout=3) 
                    if rt == "-get":
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                        print(tc.tcolors.SYNTAX + str(gr.url) + tc.tcolors.ENDC)
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                        print(tc.tcolors.SYNTAX + str(gr.request.headers) + tc.tcolors.ENDC)
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                    if rt == "-post":
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                        print(tc.tcolors.SYNTAX + str(pr.url) + tc.tcolors.ENDC)
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                        print(tc.tcolors.SYNTAX + str(pr.request.headers) + tc.tcolors.ENDC)
                        print(tc.tcolors.SUCCESS + "===================================================" + tc.tcolors.ENDC)
                except Exception as e:
                    print(tc.tcolors.WARNING + "OH NO! :" + repr(e) + tc.tcolors.ENDC)
                finally:
                    print("Request complete!")

def request_type():
    if sys.argv[3] in {"-GET", "-get"}:
        get_request = "-get"
        return get_request
    if sys.argv[3] in {"-POST", "-post"}:
        post_request = "-post"
        return post_request
        
def main():
    try:
        if sys.argv[1] in {"-help"}:
            print(tc.tcolors.SYNTAX + "Default request requires 'python3 bXSSRequest.py filewithurls -option -requesttype -payloadtype'.\n\n" + tc.tcolors.ENDC
            + tc.tcolors.SUCCESS + "[Current options]: \n" + tc.tcolors.ENDC
            + "--------------------------\n"
            "-ne : Plaintext request.\n"
            "--------------------------\n"
            "-e  : URL encoded request.\n"
            "--------------------------\n"
            + tc.tcolors.SUCCESS + "[Request types]:\n" + tc.tcolors.ENDC
            + "--------------------------\n"
            "-get : Get request\n"
            "--------------------------\n"
            "-post : Post request\n"
            "--------------------------\n"
            + tc.tcolors.SUCCESS + "[Payload options]\n" + tc.tcolors.ENDC
            + "--------------------------\n"
            "-user-agent : User agent injecton.\n"
            "--------------------------\n"
            "-referer : Referer injection.\n"
            "--------------------------\n"
            "-cookie : Cookie injection.\n"
            "--------------------------\n"
            "-all : Inject all useragent, referer, and cookie.\n"
            "--------------------------\n"
             + tc.tcolors.ENDC)
            return
        elif sys.argv[2] in {"-e"}:
            populate_array()
            encoded_request(request_type())
        elif sys.argv[2] in {"-ne"}:
            populate_array()
            encoded_request(request_type())
    except IndexError as e:
        print(tc.tcolors.WARNING + "Argument option needed. Add -help for required argugments." + repr(e) + tc.tcolors.ENDC)
main()

