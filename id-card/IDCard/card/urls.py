from django.urls import path
from .views import user_panel_view

app_name = 'card'

urlpatterns = [
	path('user', user_panel_view, name='user_panel_view'),
]


