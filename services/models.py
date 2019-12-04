from django.db.models import Model, CharField, IntegerField, \
    DateTimeField, ForeignKey, CASCADE


class ServiceGroup(Model):
    name = CharField(verbose_name='Название', max_length=50)

    class Meta:
        verbose_name = 'Группа услуг'
        verbose_name_plural = 'Группы услуг'

    def __str__(self):
        return self.name


class Service(Model):
    group = ForeignKey(ServiceGroup, verbose_name='Группа услуг',
                       related_name='services', on_delete=CASCADE)
    name = CharField(verbose_name='Название', max_length=50)
    duration = IntegerField(verbose_name='Длительность')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class Saloon(Model):
    name = CharField(verbose_name='Название', max_length=100)
    address = CharField(verbose_name='Адрес', max_length=100)
    phone = CharField(verbose_name='Телефон', max_length=30)

    class Meta:
        verbose_name = 'Салон'
        verbose_name_plural = 'Салоны'

    def __str__(self):
        return self.name


class Price(Model):
    saloon = ForeignKey(Saloon, verbose_name='Салон', on_delete=CASCADE)
    service = ForeignKey(Service, verbose_name='Услуга', on_delete=CASCADE)
    price = IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return f'{self.saloon.name} {self.service.name} {self.price}'


class Appointment(Model):
    name = CharField(verbose_name='Имя', max_length=100)
    phone = CharField(verbose_name='Телефон', max_length=100)
    service = ForeignKey(Service, verbose_name='Услуга', on_delete=CASCADE)
    datetime = DateTimeField(verbose_name='Дата и время')
    saloon = ForeignKey(Saloon, verbose_name='Салон', on_delete=CASCADE)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return f'{self.name} {self.service} {self.saloon} {self.datetime}'
