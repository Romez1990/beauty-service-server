from django.db.models import Model, CharField, IntegerField, ForeignKey, CASCADE


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
