from django.db import models


class Country(models.Model):
    code = models.CharField(
        max_length=4,
    )
    name = models.CharField(
        max_length=16
    )

    def __str__(self):
        return '({}) {}'.format(
            self.code,
            self.name
        )


class DocumentType(models.Model):
    code = models.CharField(
        max_length=8,
    )
    name = models.CharField(
        max_length=64
    )

    def __str__(self):
        return '({}) {}'.format(
            self.code,
            self.name
        )


class Base(models.Model):
    name = models.CharField(
        max_length=64,
    )
    last_name = models.CharField(
        max_length=64,
        default=''
    )
    second_last_name = models.CharField(
        max_length=64,
        default=''
    )
    phone = models.CharField(
        max_length=16,
        default=''
    )
    email = models.CharField(
        max_length=64,
        default=''
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
    )
    document_type = models.ForeignKey(
        DocumentType,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    document_number = models.CharField(
        max_length=16,
        default=''
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True


class Partner(Base):

    def __str__(self):
        return self.name


class Student(Base):
    code = models.CharField(
        max_length=16,
    )
    partners = models.ManyToManyField(
        Partner,
        related_name='students'
    )

    def __str__(self):
        return self.name
