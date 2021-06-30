from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CreateBioForm
from users.models import Profile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def privacy(request):
   return render(request, 'users/privacy.html')

def register(request):
   if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
         form.save()
         username = form.cleaned_data.get('username')
         messages.success(request, f'Your account has been created {username}! You are now able to login')
         return redirect('login')
   else:
      form = UserRegisterForm()
   return render(request, 'users/register.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class profile(DetailView):
   model = Profile
   template_name = 'users/profile.html'

   def get_context_data(self, *args, **kwargs):
      users = Profile.objects.all()
      context = super(profile, self).get_context_data(*args, **kwargs)
      page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
      context["page_user"] = page_user
      return context
      
@login_required
def update(request):
   if request.method == 'POST':
      u_form = UserUpdateForm(request.POST, instance=request.user)
      b_form = CreateBioForm(request.POST, instance=request.user.profile)
      p_form = ProfileUpdateForm(request.POST, 
                                 request.FILES, 
                                 instance=request.user.profile)
      if u_form.is_valid() and b_form.is_valid() and p_form.is_valid():
         u_form.save()
         b_form.save()
         p_form.save()
         return redirect('profile')
         
   else:
      u_form = UserUpdateForm(instance=request.user)
      b_form = CreateBioForm(instance=request.user.profile)
      p_form = ProfileUpdateForm(instance=request.user.profile)
      
   context = {
      'u_form': u_form,
      'b_form': b_form,
      'p_form': p_form
   }
   return render(request, 'users/update.html', context)