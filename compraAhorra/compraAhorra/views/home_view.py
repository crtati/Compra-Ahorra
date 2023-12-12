from django.shortcuts import render
import requests

def carrito(request):

    television = { 'image' : 'img/product/television1.jpg',
                'product': 'Televisor Caixun',
                'description': '32 PULGADAS',
                'price' : 200000,
                'quantity': 1
                }
    audifono = {'image' : 'img/product/xbox.jpg',
                'product': 'Xbox Series',
                'description': 'XBOX COLOR BLANCO',    
                'price' : 490000,
                'quantity': 1
                }
    laptop = {'image' : 'img/product/laptop1.jpg',
                'product': 'Notebook Gamer',
                'description': 'LEVONO COLOR NEGRO',    
                'price' : 400000,
                'quantity': 1
                } 

    products = [television, audifono, laptop]
    total = television.get('price') + audifono.get('price') + laptop.get('price')

    return render(request, 'home.html', {'products' : products, 'total': total})  