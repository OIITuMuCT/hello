from django import forms
from .models import Image, File, VideoFile, AudioFile


class UserForm(forms.Form):
    name = forms.CharField(label='Имя клиента', max_length=15,
                            help_text='ФИО не более 15 символов')
    age = forms.IntegerField(label='Возраст клиента')
    ling = forms.ChoiceField(label="Выберите язык",choices=((1, "English"), (2, "Germany"), (3, "French")))
    date = forms.DateField(label="Введите дату",widget=forms.DateInput(attrs={"type": "date"}))
    date_time = forms.DateTimeField(label="Введите дату и время")
    vyb = forms.NullBooleanField(label="Вы поедете в Сочи этим летом?")
    email = forms.EmailField(label="Электронный адрес",help_text="Обязательный символ - @")
    file = forms.FileField(label="Файл")
    file_path = forms.FilePathField(label="Выберите файл", path="/home/neko/Documents", allow_files="True", allow_folders="True")
    num = forms.FloatField(label="Введите число")
    ip_adres = forms.GenericIPAddressField(label=" Enter Ip address", help_text="Example 127.0.0.1")
    num_json = forms.JSONField(label="Данные формата JSON")
    country = forms.MultipleChoiceField(label="Выберите страны", choices=((1, "Aнглия"), (2, "Германия"), (3, "Испания"), (4, "Россия")))
    city = forms.TypedChoiceField(label="Choice city", empty_value=None, choices=((1, "Moscow"), (2, "London"), (3, "Paris")))
    city_multiple = forms.TypedMultipleChoiceField(label="Выберите город", empty_value=None, choices=((1, "Москва"),
                                                                                                      (2, "Воронеж"),
                                                                                                      (3, "Курск"),
                                                                                                      (4, "Томск")))
    combo_text = forms.ComboField(label="Введите данные комбофилд",fields=[forms.CharField(max_length=20), forms.EmailField()])
    combo_multi_text = forms.MultiValueField(label="комплескное поле", fields=(
        forms.CharField(max_length=20), forms.EmailField()
    ))


class UserWForm(forms.Form):
    name = forms.CharField(label="Имя клиента:", widget=forms.TextInput(attrs={"class": "myfield"}))
    age = forms.IntegerField(label="Возраст клиента:", min_value=1, max_value=120, widget=forms.NumberInput(attrs={"class": "myfield"}))
    required_css_class = "field"
    error_css_class = "error"


class UserCForm(forms.Form):
    name = forms.CharField(
        label="Имя клиента:", help_text="ФИО клиента", widget=forms.TextInput(attrs={"class": "myfield"})
    )
    age = forms.IntegerField(
        label="Возраст клиента:",
        min_value=1,
        max_value=120,
        widget=forms.NumberInput(attrs={"class": "myfield"}),
    )

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields ="__all__"
        # fields = {'title', 'image'}

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = "__all__"

class VideoForm(forms.ModelForm):
    class Meta:
        model = VideoFile
        fields = "__all__"


class AudioForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = "__all__"
