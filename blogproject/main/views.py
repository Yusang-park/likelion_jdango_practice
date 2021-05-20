from django.shortcuts import render, redirect, get_object_or_404
from .models import Write, Comment
from .forms import WriteForm, CommentForm
from django.contrib.auth.models import User #유저 모델 import

# Create your views here.
def index(request):
    #서버의 write 클래스 정보를 모두 가져온다.
    all_write = Write.objects.all()
    return render(request, 'index.html', {'all_write': all_write})

def create(request):
    # 보안 요청이라면
    if request.method == 'POST': 
        # 받은 post를 담는다
        create_form = WriteForm(request.POST)
        # 유효하면
        if create_form.is_valid():
            # 저장한다
            create_form.save()
            #index로 이동, redirect는 ''의 요청을 보낸다.
            #render는 새로고침해서 그린다.
            return redirect('main:index')
    else:
        #빈 요청이라면
        create_form = WriteForm()
        # create로 이동, object로 보내왔음.
    return render(request, 'create.html', {'create_form':create_form})


def detail(request, write_id):
    user = request.user
    comment_form = CommentForm()
    comments = Comment.objects.filter(post=write_id)
    my_write = get_object_or_404(Write, id=write_id)
    return render(request, 'detail.html', {'my_write':my_write, 'comment_form': comment_form, 'comments' : comments, 'user':user})

def update(request, write_id):
    my_write = get_object_or_404(Write, id=write_id)
    if request.method == "POST":
        update_form = WriteForm(request.POST, instance=my_write)
        # 각 하나를 들고오기 위함
        if update_form.is_valid():
            update_form.save()
            return redirect('main:index')
    else:
        update_form = WriteForm(instance=my_write)
        
    return render(request, 'update.html', {'update_form' : update_form})




def delete(request, write_id):
    my_write = get_object_or_404(Write, id=write_id)
    my_write.delete()
    return redirect('main:index')



def create_comment(request, write_id):
    if request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid:
            form = comment.save(commit=False) #제출은 보류
            user = request.user
            form.user = User.objects.get(id = user.id)
            form.post = Write.objects.get(id = write_id)
            form.save()
    return redirect('main:detail', write_id)


def delete_comment(request, write_id, comment_id):
    my_comment = get_object_or_404(Comment, id=comment_id)
    my_comment.delete()
    return redirect('main:detail', write_id)
