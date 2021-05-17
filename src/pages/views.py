from django.shortcuts import render
from django.http	import	HttpResponse
# Create your views here.



def home_view(requset, *args , **kwargs):
	print(args, kwargs)
	print(requset.user)

	return	render(requset, "home.html" , {})
	

# Create your views here.
def contact_view(requset , *args , **kwargs):
	return	render(requset, "contact.html" , {})


def about_view(requset , *args , **kwargs):
	my_context={
		"title" : "this is about me",
		"my_number" : 123 ,
		"my_list" : [ 123, 456 , 789 , "abc" ]
	}
	return	render(requset, "about.html" , my_context)


def social(requset , *args , **kwargs):
	return	render(requset, "social.html" , {})
