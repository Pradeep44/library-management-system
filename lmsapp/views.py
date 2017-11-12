from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import LmsPost
from .forms import LmsPostForm
# Create your views here.
def homepage(request):
	blogs = LmsPost.objects.all()
	context ={'blogs':blogs}
	template_name='home.html'
	return render(request,template_name,context)
def detail_page(request):
	blogs =  LmsPost.objects.all()
	context ={'blogs':blogs}
	template_name='detail.html'
	return render(request,template_name,context)

def details(request, pk):
	blog = LmsPost.objects.get(pk=pk)
	template_name= 'detail.html'
	context = {'blog':blog}
	return render(request, template_name,context)
	
def newpost(request):
	if request.method =='POST':
		form = LmsPostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('details',pk=post.pk)
	else:
		form=LmsPostForm()
	return render(request,'newpost.html',{'form': form})	

