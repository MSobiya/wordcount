from django.http import HttpResponse
from django.shortcuts import render
import operator

#In homepage and contact_us method we write html code directly therefore we are using HttpResponse.
def homepage(request):
	#It will be shown on website
	#We can't directory return anything. It will be return in the form of HttpResponse.
	#HttpResponse contains html code not only a simple string.
	return HttpResponse("<h1>Hello! This is Homepage.</h1><form action='wordcount'><input type='submit' value='WordCountPage'></form>")

def contact_us(request):
	return HttpResponse("<h1>Contact Page</h1><br>This is our contact page.")


#To call html file we are using render
#Through this we can also pass python code, here we are passing dictionary

#without python code
#def home(request):
	#return render(request, 'home.html')

#With python code
def home(request):
	return render(request, 'home.html',{'name' :  "Sobiya"})

#Above all methods are for understanding purpose have no use for this wordcout app.

#wordcount method to count words.
def word_count(request):
	return render(request, 'wordcount.html')

def count(request):
	#accepting the data of written in textarea from wordcount.html page.
	data = request.GET['wordstextarea']
	#print(data)
	#data contains complete text typed by user. Now to count total number of words we split this string by space and get a list, then get the length of list using len()
	words = data.split(' ')

	#create dictionary for counting number of words
	word_dict = {}
	for i in words:
		if i in word_dict:
			#increase value by 1
			word_dict[i] += 1
		else:
			#create new dict element
			word_dict[i] = 1

	#sort dictionary based on values

	sorted_list = sorted(word_dict.items(), key=operator.itemgetter(1),reverse = True)

	return render(request, 'count.html', {'complete_text' : data, 'no_of_words' : len(words), 'word_dict' : sorted_list})



def about_us(request):
	return render(request, 'about.html')