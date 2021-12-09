from django.shortcuts import render
from .models import Word
import random
from django.http import HttpResponse

def index(request):
  return render(request, "sample_site_app/index.html")

def result(request):
  print('ボタン押された。')
  if request.method == 'POST':  # POSTの処理
    # データベースからランダムでカテゴリと単語を取得する。
    all_word = Word.objects.all()
    # ランダムでカテゴリを選ぶ。
    radom_word = random.choice(all_word)
    print('ランダムワード')
    print(radom_word)
      
    return HttpResponse(radom_word)
