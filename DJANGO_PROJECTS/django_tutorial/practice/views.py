from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def practice_view(request):
    context = {
        'list_of_numbers': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'greeting': "Hello, World!",
        'user_info': {
            'first_name': "John",
            'last_name': "Doe",
            'email': "john.doe@example.com"
        },
        'is_vip': False,
        'notes': "<strong>Note:</strong> Always learn something new!",
        'now': datetime.now()
    }
    return render(request, 'practice_page.html', context)
