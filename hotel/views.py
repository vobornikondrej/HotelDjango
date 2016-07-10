from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Hotels

def index(request):
	template = loader.get_template('hotels/index.html')
	hotels_list = Hotels.objects.all()
	
	context = {
		'hotels_list': hotels_list,
	}
	
	return render(request, 'hotels/index.html', context)
	template = loader.get_template('hotels/index.html')
