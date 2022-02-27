#!/usr/bin/env python
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

# Importing modules
from pandevice import firewall
import sys
import re

if __name__ == '__main__':

  try:

    # Defining user credentials and firewalls.
    USERNAME      = "USERNAME_HERE"
    PASSWORD      = "PASSWORD_HERE"
    FIREWALLS     = [["FW01_HOSTNAME","FW01_IP"], 
                     ["FW02_HOSTNAME","FW02_IP"]]

    # Operational Command
    command             = "show system info"

    # Defining filters to apply.
    model_filter        = "<model>(.*)</model>"
    version_filter      = "<sw-version>(.*)</sw-version>"

    # Creating firewall object and then executing command on object. 
    for FIREWALL_NAME, FIREWALL_IP in FIREWALLS:
      pan_fw_connect   = firewall.Firewall(hostname=FIREWALL_IP, api_username=USERNAME, api_password=PASSWORD)
      system_info      = pan_fw_connect.op(cmd=command, xml=True)

      #un-comment the line below to ignore filters and to see the full 'Show System Info' ouput
      #print(system_info)

      #Applying filters.
      model            = re.search(model_filter,str(system_info))
      system_version   = re.search(version_filter,str(system_info))

      #Displaying results.
      print(FIREWALL_NAME+" - model: "+model.group(1)+" - version: "+system_version.group(1))

  except:
    # Error message then exit.
    print("ERROR  : Unable to connect to "+FIREWALL_IP+". Check the Firewall IP address and API User Credentials.")
    sys.exit(0)	
