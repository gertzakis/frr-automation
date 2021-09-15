from paramiko import SSHClient
from time import sleep

hostname = "10.25.103.149"
username = "root"
password = "eve@123"

# commands_list = [
#     "cat /etc/frr/frr.conf", 
#     "systemctl status frr.service"
# ]

with open("configs/router-04.cfg") as f:
    configuration = f.read()

with SSHClient() as ssh_client:
    ssh_client.load_system_host_keys()
    ssh_client.connect(hostname=hostname, username=username, password=password)
    stdin, stdout, stderr = ssh_client.exec_command("cat /etc/frr/frr.conf")
    cat_cmd_output = stdout.readlines()
    ssh_client.exec_command("systemctl reload frr.service")
    sleep(1)
    stdin, stdout, stderr = ssh_client.exec_command("systemctl status frr.service")
    frr_status = stdout.readlines()

output = ""
for line in cat_cmd_output:
    output += line

frr_output = ""
for line in frr_status:
    frr_output += line

print(output)
print(frr_output)

# print(stdout.read())

