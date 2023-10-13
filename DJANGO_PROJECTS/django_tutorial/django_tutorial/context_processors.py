from django.conf import settings

def company_name(request):
    # This function makes the COMPANY_NAME available in templates
    return {'COMPANY_NAME': settings.COMPANY_NAME}