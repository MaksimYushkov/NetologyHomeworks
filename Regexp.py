import csv
from itertools import chain
import re


def wr_by_columns(contacts):  #Разбить ФИО по столбцам если необходимо
    for el in contacts[1:]:
        data = ' '.join(el[:3])
        new_data = data.split()
        i = 0
        while i < len(new_data):
            el[i] = new_data[i]
            i += 1
    return contacts_list


def deduplicate(contacts): #Дублируемые строки соединить в одну
    new_list = []
    for data in contacts:
        if data[0] and data[1] not in list(chain(*new_list)):
            new_list.append(data)
        else:
            for id, el in enumerate(new_list):
                if el[0] == data[0] and el[1] == data[1]:
                    i = 0
                    for el_ in el:
                        if el_ == '':
                            el[i] = data[i]
                        i += 1
                new_list[id] = el
    return new_list


def phones_normalize(contacts): #Привести номера телефонов к единому виду
    new_contacts = []
    for el in contacts[1:]:
        new_contacts.append(el[5])
    for id, contact in enumerate(new_contacts):
        pattern = r"((8|\+7))[-\s*]?[-\s*]?\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})\s*\(?(\w+\.)?\s*(\d+)" \
                  r"?\)?"
        new_contact = re.sub(pattern, r"+7(\3)\4-\5-\6 \7 \8", contact)
        new_contacts[id] = new_contact.strip(' ')
    i = 0
    for el in contacts[1:]:
        el[5] = new_contacts[i]
        i += 1
    return contacts


if __name__ == '__main__':

    with open("phonebook_raw.csv", encoding='utf-8', newline='') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    new_contacts_list = deduplicate(wr_by_columns(contacts_list))
    phones_normalize(new_contacts_list)

    with open("phonebook.csv", "w", encoding='utf-8', newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts_list)




