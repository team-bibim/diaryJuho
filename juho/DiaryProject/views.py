from django.shortcuts import render,get_object_or_404, redirect
from .models import Diary
from .forms import DiaryForm

# Create your views here.

#일기 리스트 나열
#등록한 시간 순서의 역순으로 나열
def diary_list(request):
    diaries = Diary.objects.order_by('-time_create')
    return render(request, 'diary/diary_list.html')

#해당 일기의 세부사항
#primary key를 통해 번호를 가져와서 해당 번호의 일기의 세부 정보를 보여줌
def diary_detail(request, pk):
    diary = get_object_or_404(Diary, pk=pk)
    return render(request, 'diary/diary_detail.html')

#일기 추가
#요청이 post방식인지 확인하고, form.py를 참고하여 post방식이고 입력된 데이터가
#폼에 입력되기 적당한지 판단, 그 이후에 추가 후 redirect

def diary_new(request):
    if request.method == "POST":
        form = DiaryForm(request.POST)
        if form.is_vaild():
            diary = form.save(commit=False)
            diary.save()
            return redirect('diary_detail', pk=diary.pk)
    else:
        form = DiaryForm()
    return render(request, 'diary/diary_edit.html')

#render는 context 값을 원하는 html파일로 넘길 수 있음

#일기 수정
#마찬가지로 요청이 post방식인지 확인하고, form.py를 참고하여 post방식이고 입력된 데이터가
#폼에 입력되기 적당한지 판단, 이후 수정 진행

def diary_edit(request, pk):
    diary= get_object_or_404(Diary, pk=pk)
    if request.method == "POST":
        form = DiaryForm(request.POST, instance=diary)
        if form.is_valid():
            diary = form.save(commit=False)
            diary.save()
            return redirect('diary_detail', pk=diary.pk)
    else:
        form = DiaryForm(instance=diary)
    return render(request, 'diary/diary_edit.html')

#일기 삭제
#해당 일기 삭제 후 리스트 페이지로 돌아감
def diary_delete(request, pk):
    diary = get_object_or_404(Diary, pk=pk)
    diary.delete()
    return redirect('diary_list')