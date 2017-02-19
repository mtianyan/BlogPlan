from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def showBlog(request,blogId):
	
	# blog = models.Blog.objects.get(id=blogId)
	# return render(request,'blog/blog.html',{'blog':blog})
	return HttpResponse("hi,blog")
def showBlogList(request):
	# t = loader.get_template('blog_list.html')
	# blogs = Blog.object.all()
	# context ={'blogs':blogs}
	# html = t.render(context)
	return HttpResponse("hi,list")

