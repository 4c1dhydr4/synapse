from django.contrib.auth.forms import AuthenticationForm

class SigninForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super(SigninForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder':'Email'})
		self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder':'Password', 'type':'password'})