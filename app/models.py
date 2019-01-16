from django.db import models

# Create your models here.

from django.utils import timezone


# 用户表
class User(models.Model):
    icon = models.ImageField(upload_to='headimages')
    username = models.CharField(verbose_name='用户名', max_length=32)
    password = models.CharField(verbose_name='密码', max_length=32)
    phone = models.CharField(verbose_name='手机号', max_length=32)
    profession = models.CharField(verbose_name='职业', max_length=64)
    native_place = models.CharField(verbose_name='籍贯', max_length=256)
    email = models.CharField(verbose_name='邮箱', max_length=128)
    ip = models.CharField(verbose_name='登录地址',max_length=32)
    date = models.DateTimeField(verbose_name='登录时间',auto_now=True)
    login_nums = models.IntegerField(verbose_name='登录次数',default=0)

    token = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = '用户管理'
        db_table = 'b_user'

    def __str__(self):
        return self.username


# 文章分类
class Category(models.Model):
    c_name = models.CharField(verbose_name='名称', max_length=32)

    class Meta:
        verbose_name_plural = '文章类别'
        db_table = 'b_category'

    def __str__(self):
        return self.c_name


# 标签
class Tag(models.Model):
    tag_name = models.CharField(verbose_name='文章标签', max_length=20)

    class Meta:
        verbose_name_plural = '文章标签'
        db_table = 'b_tag'

    def __str__(self):
        return self.tag_name


# 博客表
class Blog(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    content = models.TextField(verbose_name='正文', default='')
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    modify_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    tag = models.ManyToManyField(Tag, verbose_name='文章标签')
    category = models.ForeignKey(Category, verbose_name='个人分类')
    click_nums = models.IntegerField(verbose_name='点击量', default=0)
    like_nums = models.ImageField(verbose_name='点赞数', default=0)
    u_b = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = '我的博客'
        db_table = 'b_blog'

    def __str__(self):
        return self.title


# 评论
class Comment(models.Model):
    content = models.CharField(verbose_name='内容', max_length=300)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    comment_nums = models.IntegerField(verbose_name='评论数', default=0)
    u_comm_id = models.ForeignKey(User, verbose_name='用户名')
    b_comm_id = models.ForeignKey(Blog, verbose_name='评论的博客')

    class Meta:
        verbose_name_plural = '博客评论'
        db_table = 'b_comment'

    def __str__(self):
        return self.content[:10]

# 统计表
# class Counts(models.Model):
#     blog_nums = models.ForeignKey(Blog)
#     category_nums = models.ForeignKey(Category)
#     tag_nums = models.ForeignKey(Tag)
#
#     class Meta:
#         verbose_name_plural = '统计'
#         db_table = 'b_counts'
#
#     def __str__(self):
#         return self.blog_nums,self.category_nums,self.tag_nums
