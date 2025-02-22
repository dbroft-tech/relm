from django.shortcuts import render

def handler404(request, exception=None):
    context = {
        'error_code': '404',
        'error_title': 'Page Not Found',
        'error_message': "We're sorry, but the page you're looking for cannot be found.",
        'path': request.path,
    }
    response = render(request, 'core/errors/404.html', context)
    response.status_code = 404
    return response

def handler500(request, exception=None):
    context = {
        'error_code': '500',
        'error_title': 'Server Error',
        'error_message': "We're sorry, but something went wrong on our end.",
    }
    response = render(request, 'core/errors/500.html', context)
    response.status_code = 500
    return response

def handler403(request, exception=None):
    context = {
        'error_code': '403',
        'error_title': 'Access Denied',
        'error_message': "You don't have permission to access this page.",
    }
    response = render(request, 'core/errors/403.html', context)
    response.status_code = 403
    return response

def handler400(request, exception=None):
    context = {
        'error_code': '400',
        'error_title': 'Bad Request',
        'error_message': "We couldn't process your request.",
    }
    response = render(request, 'core/errors/400.html', context)
    response.status_code = 400
    return response 