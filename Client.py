class Client():
    country = "Russia"

    def __init__(self, first_name, last_name, patronymic,city, index, address):
        if not (type(first_name)==str and type(last_name)==str and type(city)==str and type(index) ==int and type(address) ==str) :
            print("Неверный тип данных")
            return None
        elif not(first_name.isalpha() and last_name.isalpha() and patronymic.isalpha()):
            print("В строковых данных содержаться символы")
            return None
        self.first_name, self.last_name,self.patronymic, self.city, self.index, self.address = (
            first_name, last_name,patronymic, city, index, address)
        self.years = None

        
        file = open('text.txt', 'a')
        file.write('{}|{}|{}|{}|{}|{}|{}'.format(self.first_name, self.last_name,self.patronymic, Client.country, self.city, self.index, self.address))
        file.write("\n")
        file.close()

    def get_client_info(self):
        self.client_info = {'first_name': self.first_name,
                       'second_name': self.last_name,
                       'patronymic': self.patronymic,
                       'country': Client.country,
                       'city': self.city,
                       'index': self.index,
                       'address': self.address}
        return self.client_info

    def print_client_card(self):
        print('{}: {}, {}: {}, {}: {}, {}: {}, {}: {}, {}: {}'.format("Name", self.first_name, "Last Name", self.last_name, "Country", Client.country,
                                                              "City", self.city, "Index/Postcode", self.index, "Address", self.address))
    @property
    def name(self):
        return ( self.last_name + ' ' + self.first_name[0:1] + '.' + self.patronymic[0:1]+'.')

    @property
    def location(self):
        return ('{} {} {} {}'.format(self.address, self.city, self.country, self.index))
    
    @property
    def age(self):
        return self.years
    
    @age.setter
    def age(self, new_age):
        if new_age > 0 :
            self.years = new_age
            
    @age.deleter
    def age(self):
        del self.years




def read_clients_info(file):
    """
    Функция считывает данные о клиентах из файла и выводит в виде таблицы.
    Входные данные - имя файла.
    """
    print('|{:<15}|{:<20}|{:<20}|{:<13}|{:<25}|{:<8}|{:<25}|'.format("Name","Last Name","Patronymic","Country","City","Index","Address"))
    try:
        file = open(file, 'r')
        for line in file.readlines():
            l = line[:len(line)-2]
            L = l.split('|')
            print('|{:<15}|{:<20}|{:<20}|{:<13}|{:<25}|{:<8}|{:<25}|'.format(L[0],L[1],L[2],L[3],L[4],L[5],L[6]))
    except Exception as e:
        print("Файл не найден. {}".format(e))


test_client = Client('Konstatin', 'Konstantinopolskiy','Igorevich',
                         'Petropavlovsk-Kamchatsky', 683000,
                         'Vladivostokskaya, 35')
print(test_client.location)
print(test_client.name)
test_client.age = 18
print(test_client.age)
del test_client.age
#print(test_client.age)

read_clients_info("text.txt")
