from django.db import models
from user.models import User
# from django.db.models import ForeignKey


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # user_id (int)
    # user 정보가 사라질 때 같이 삭제 - on_delete=models.CASCADE
    # user 정보가 사라져도 글은 남길 때 - on_delete=models.SET_NULL, null=True
    title = models.CharField(max_length=100)
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)
    img_url = models.URLField(null=True)

    class Meta:
        db_table="post"
        # 만약 테이블 이름을 지정하지 않으면 - app_model (ex: board_post)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # post_id (1)
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="comment"