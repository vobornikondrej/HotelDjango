from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Question

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):  
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
	response = "You're looking at results for a question %s"
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting for a question %s" % question_id)