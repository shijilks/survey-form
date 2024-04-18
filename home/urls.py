# urls.py
from django.urls import path
from .views import survey_view
from . import views

urlpatterns = [
    path('', survey_view, name='survey'),
    path('thank-you/<int:participant_id>/', views.thank_you_page, name='thank_you_page'),
    path('edit/<int:participant_id>/', views.edit_participant, name='edit_participant'),
    path('delete/<int:participant_id>/', views.delete_participant, name='delete_participant'),
]


