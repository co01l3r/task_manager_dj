from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Task


class TasksLoginView(LoginView):
    """
    class inherits functionality from LoginView. When successfully logged in always
    prevent authenticated user from login. When submitted and logged in redirect user
    to the home page using reverse_lazy()

    atr
    ---
    template_name = override default template name
    fields = specify what fields from model we want to use for creating a form
    redirect_authenticated_user = bool, changed default value to be true, always prevent auth user be there
    success_url = redirect to when success

    """
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')


class TasksRegister(FormView):
    """
    class inherits functionality from FormView and generate built-in form. When submitted uses
    UserCreationForm to create user and redirect user to the login page using reverse_lazy()
    when success.

    atr
    ---
    template_name = override default template name
    form_class = specify form to create user
    success_url = redirect to when success
    """
    template_name = 'base/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        """
        before make post request, make sure user is successfully created, then continue
        """
        user = form.save()
        if user is not None:
            return super(TasksRegister, self).form_valid(form)


class TaskList(LoginRequiredMixin, ListView):
    """
    class inherits functionality from ListView, returns template with set of data from model.
    Using Mixin to restricts unauthenticated users from this page, redirect this user to
    page, that is specified in settings.py of the project, in this case to login view page.

    atr
    ---
    model = model
    context_object_name = override default value for readability
    """
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        """
        returns all passed data. Filter those data here, before it happens, to prevent users see
        other user's data.

        atr
        ---
        context = original context value
        """
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    """
    class inherits functionality from DetailView, returns template with information
    about item from model. Using Mixin to restricts unauthenticated users from this
    page, redirect unauthenticated user to LOGIN_URL, that is specified in settings.py
    of the project.

    atr
    ---
    model = model
    context_object_name = override default value for readability
    template_name = override default template name
    """
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    """
    class inherits functionality from CreateView. Uses model to create fields for form.
    When submitted send post request and creating item in model/db following with redirect
    user to the home page using reverse_lazy(). Using Mixin to restricts unauthenticated
    users from this page, redirect this user to LOGIN_URL, that is specified in settings.py in
    the project.

    atr
    ---
    model = model
    fields = specify what fields from model we want to use for creating a form
    success_url = redirect to when success
    """
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        """
        before making post request, this make sure user is logged in, then continue
        as expected.
        """
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    """
    class inherits functionality from UpdateView, takes item from model, create and
    prefill form based of these data. When submitted modify the model data and redirect
    user to the home page using reverse_lazy(). Using Mixin to restricts unauthenticated
    users from this page, redirect this user to LOGIN_URL, that is specified in settings.py of
    the project.

    atr
    ---
    model = model
    fields = specify fields from model we want to modify
    success_url = redirect to when success
    """
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    """
    class inherits functionality from DeleteView, renders (prefix)task_confirm_delete
    template and ask user if wants to delete the item. When submitted sending post
    request and delete the item with redirecting user to the home page using reverse_lazy().
    Using Mixin to restricts unauthenticated users from this page, redirect this user to
    LOGIN_URL, that is specified in settings.py of the project.

    atr
    ---
    model = model
    context_object_name = override default value for readability
    success_url = redirect to when success
    """
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
