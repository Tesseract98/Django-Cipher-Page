from django.shortcuts import render
from cryptography.fernet import Fernet
from django.http import HttpResponse
# from .forms import CipherForm

# Create your views here.

def main(request):
	if request.method == "GET":
		return render(request, "cipher/cipher_page.html")
	elif request.method == "POST":
		str_cipher_text = ''
		str_decipher_text = ''
		# key = Fernet.generate_key()
		key = b'KELWlrXv4ruCxp-Lt8FUZXLdn5wRNE8wOqWBLo7w0vI='
		cipher_suite = Fernet(key)
		# form = CipherForm(request.POST)
		int_click, int_clear = 0, 0
		# if form.is_valid():
		str_decipher_text = request.POST.get('decipher_text')
		str_cipher_text = request.POST.get('cipher_text')
		if request.POST.get('btn_click'):
			int_click = int(request.POST.get('btn_click'))
		if request.POST.get('btn_clear'):
			int_clear = int(request.POST.get('btn_clear'))
		if int_click == 1:
		    str_cipher_text = cipher_suite.encrypt(bytes(str_decipher_text, 'UTF-8')).decode('UTF-8')
		    context = {'cipher_text': str_cipher_text, 'decipher_text': str_decipher_text}
		    return render(request, "cipher/cipher_page.html", context)
		elif int_click == 2:
		    str_decipher_text = cipher_suite.decrypt(bytes(str_cipher_text, 'UTF-8')).decode('UTF-8')
		    context = {'cipher_text': str_cipher_text, 'decipher_text': str_decipher_text}
		    return render(request, "cipher/cipher_page.html", context)
		elif int_clear == 1:
			context = {'cipher_text': str_cipher_text, 'decipher_text': ""}
			return render(request, "cipher/cipher_page.html", context)
		elif int_clear == 2:
			context = {'cipher_text': "", 'decipher_text': str_decipher_text}
			return render(request, "cipher/cipher_page.html", context)
		return HttpResponse(404)	
