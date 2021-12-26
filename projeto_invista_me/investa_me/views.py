from django.shortcuts import render # renderizar uma página HTML
from django.shortcuts import HttpResponse

def pagina_inicial (request):
    return HttpResponse('Pronto para investir')

def contato (request):
    return HttpResponse('Para dúvidas, enviar email para contanto')

def minha_historia (request):
    pessoa = {
        'nome' : 'Jeff',
        'idade' : 28,
        'hobby' : 'Games'
    }
    return render(request, 'investimentos/minha_historia.html', pessoa)

def novo_investimento (request):
    return render(request, 'investimentos/novo_investimento.html')

def investimento_registrado (request):
    investimento = {
        'tipo_investimento' : request.POST.get('TipoInvestimento')

    }
    return render (request,'investimentos/investimento_registrado.html', investimento )

