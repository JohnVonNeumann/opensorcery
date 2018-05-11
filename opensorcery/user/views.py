from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import json
# Create your views here.

@login_required
def welcome(request):
    return render(request, "welcome.html")
#    user = request.user
#    # the auth operation generates a user dict
#    # then in social_django/storage.py the social_auth object is created
#    # which is effectively a db op 
#    auth0user = user.social_auth.get(provider="auth0")
#    userdata = {
#        'user_id': auth0user.uid,
#        'name': user.first_name,
#        'picture': auth0user.extra_data['picture']
#    }
#    
#    return render(request, 'welcome.html', {
#        'auth0User': auth0user,
#        'userdata': json.dumps(userdata, indent=4)
#    })
#
# post creds to the /login/auth0 AUTH0 handled url, then assert that the information provided back from the /welcome screen is correct is correct
