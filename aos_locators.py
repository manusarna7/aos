from faker import Faker

fake = Faker(locale='en_CA')
aos_url = 'https://advantageonlineshopping.com/#/'
aos_login_url = 'https://advantageonlineshopping.com/#/'
aos_users_main_page = 'https://advantageonlineshopping.com/#/'

aos_dashboard_url = 'https://advantageonlineshopping.com/#/'
new_username = fake.user_name()
new_password = fake.password()
email = fake.email()
firstname = fake.first_name()
lastname = fake.last_name()
phone = fake.phone_number()
country = fake.country()
city = fake.city()
address = fake.street_address()
province = fake.province_abbr()
postal_code = fake.postalcode()

