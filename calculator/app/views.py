from django.shortcuts import render
from django.views import View

class HomeView(View):

    template = 'app/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template)


class CalculatorView(View):

    template = 'app/calculator.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template)

    def post(self, request, *args, **kwargs):
        expression = request.POST.get('expression')

        try:
            result = eval(expression, {"__builtins__": None}, {})
        except:
            result = 'invalid input'

        data = {'result': result}

        return render(request, self.template, context=data)