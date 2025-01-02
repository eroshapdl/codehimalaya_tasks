from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm, StudentForm
from django.views import View
from django.views.generic import TemplateView
from django.forms import formset_factory

class HomeView (TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Call the parent's get_context_data method to get the default context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Paudel Niwas'
        context["head"] = 'Welcome to Paudel Niwas test'

        return context



class AboutUsView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello! Welcome")

class CourseDetailsView(View):
    def get(self, request, courseid, *args, **kwargs):
        return HttpResponse(courseid)



class MyFormView (View):
    form_class = NameForm
    initial = {"key": "value"}
    template_name = "yourname.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/thanks/")

        return render(request, self.template_name, {"form": form})


class AddNumbersView(View):
    template_name = "add_numbers.html"

    def get(self, request, *args, **kwargs):
        sum_result = 0
        num1 = request.GET.get('num1')
        num2 = request.GET.get('num2')

        if num1 and num2:
            try:
                sum_result = float(num1) + float(num2)
            except ValueError:
                sum_result = "Invalid input"

        return render(request, self.template_name, {'sum_result': sum_result})
    
def create_student(request):
    StudentFormset = formset_factory(StudentForm, extra=0)  

    if request.method == 'POST':
        formset = StudentFormset(request.POST)
        return HttpResponse(formset.cleaned_data)
    formset = StudentFormset(initial = [{'student_name': 'Ep'}])
    return render(request, "create_student.html", {"formset": formset})

        

''''
class StudentView (View):
    form_class = StudentForm
    initial = {"key": "value"}
    template_name = "create_student.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            student_name = form.cleaned_data['student_name']
            return HttpResponse(f"Student {student_name} was created" )

'''  

