from django import forms

class CipherForm(forms.Form):
	decipher_text = forms.CharField(label='decipher_text')
	cipher_text = forms.CharField(label='cipher_text')
	btn_click = forms.CharField(label='btn_click')
	btn_clear = forms.CharField(label='btn_clear')