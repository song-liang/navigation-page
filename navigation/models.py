from django.db import models


class Category(models.Model):
    name = models.CharField("分类名称", max_length=50, unique=True)
    icon = models.ImageField("图标", upload_to='icons/', null=True, blank=True)
    weight = models.IntegerField("权重", default=0)  # 用于排序

    class Meta:
        ordering = ['-weight']  # 按权重倒序排列
        db_table = 'nav_category'  # 指定模型类对应表名
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Link(models.Model):
    category = models.ForeignKey(Category, verbose_name="分类", on_delete=models.CASCADE)
    title = models.CharField("网站名称", max_length=100)
    url = models.URLField("网址")
    description = models.TextField("描述", blank=True)
    weight = models.IntegerField("权重", default=0)
    icon = models.ImageField("图标", upload_to='icons/', null=True, blank=True)

    class Meta:
        ordering = ['-weight']  # 按权重倒序排列
        db_table = 'nav_link'  # 指定模型类对应表名
        verbose_name = '链接'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

