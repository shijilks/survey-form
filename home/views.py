# views.py
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ParticipantForm
from .models import Participant

def survey_view(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save()
            return redirect('thank_you_page', participant_id=participant.id)
    else:
        form = ParticipantForm()
    return render(request, 'survey_form.html', {'form': form})

def thank_you_page(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    return render(request, 'thank_you_page.html', {'participant': participant})


def edit_participant(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    if request.method == 'POST':
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            # Redirect to thank you page with participant ID
            return redirect('thank_you_page', participant_id=participant.id)
    else:
        form = ParticipantForm(instance=participant)  # Pre-fill form with participant's existing details
    return render(request, 'edit_participant.html', {'form': form})

def delete_participant(request, participant_id):
    participant = get_object_or_404(Participant, pk=participant_id)
    if request.method == 'POST':
        participant.delete()
        return redirect('survey')  # Redirect to a suitable page after deletion
    return render(request, 'delete_participant.html', {'participant': participant})

