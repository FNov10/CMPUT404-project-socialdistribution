import requests
import base64
from rest_framework.response import Response
from rest_framework import status

# def getNodeAuthors_social_distro():

#     #https://social-distro.herokuapp.com/api/authors/15/
#     url = 'https://social-distro.herokuapp.com/api/authors/'

#     username = 'remote1'
#     password = 'r3mot31'
#     #remote1:r3mot31
#     credentials = f'{username}:{password}'
#     encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
#     authorization_header = f'Basic {encoded_credentials}'
#     headers = {'Authorization': authorization_header}

#     response = requests.get(url, headers=headers)
   
#     status_code = response.status_code
#     json_response = response.json()
#     authors = json_response['results']
#     return authors


def getNodeApp2():
    #https://social-distro.herokuapp.com/api/authors/15/
    url = 'https://killme.herokuapp.com/authors/'
    hosturl = 'https://killme.herokuapp.com/'

    username = 'app1team15'
    password = 'hari1234'
    #remote1:r3mot31

    session = requests.Session()
    session.auth = (username, password)

    auth = session.post(hosturl)
    response = session.get(url)

    # credentials = f'{username}:{password}'
    # encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
    # authorization_header = f'Basic {encoded_credentials}'
    # headers = {'Authorization': authorization_header}

    # response = requests.get(url, headers=headers)
   
    #status_code = response.status_code
    json_response = response.json()
    authors = json_response['results']
    print(authors)
    return authors

def getNodeAuthors_Yoshi():
    url = 'https://yoshi-connect.herokuapp.com/authors'
    #base64encoded username: minion and password: minion
    # authorization = 'minion:minion'
    # encoded_authorization = base64.b64encode(authorization.encode("utf-8"))
    # authroization_header = 'Basic ' + encoded_authorization
    # headers = {'Authorization': authroization_header}
    
    response = requests.get(url)
    status_code = response.status_code
    # response = requests.get(url, headers=headers)
    json_response = response.json()
    authors = json_response['items']
    return authors


def getNodeAuthor_Yoshi(author_id):
    url = 'https://yoshi-connect.herokuapp.com/authors/'

    url = url + author_id

    response = requests.get(url)
    status_code = response.status_code
    
    if status_code == 200:
        json_response = response.json()
       
        return(json_response, status_code)
    else: return (None, status_code)

def getNodeAuthor_App2(author_id):
    url = 'https://killme.herokuapp.com/authors/'
    hosturl = 'https://killme.herokuapp.com/'

    url = url + author_id

    response = requests.get(url)
    status_code = response.status_code
    
    if status_code == 200:
        json_response = response.json()
       
        return(json_response, status_code)
    else: return (None, status_code)

#29c546d45f564a27871838825e3dbecb
# getNodeAuthor_Yoshi('asgasdfgdsfgd')
# getNodeAuthor_Yoshi('29c546d45f564a27871838825e3dbecb')

def getNodeAuthor_social_distro(author_id):
    url = 'https://social-distro.herokuapp.com/api/authors/https://social-distro.herokuapp.com/authors/'

    url = url + author_id

    response = requests.get(url)
    status_code = response.status_code
   
    if status_code == 200:
        json_response = response.json()

        return(json_response, status_code)
    else: return (None, status_code)


####### GET POSTS

def getNodePost_Yoshi(author_id):
    url = 'https://yoshi-connect.herokuapp.com/authors/'

    url = url + author_id + '/posts/'
    
    response = requests.get(url)
    status_code = response.status_code
   
    if status_code == 200:
        json_response = response.json()
        return(json_response, status_code)
    else: return (None, status_code)

def getNodePost_app2(author_id):
    url = 'https://killme.herokuapp.com/posts/authors/'
    hosturl = 'https://killme.herokuapp.com/'

    url = url + author_id + '/posts/'
    username = 'app1team15'
    password = 'hari1234'
    #remote1:r3mot31

    session = requests.Session()
    session.auth = (username, password)

    auth = session.post(hosturl)
    response = session.get(url)
    
    # credentials = f'{username}:{password}'
    # encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
    # authorization_header = f'Basic {encoded_credentials}'
    # headers = {'Authorization': authorization_header}

    # response = requests.get(url, headers=headers)
    #  response = requests.get(url)
    status_code = response.status_code
    if status_code == 200:
        json_response = response.json()
        return(json_response)

