from django import forms
from ticket_app.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event  # Link to the Event model
        fields = ['event_title', 'event_description', 'event_date', 'event_time', 'event_address', 'event_capacity', 'event_price']  # Fields you want to include in the form
        widgets = {
            'event_title': forms.TextInput(attrs={'class': 'form-control'}),
            'event_description': forms.Textarea(attrs={'class': 'form-control'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'event_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'event_address': forms.TextInput(attrs={'class': 'form-control'}),
            'event_capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'event_price': forms.NumberInput(attrs={'class': 'form-control'})
        }

    def clean_event_title(self):
        event_title = self.cleaned_data['event_title']
        if Event.objects.filter(event_title=event_title).exists():
            raise forms.ValidationError(f"Event with the title '{event_title}' already exists.")
        return event_title



class TicketPurchaseForm (forms.Form):
    # Event field is hidden and populated via the view
    event = forms.ModelChoiceField(
        queryset=Event.objects.all(),  # Dynamically fetch all events
        label="Select Event",
        widget=forms.HiddenInput(), 
    )
    ticket_quantity = forms.IntegerField(
        min_value=1,
        label="Number of Tickets",
         widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    ticket_type = forms.ChoiceField(
        choices=Ticket.Ticket_CHOICES,
        label="Ticket Type",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=254, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )






