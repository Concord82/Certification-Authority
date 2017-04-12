# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.forms import widgets
# Create your models here.

class Cert_Parameters(models.Model):
    SSL_CA = (
        ('CA:TRUE','Шаблон сертификата УЦ'),
        ('CA:FALSE','Шаблон другого типа')
    )
    NS_CERT_TYPE = (
        ('client', 'Сертифкат пользователя'),
        ('email', 'Защита элктронной почты'),
        ('server', 'Сертификат сервера')
    )

    KEY_USAGE = (
        ('digitalSignature', 'Цифровая подпись'),
        ('nonRepudiation', 'Не отрицаемость'),
        ('keyEncipherment', 'Шифрование ключа'),
        ('dataEncipherment', 'Шифрование данных'),
        ('keyAgreement', 'Согласование ключей'),
        ('keyCertSign', 'Проверка подписей'),
        ('cRLSign', 'Публикация списка отзыва'),
        ('encipherOnly','Шифрование согласования ключей'),
        ('decipherOnly','Расшифровка согласования ключей')
    )

    EXTENDET_KEY_USAGE = (
        ('serverAuth','SSL/TLS Идентификация веб-сервера'),
        ('clientAuth','SSL/TLS Аутентификация веб-клиента'),
        ('CodeSigning', 'Подписание кода'),
        ('emailProtection','Защита электронной почты по электронной почте (S/MIME)'),
        ('timeStamping','Штамп доверенного времени'),
        ('msCodeInd','Microsoft Individual Code Signing (authenticode)'),
        ('msCodeCom','Microsoft Commercial Code Signing (authenticode)'),
        ('msCTLSign','Microsoft Trust List Signing'),
        ('msSGC','Microsoft Server Gated Crypto'),
        ('msEFS','Microsoft Encrypted File System'),
        ('nsSGC','Netscape Server Gated Crypto')
    )

    title = models.CharField(
        verbose_name='Имя сертификата',
        max_length=64)
    mash_name = models.CharField(
        verbose_name='Машино понятное имя ',
        max_length=64)
    ca_type = models.CharField(
        verbose_name='Сертификат УЦ',
        choices=SSL_CA,
        default='CA:FALSE',
        max_length=10)
    nsCertType = models.CharField(
        verbose_name='тип сертификата',
        choices=NS_CERT_TYPE,
        max_length=255,
        default='server' )
    keyUsage = models.CharField(
        verbose_name='Использование ключа',
        choices=KEY_USAGE,
        max_length=255,
        default='digitalSignature')
    extendedKeyUsage = models.CharField(
        verbose_name='Расширенное использование ключа',
        choices=EXTENDET_KEY_USAGE,
        max_length=255,
        default='serverAuth'
    )



