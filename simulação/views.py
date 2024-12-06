from django.shortcuts import render
from django.http import JsonResponse
import subprocess

def home(request):
    return render(request, 'simulação/index.html')

def start_simulation(request):
    # Executa o script do Pygame
    subprocess.Popen(['python', 'simulation.py'])
    return JsonResponse({'message': 'Simulação iniciada!'})
