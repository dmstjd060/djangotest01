from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Choice, Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        #설문투표 폼을 다시 보여준다.
        return render(request, 'polls/detail.html', {
            'question':p,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #POST 데이터를 정상적으로 처리하였으면, 항상 HttpResoinseRedirect를 반환하여 리다이렉션 처리함
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})


############################################################################


def get_name(request):
    #POST 방식이면, 데이터가 담긴 제출된 폼으로 간주합니다.
    if request.method == 'POST':
        #request에 담긴 데이터로, 클래스 폼을 생성합니다.
        form = NameForm(request.POST)
        #폼에 담긴 데이터가 유효한지 체크합니다.
        if form.is_valid():
            #폼 데이터가 유효하면, 데이터는 cleaned_data로 복사됩니다.
            new_name = form.cleaned_data['name']
            #로직에 따라 추가적인 처리를 합니다.

            #새로운 URL로 리다이렉션 시킵니다.
            return HttpResponseRedirect('/thanks/')

        #POST 방식이 아니면 (보통은 GET 요청임), 빈 폼을 사용자에게 보여줍니다.
    else:
        form = NameForm()

    return render(request, 'name.html', {'form':form})
