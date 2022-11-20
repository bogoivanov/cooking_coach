from django.shortcuts import render
from cooking_coach.auth_app.forms import SignUpForm
from django.contrib.auth import views as auth_views, login
from django.urls import reverse_lazy
from django.contrib.auth import mixins as auth_mixins, get_user_model
from django.views import generic as views

UserModel = get_user_model()


# Create your views here.
class UsersListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = UserModel
    template_name = 'index.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #
    #     # context['has_email'] = AppUser.has_email(self.request.user)
    #     print(self.request.user.__class__)
    #     return context


class SignUpView(views.CreateView):
    template_name = 'sign-up.html'
    form_class = SignUpForm

    success_url = reverse_lazy('index')

    # Signs the user in, after successful sign up
    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class SignInView(auth_views.LoginView):
    template_name = 'sign-in.html'
    success_url = reverse_lazy('index')


class SignOutView(auth_views.LogoutView):
    template_name = 'sign-out.html'


#
# class SignInForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField()
#
#
# def sign_in(request):
#     if request.method == 'GET':
#         form = SignInForm()
#     else:
#         form = SignInForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             # user = authenticate(request, username=username, password=password)
#             user = authenticate(request, **form.cleaned_data)
#
#             if user:
#                 login(request, user)
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'auth/sign-in.html', context)


'''
%M0nkiV123
'''

'''
pre_clean
clean
post_clean
'''
