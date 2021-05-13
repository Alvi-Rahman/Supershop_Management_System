from django.shortcuts import render
from django.views import View


class HomePage(View):
    template_name = "supershop_app/index.html"

    def get(self, request):
        # paraphrase_class = ParaphraseTool()
        return render(request, self.template_name, context={'get': 1})

    def post(self, request):
        return render(request, self.template_name)
