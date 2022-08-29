# Author: Victor Stahlman
# Description: This is a simple python program to generate data for testing larger than 1000 rows you can make on Mockaroo
#https://faker.readthedocs.io/en/master/providers.html Link to Documentation used to call items

import sys
import csv
from faker import Faker

fake = Faker()
number_of_records = int(100000)
i = 0

#Opens up a csv in the user file for who is running it and it will run till number_of_records has been met
with open('random-person.csv','w', newline='') as file:
  file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

  file_writer.writerow(['ID',
  'First', 'Last', #Name
  'Age', #Age
  'Address','City','Country', 'Postcode', #Address
  'Company','Email','Domain',#Company
  'IP4','IP6',#IP
  'URL','Job','Description','IsDone',#RandomBis
  'StartDate','EndDate','Weekday',#Dates
  'Phone','SSN','Info', #UserInfo

    #Other
  'Balance', 'repeat', 
  'Element', 
  'Interval', 
  'Tav',
  'Other'])

  for _ in range(number_of_records):
    file_writer.writerow([ i, 
    fake.first_name(), fake.last_name(), #Name
    fake.numerify("@#"), #Age
    fake.street_address(),fake.city(), fake.country(), fake.postcode(), #Address
    fake.company(), fake.ascii_company_email(),fake.domain_name(),#Company
    fake.ipv4(),fake.ipv6(), #IP
    fake.url(),fake.job(),fake.sentence(nb_words=10),fake.boolean(chance_of_getting_true=50),#RandomBis
    fake.date(), fake.date(),fake.day_of_week(),#Dates
    fake.phone_number(),fake.ssn(),fake.user_agent(), #UserInfo

      #Other
    fake.pricetag(), fake.random_digit(),
    fake.random_element(elements=('a', 'b', 'c', 'd')),
    fake.bothify(letters='ABCDE'), 
    fake.boolean(chance_of_getting_true=70), 
    fake.random_digit_or_empty()


    ])
    i = i + 1
  