# Newsletter Context

def newsletter(request):
    '''
    Check if newsletter extra signup has been shown in the last 24 hours
    24 hours is the length set for the django session storage to persist in
    settings.py
    '''
    newsletter_shown = request.session.get('newsletter_shown', False)
    if newsletter_shown:
        context = {'show_newsletter_extra_signup': False}
    else:
        context = {'show_newsletter_extra_signup': True}
    return context
