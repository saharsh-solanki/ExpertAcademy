from django.db import models

# Create your models here.


class quize_category(models.Model):
    cat_name=models.CharField(max_length=50)
    def __str__(self):
        return self.cat_name

class quize(models.Model):
    quize_catagery=models.ManyToManyField(quize_category)
    quize_name = models.CharField(max_length=250)
    def __str__(self):
        return self.quize_name

class question(models.Model):
    quize_id=models.ForeignKey(quize,on_delete=models.CASCADE)
    question=models.CharField(max_length=250)
    explanation = models.CharField(max_length=500)
    def __str__(self):
        return self.question

class answer(models.Model):
    question_id=models.ForeignKey(question,on_delete=models.CASCADE)
    answer = models.CharField(max_length=250)
    correct_answer=models.BooleanField()
    def __str__(self):
        return self.answer


class user_answer(models.Model):
    user_email = models.CharField(max_length=250)
    quize_id = models.CharField(max_length=250)
    question_id=models.CharField(max_length=250)
    answer_id=models.CharField(max_length=250)
    def __str__(self):
        return self.user_email


class user_start_quize(models.Model):
    quize_id=models.CharField(max_length=250,null=True)
    user_email=models.CharField(max_length=250)
    status= models.CharField(max_length=250)

    def __str__(self):
        return self.user_email