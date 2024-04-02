from users.forms import LoginForm, RegisterForm


def MyContextProcessor(object):
    form = LoginForm()
    forms = RegisterForm
    return {'forms': forms, 'form': form}
