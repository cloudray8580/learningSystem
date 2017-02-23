from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    # mytemplate = loader.get_template('myserver/testMarkdown.html')
    # return HttpResponse(mytemplate)
    # why the above do not work??????
    return render(request, 'myserver/testMarkdown.html',None)

import json
from myserver.models import Question
def getMarkdownText(request):
    response_data = {}
    # response_data['test'] = "# Marked in browser\n\nRendered by **marked**. $$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$"
    response_data['test'] = Question.objects.get(id=1).question_text
    print(response_data['test'])
    return HttpResponse(json.dumps(response_data), content_type="application/jason")
   # return "# Marked in browser\n\nRendered by **marked**. $$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$"
