from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import json
# Create your views here.

@login_required
def welcome(request):
    user = request.user
    auth0user = user.social_auth.get(provider="auth0")
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture']
    }
    
    return render(request, 'welcome.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })

def login(request):
    return render(request, "login.html")
