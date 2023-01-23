from django.shortcuts import render

from .models import Region


def get_regions(request):
    print("_______________________")
    regions = Region.nodes.all()
    print(regions)
    return render(request, 'main_regions.html', {'regions': regions})
