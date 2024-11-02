from django import forms


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
    