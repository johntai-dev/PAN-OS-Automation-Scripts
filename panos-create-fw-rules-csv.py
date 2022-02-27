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
from pandevice import policies
import timeit
import csv
import sys

if __name__ == '__main__':

  try: 
    # Defining user credentials, firewall, and csv filepath.
    USERNAME       = "USERNAME_HERE"
    PASSWORD       = "PASSWORD_HERE"
    FIREWALL_IP    = "PAN_FW_IP_HERE"
    RULE_CSV       = "CSV_FILEPATH_HERE"
    
    # Creating firewall object.
    firewall = firewall.Firewall(hostname=FIREWALL_IP, api_username=USERNAME, api_password=PASSWORD)

    # Creating rulebase container. 
    rulebase = panos.policies.Rulebase()

    # Adding rulebase container to the firewall object. 
    firewall.add(rulebase)

    # Opening csv file and reading it.
    file_      = open(RULE_CSV, 'r')
    csv_reader = csv.reader(file_)

    # Security rules table.
    security_rules = []

    for row in csv_reader:
      # row[0] is the value of rule name
      # row[1] is the value of the source zone ( any )
      # row[2] is the value of the source IP
      # row[3] is the value of destination zone ( any )
      # row[4] is the value of the destination IP
      # row[5] is the value of the application
      # row[6] is the value of the service 
      # row[7] is the value of the action

        rule_name         = row[0]
        source_zone       = row[1].split(" ")
        source_ip         = row[2].split(" ")   
        destination_zone  = row[3].split(" ")    
        destination_ip    = row[4].split(" ")    
        application       = row[5].split(" ")    
        service           = row[6].split(" ")   
        action            = row[7] 

      # Creating a security policy rule for each entry in the CSV file.
        security_rules.append(policies.SecurityRule(name=rule_name, fromzone=source_zone, source=source_ip, tozone=destination_zone,  destination=destination_ip, application=application, service=service, action=action))

    # Adding security rules list to Rulebase container. 
    rulebase.extend(security_rules)

    # Finding similar objects, creating rules, and commit.
    rulebase.find('NAME_OF_RULE').create_similar()
    firewall.commit()

  except:
    # Error message then exit.
    print("ERROR   : Connecting to "+FIREWALL_IP+". Check User Credentials or Firewall IP address.")
    print("Check if the path of the "+RULE_CSV+" file is correct.")
  sys.exit(0)
