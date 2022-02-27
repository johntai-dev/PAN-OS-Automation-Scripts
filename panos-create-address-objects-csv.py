#!/usr/bin/env python
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# Importing modules.
from pandevice import firewall
from pandevice import objects
import timeit
import csv
import sys

if __name__ == '__main__':

  try: 
    # Defining user credentials, firewall, and csv filepath.
    USERNAME       = "USERNAME_HERE"
    PASSWORD       = "PASSWORD_HERE"
    FIREWALL_IP    = "PAN_FW_IP_HERE"
    ADDRESS_CSV    = "CSV_FILEPATH_HERE"
    
    # Creating firewall object.
    firewall = firewall.Firewall(hostname=FIREWALL_IP, api_username=USERNAME, api_password=PASSWORD)

    # Opening csv file and reading it.
    file_      = open(RULE_CSV, 'r')
    csv_reader = csv.reader(file_)

    # Address objects table.
    address_objects = []

    for row in csv_reader:
      # row[0] is the value of address object name
      # row[1] is the value of address object IP

        address_name      = row[0]
        address_ip        = row[1] 

      # Creating an address object for each entry in the CSV file.
        address_objects.append(policies.AddressObject(name=address_name, source=address_ip))

    # Adding address object list to firewall. 
    firewall.extend(address_objects)

    # Finding similar address objects, creating objects, and commit.
    firewall.find('NAME_OF_OBJECT').create_similar()
    firewall.commit()

  except:
    # Error message then exit.
    print("ERROR   : Connecting to "+FIREWALL_IP+". Check User Credentials or Firewall IP address.")
    print("Check if the path of the "+ADDRESS_CSV+" file is correct.")
  sys.exit(0)