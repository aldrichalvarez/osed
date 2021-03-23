from django.shortcuts import render
from django.http import HttpResponse

posts = [
   {
      'image': 'https://wallpaperaccess.com/full/3389575.jpg',
      'author': 'Sean Darrel Hernandez',
      'class': 'Photoshop Master Class',
      'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
      'likes': '1000',
      'ranking': '1'
   },
   {
      'image': 'https://wallpaperaccess.com/full/3389575.jpg',
      'author': 'Aldrich Heinz Alvarez',
      'class': 'Full Stack Web Dev using Django',
      'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
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