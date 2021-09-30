import bobo

'''
bobo -f bobo-demo.py
curl localhost:8080/?username=Bobby
'''


@bobo.query("/")
def hello(username):
    return f"Hello {username}!"
