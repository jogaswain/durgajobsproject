from django.shortcuts import render

# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')
def movie_news_view(request):
    news1 = 'in telugu devdas movie is not good'
    news2 = 'salman is demanding 100 crores to sign a movie'
    news3 = 'sonali is getting cure slowly'
    news4 = 'amitabh is back again, signing a movie suryabanshi'
    news5 = 'salman is going to marry to kangna soon'
    my_dict = {'news1':news1,'news2':news2,'news3':news3,'news4':news4,'news5':news5}
    return render(request,'testapp/mnews.html',my_dict)
