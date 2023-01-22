from decouple import config

user=config('username')
password=config('password')

print(user,password)
