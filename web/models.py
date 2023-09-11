from django.db import models

class Result_post(models.Model):

    text = models.TextField(max_length=5000, blank=True, null=True, verbose_name="공사내용")
    address = models.CharField(max_length=200, verbose_name="공사주소")
    business_name = models.CharField(max_length=200, verbose_name="공사이름")
    business_start_at = models.DateField(null=True, blank=True, verbose_name="공사시작일")
    business_finish_at = models.DateField(null=True, blank=True, verbose_name="공사마감일")
    file_1 = models.FileField(upload_to='files/%Y%m%d', null=True, blank=True, verbose_name="파일")
    file_2 = models.FileField(upload_to='files/%Y%m%d', null=True, blank=True, verbose_name="파일")
    file_3 = models.FileField(upload_to='files/%Y%m%d', null=True, blank=True, verbose_name="파일")
    file_4 = models.FileField(upload_to='files/%Y%m%d', null=True, blank=True, verbose_name="파일")
    file_5 = models.FileField(upload_to='files/%Y%m%d', null=True, blank=True, verbose_name="파일")

    def __str__(self):
        return self.address

    class Meta:
        db_table = 'result_posts'
        verbose_name = '공사실적'
        verbose_name_plural = '공사실적'

class Notice_post(models.Model):

    title = models.CharField(max_length=50, verbose_name="제목")
    text = models.TextField(max_length=10000, blank=True, null=True, verbose_name="내용")
    create_at = models.DateField(auto_now_add=True, verbose_name="날짜")
    clicks = models.IntegerField(default=1, verbose_name="조회수")
    file_1 = models.FileField(upload_to='files/%Y%m%d', null=True, blank=True, verbose_name="파일")
    file_2 = models.FileField(upload_to='files/%Y%m%d', null=True, blank=True, verbose_name="파일")
    file_3 = models.FileField(upload_to='files/%Y%m%d', null=True, blank=True, verbose_name="파일")
    file_4 = models.FileField(upload_to='files/%Y%m%d', null=True, blank=True, verbose_name="파일")
    file_5 = models.FileField(upload_to='files/%Y%m%d', null=True, blank=True, verbose_name="파일")


    @property
    def update_clicks(self):
        self.clicks += 1
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'notice_posts'
        verbose_name = '공지사항'
        verbose_name_plural = '공지사항'

class Information_post(models.Model):

    password = models.CharField(max_length=50, verbose_name="비밀번호")
    author = models.CharField(max_length=50, verbose_name="작성자")
    title = models.CharField(max_length=500, verbose_name="제목")
    text = models.TextField(max_length=10000, verbose_name="내용")
    phone_number = models.CharField(max_length=20, verbose_name="전화번호")
    create_at = models.DateField(auto_now_add=True, verbose_name="날짜")
    clicks = models.IntegerField(default=1, verbose_name="조회수")

    @property
    def update_clicks(self):
        self.clicks += 1
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'information_posts'
        verbose_name = '문의글'
        verbose_name_plural = '문의글'
