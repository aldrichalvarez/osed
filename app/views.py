from django.shortcuts import render
from django.http import HttpResponse

 
posts = [
   {
      'video': 'https://www.youtube.com/embed/5GqgZOaDI0k',
      'author': 'Sean Darrel Hernandez',
      'class': 'Photoshop Master Class',
      'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ',
      'likes': '1000',
      'ranking': '1'
   },
   {
      'video': 'https://www.youtube.com/embed/5GqgZOaDI0k',
      'author': 'Aldrich Heinz Alvarez',
      'class': 'Full Stack Web Dev using Django',
      'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. ',
      'likes': '1000',
      'ranking': '2'
   },
]

def home(request):
   context = {
      'posts': posts
   }
   return render(request, 'app/home.html', context)

def about(request):
   return render(request, 'app/about.html')