#29c546d45f564a27871838825e3dbecb
# getNodeAuthor_Yoshi('asgasdfgdsfgd')
# getNodeAuthor_Yoshi('29c546d45f564a27871838825e3dbecb')

def getNodePost_social_distro(author_id):
    url = 'https://social-distro.herokuapp.com/api/authors/'

    url = url + author_id + '/posts/'
    username = 'remote1'
    password = 'r3mot31'
    #remote1:r3mot31
    credentials = f'{username}:{password}'
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
    authorization_header = f'Basic {encoded_credentials}'
    headers = {'Authorization': authorization_header}

    response = requests.get(url, headers=headers)
    #response = requests.get(url)
    status_code = response.status_code
    if status_code == 200:
        json_response = response.json()
        return(json_response)

# import socket

# bytes_to_read = 4096
# HOST = 'yoshi-connect.herokuapp.com'

# def get(port):

#     request = b"GET /authors HTTP/1.1\nHost:" + HOST.encode("utf-8") + b"\n\n"

#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.connect((HOST, port))
#     s.send(request)

#     s.shutdown(socket.SHUT_WR)

#     result = s.recv(bytes_to_read)
#     print(result.decode())
#     # while(len(result) > 0):

#     #         print(result)
#     #         result = s.recv(bytes_to_read)
#     s.close()


    
# get(80)



def postFollow(data, author_id):
    #"type": "Follow",
    #"actor":{"id":"cfd9d228-44df-4a95-836f-c0cb050c7ad6"},
    #"object":{"id":"971fa387-b101-4276-891f-d970f2cf0cad"}

    #     username = 'remote1'
    #     password = 'r3mot31'
    #     #remote1:r3mot31
    #     credentials = f'{username}:{password}'
    #     encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
    #     authorization_header = f'Basic {encoded_credentials}'
    #     headers = {'Authorization': authorization_header}

    #     response = requests.get(url, headers=headers)

    author, status_code = getNodeAuthor_social_distro(author_id)
    if status_code != 200:
        author, status_code = getNodeAuthor_Yoshi(author_id)
        if status_code != 200:
            author, status_code = getNodeAuthor_App2(author_id)
            if status_code != 200:
                error_msg = "Author id not found"
                return Response(error_msg, status=status.HTTP_404_NOT_FOUND)
            # if status_code != 200:
            #     error_msg = "Author id not found"
            #     return Response(error_msg, status=status.HTTP_404_NOT_FOUND)
            # else:
            #     url =  'https://killme.herokuapp.com/authors/{author_id}/inbox'
            #     username = 'app1team15'
            #     password = 'hari1234'
            #     request_data = data

        else:
            url =  'https://yoshi-connect.herokuapp.com/authors/{author_id}/inbox'
            username = "minion"
            password = "minion"
            request_data = {"actor":data.actor}
    else:
        url =  'https://social-distro.herokuapp.com/api/authors{author_id}/inbox'
        username = 'team24'
        password = 'team24'
        '''"author:"urltoauthor", "object":"urltoobject", "type":"Follow", "Summary":"username liked your post"'''
        request_data = {"author":data.actor, "object":data.object, "type":"Follow", "Summary":"A Follow Request"}
    #Make summary manually 
    credentials = f'{username}:{password}'
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")
    authorization_header = f'Basic {encoded_credentials}'
    headers = {'Authorization': authorization_header}
    
    # This should in theory work for the Yoshi APP, Not ready yet so testing when they get it done 
    response = requests.post(url, headers=headers, data=request_data)

    #Check if they return an HTTP response, IF not do HTTP response 200 OK 
    if response.status_code == 200:
        return Response("OK", status=status.HTTP_200_OK)

    ''' Our Way to send a follow request.  
    "type":"Follow",
        "actor": {
                "id": "c164d06a-a922-4535-9c3d-d3ec2cfc4e9a"
                },
        "object": {
            "id": "b7cbbd87-3da4-48a2-ab97-ee0331276412"
                }'''