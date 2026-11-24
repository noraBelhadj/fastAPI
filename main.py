from fastapi import FastAPI, HTTPException
#from data import users_db 
users_db = [
    {
        'user_id': 1,
        'name': 'Alice',
        'subscription': 'free tier'
    },
    {
        'user_id': 2,
        'name': 'Bob',
        'subscription': 'premium tier'
    },
    {
        'user_id': 3,
        'name': 'Clementine',
        'subscription': 'free tier'
    }
]

api = FastAPI(
    title='My API'
)


@api.get('/item/{itemid}')
def get_item_default(itemid):
    return {
        'route': 'dynamic',
        'itemid': itemid,
        'source': 'string'
    }

@api.get('/item/{itemid:float}')
def get_item_float(itemid):
    return {
        'route': 'dynamic',
        'itemid': itemid,
        'source': 'float'
    }

@api.get('/users')
def get_users():
    return users_db

@api.get('/users/{userid}')
def get_user(userid):
    for user in users_db:
        user['user_id'] = userid
        return user

@api.get('/users/{userid:int}/name')
def get_user_name(userid):
    user = {}
    for user_sb in users_db:
        if int(user_sb['user_id']) == userid:
            user = user_sb['name']
    return user

@api.get('/users/{userid:int}/subscription')
def get_user_name(userid):
    for user_sb in users_db:
        if int(user_sb['user_id']) == userid:
            return user_sb['subscription']      
    raise HTTPException(status_code=404, detail="User not found")

@api.get('/arg')
def get_argument(argument):
    return {'data' : argument}


    

