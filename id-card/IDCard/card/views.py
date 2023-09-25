from django.shortcuts import render

def user_panel_view(request):
    return render(request, 'user_panel.html')