from django.db import models

# Create your models here.

from django.utils import timezone

# 文章分类
class Category(models.Model):
    c_name = models.CharField(verbose_name='名称',max_length=32)
    nums = models.IntegerField(verbose_name='分类数',default=0)

    class Meta:
        verbose_name_plural = '文章类别'
        db_table = 'category'

    def __str__(self):
        return self.c_name

# 标签
class Tag(models.Model):
    tag_name = models.CharField(verbose_name='文章标签',max_length=20)
    nums = models.IntegerField(verbose_name='标签数目',default=0)

    class Meta:
        verbose_name_plural = '文章标签'
        db_table = 'tag'

    def __str__(self):
        return self.tag_name

# 博客表
class Blog(models.Model):
    title = models.CharField(verbose_name='标题',max_length=100)
    content = models.TextField(verbose_name='正文',default='')
    create_time = models.DateTimeField(verbose_name='创建时间',default=timezone.now)
    modify_time = models.DateTimeField(verbose_name='修改时间',auto_now=True)
    click_nums = models.IntegerField(verbose_name='点击量',default=0)
    category = models.ManyToManyField(Category,verbose_name='文章分类')
    tag = models.ManyToManyField(Tag,verbose_name='标签')

    class Meta:
        verbose_name_plural = '我的博客'
        db_table = 'blog'

    def __str__(self):
        return self.title

# 用户表
class User(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=32)
    phone = models.IntegerField(verbose_name='手机号')
    blog = models.ForeignKey(Blog,verbose_name='博客')
    class Meta:
        verbose_name_plural = '用户管理'
        db_table = 'user'
    def __str__(self):
        return self.username

# 评论
class Comment(models.Model):
    content = models.CharField(verbose_name='内容',max_length=300)
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    user = models.ForeignKey(User,verbose_name='用户名')

    post = models.ForeignKey(Blog)

    class Meta:
        verbose_name_plural = '博客评论'
        db_table = 'comment'

    def __str__(self):
        return self.content[:10]

# 统计表
class Counts(models.Model):
    blog_nums = models.ForeignKey(Blog)
    category_nums = models.ForeignKey(Category)
    tag_nums = models.ForeignKey(Tag)

    class Meta:
        verbose_name_plural = '统计'
        db_table = 'counts'

    def __str__(self):
        return self.blog_nums,self.category_nums,self.tag_nums
