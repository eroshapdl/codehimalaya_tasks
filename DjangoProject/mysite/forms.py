from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)

class StudentForm (forms.Form):
    student_name = forms.CharField (label = "Student Name", max_length=100)
    

