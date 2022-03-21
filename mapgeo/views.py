from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
import folium
from io import BytesIO
from .forms import latlog

def mapview(request):
    if request.method == 'POST':
        fm = latlog(request.POST)
        if fm.is_valid():
            lat = fm.cleaned_data['lat']
            log = fm.cleaned_data['log']

            m = folium.Map([lat, log], zoom_start=10)
            test = folium.Html('<b>Map</b>', script=True)
            popup = folium.Popup(test, max_width=5000)
            folium.RegularPolygonMarker(location=[lat, log], popup=popup).add_to(m)
            m=m._repr_html_() #updated
            context = {'my_map': m,'form':latlog()}
            context["lat"] = lat
            context['log'] = log

    else:
        m = folium.Map([22.9987, 72.58926], zoom_start=10)
        test = folium.Html('<b>Map</b>', script=True)
        popup = folium.Popup(test, max_width=5000)
        folium.RegularPolygonMarker(location=[22.9987, 72.58926], popup=popup).add_to(m)
        m=m._repr_html_() #updated
        fm = latlog()
        context = {'my_map': m,'form':fm}
        context["lat"] = 22.9987
        context['log'] = 72.58926
        
    return render(request,'mapgeo/home.html',context)



def download(request):
    lat = request.GET["lat"]
    log = request.GET["log"]

    m = folium.Map([lat, log], zoom_start=10)
    img_data = m._to_png()
    response = HttpResponse(BytesIO(img_data).read(), content_type='jpg/png');
    response['Content-Disposition'] = 'attachment; filename="%s"' % 'test.png'
    return response