import registration.views


class Registration(registration.views.RegistrationView):
    success_url = '/ok'
    template_name = 'registration.html'

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(registration.views.RegistrationView, self).form_valid(form)
