from django.db import models

# Create your models here.

class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    members = models.ManyToManyField(Member, related_name='projects')

    def __str__(self):
        return self.title


class BorrowedItem(models.Model):
    item_name = models.CharField(max_length=100)
    borrower = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='borrowed_items')
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.item_name} borrowed by {self.borrower}"
