def user_data(name, surname, byear, city, e_mail, tel):
    user_info = {'имя': name, 'фамилия': surname, 'год рождения': byear, 'город проживания': city, 'e-mail': e_mail,
                 'телефон': tel}
    return user_info


print(user_data('Иван', 'Иванов', 1992, 'Москва', 'ivan_ivanov@mail.ru', '8(999)888-77-66'))