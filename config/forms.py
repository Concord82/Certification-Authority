#  coding=utf-8
from django.utils.translation import ugettext_lazy as _
from django import forms
from CertAuthority.settings import BASE_DIR
from constance import config
len_bits = (
    (1, '1024'),
    (2, '2048'),
    (4, '4096')
)

countrylist = (
    ('RU', 'Россия'),
    ('BY', 'Belarus'),
    ('UA', 'Ukraine'),
    ('GB', 'United Kingdom'),
    ('US', 'United States of America')
)

hashalg = (
    (1, 'sha256'),
    (2, 'sha384'),
    (3, 'sha512')
)

class CertParams(forms.Form):
    capath = forms.CharField(label=_(u'Directory Name'),max_length=255, initial=config.CA_PATH, help_text='Путь для файлов УЦ')
    year = forms.IntegerField(label=_(u'Validity'), min_value=5, max_value=50, initial=20)
    algoritm = forms.ChoiceField(label=_(u'Hash Algoritm'), choices=hashalg, initial=1)
    bits = forms.ChoiceField(label=_(u'Length Key'), choices=len_bits, initial=4)
    password = forms.CharField(label = _('Key password'), widget=forms.PasswordInput, min_length=6, max_length=32, help_text='Пароль ключа УЦ')
    password2 = forms.CharField(label=_('Again password'), widget=forms.PasswordInput, min_length=6, max_length=32,help_text='Подтверждение пароля')

    def clean_capath(self):
        from os.path import exists, isdir
        ca_dir = self.cleaned_data['capath']

        if not exists(ca_dir) or not isdir(ca_dir):
            raise forms.ValidationError('Указанный каталог не существует . Проверьте путь до каталога ')
        else:
            config.CA_PATH = ca_dir
        return ca_dir

    def clean(self):
        cleaned_data = super(CertParams, self).clean()
        pass1 = cleaned_data.get('password')
        pass2 = cleaned_data.get('password2')

        if pass1 and pass2:
            print pass1, pass2
            if pass1 != pass2:
                raise forms.ValidationError('Пароли не совпадают')
            else:
                from os import listdir, makedirs, chmod
                from os.path import join as joinpath
                from os.path import exists, isdir
                from subprocess import Popen, PIPE
                ca_dir = joinpath(config.CA_PATH, 'CA')
                if not exists(ca_dir):
                    makedirs(ca_dir)
                    # создаем подкаталоги для работы УЦ
                    uc_dirs = ['certs', 'crl', 'newcerts', 'private']
                    for uc_dir in uc_dirs:
                        makedirs(joinpath(ca_dir, uc_dir))
                    chmod(joinpath(ca_dir, 'private'), 0700)
                    # создаем файлы
                    serial_files = ['serial', 'crlnumber']
                    for serial_file in serial_files:
                        with open(joinpath(ca_dir, serial_file), 'w') as serialfile:
                            serialfile.write('1000')
                    with open(joinpath(ca_dir, 'index.txt'), 'w') as f:
                        pass
                    # генерируем файл со случайными данными
                    proc = Popen('dd if=/dev/random bs=1 count=32 of=' + joinpath(ca_dir, 'private', '.rand'),
                                 shell=True, stdout=PIPE, stderr=PIPE)
                    proc.stdout.readlines()
                else:
                    raise forms.ValidationError('Каталог для создания УЦ уже создан. Проверьте указанный путь.')





    def create_dir(self):
        print self.cleaned_data['capath']

        import os
        if not os.path.exists(self.cleaned_data['capath']) or os.path.isfile(self.cleaned_data['capath']):
            os.makedirs(self.cleaned_data['capath'])


class CertForm(forms.Form):
    name = forms.CharField(label=_(u'Certification Authority Name'), max_length=100)
    country = forms.ChoiceField(label=_(u'Country'), choices=countrylist)
    state = forms.CharField(label=_(u'State'), max_length='100')
    city = forms.CharField(label=_(u'City'), max_length='100')
    orgname = forms.CharField(label=_(u'Company Name'), max_length='100')
    unitname = forms.CharField(label=_(u'Organisation Unit'), max_length='100')
    email = forms.EmailField(label=_(u'E-Mail'), max_length=32)





