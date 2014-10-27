from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    price = models.FloatField()

    def __unicode__(self):
        return self.name

    @classmethod
    def all(cls):
        return Product.objects.all()


class OrderItem(models.Model):
    count = models.IntegerField()
    product = models.ForeignKey(Product, default=None)

    def __unicode__(self):
        return u'%s items of %s' % (self.count, self.product.name)


class Order(models.Model):
    name = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal = models.CharField(max_length=7)
    country = models.CharField(max_length=100)
    giftwrap = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)

    def __unicode__(self):
        return self.name