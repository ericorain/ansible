# Using with ansible

Codes here are made to provide example of usage of ansible with network devices.

## Installation:

>pip install ansible

``` yaml
(project1) [eorain@centos7 project1]$ pip install ansible
Collecting ansible
  Downloading https://files.pythonhosted.org/packages/17/c9/d379b76ecaa42f4ee08b01c365e9ed1be0b302ff8a26eef120d481b144fa/ansible-2.8.0.tar.gz (14.3MB)
     |¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦| 14.3MB 10.9MB/s
Requirement already satisfied: jinja2 in ./lib/python3.7/site-packages (from ansible) (2.10.1)
Requirement already satisfied: PyYAML in ./lib/python3.7/site-packages (from ansible) (5.1)
Requirement already satisfied: cryptography in ./lib/python3.7/site-packages (from ansible) (2.6.1)
Requirement already satisfied: MarkupSafe>=0.23 in ./lib/python3.7/site-packages (from jinja2->ansible) (1.1.1)
Requirement already satisfied: asn1crypto>=0.21.0 in ./lib/python3.7/site-packages (from cryptography->ansible) (0.24.0)
Requirement already satisfied: cffi!=1.11.3,>=1.8 in ./lib/python3.7/site-packages (from cryptography->ansible) (1.12.3)
Requirement already satisfied: six>=1.4.1 in ./lib/python3.7/site-packages (from cryptography->ansible) (1.12.0)
Requirement already satisfied: pycparser in ./lib/python3.7/site-packages (from cffi!=1.11.3,>=1.8->cryptography->ansible) (2.19)
Building wheels for collected packages: ansible
  Building wheel for ansible (setup.py) ... done
  Stored in directory: /home/eorain/.cache/pip/wheels/31/ab/70/df86c93df35db7378d7bf40e30e1f2b0c43fb179cda1d940b3
Successfully built ansible
Installing collected packages: ansible
Successfully installed ansible-2.8.0
(project1) [eorain@centos7 project1]$
```

## Getting current version

The command to get the current version of ansible is:

> ansible --version

``` yaml
(project1) [eorain@centos7 ansible]$ ansible --version
ansible 2.8.0
  config file = None
  configured module search path = ['/home/eorain/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/eorain/prog/venv/project1/lib/python3.7/site-packages/ansible
  executable location = /home/eorain/prog/venv/project1/bin/ansible
  python version = 3.7.3 (default, Apr 13 2019, 17:43:27) [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
(project1) [eorain@centos7 ansible]$
```

## Code 1: IOS show command

The following code is demonstrating the use of a simple show command on a group of Cisco IOS devices with ansible.

All the files are located inside the same folder (whatever folder you want).

1. I create an ansible.cfg file.

<span style="color:MediumSeaGreen">**ansible.cfg**</span>:
``` ini
[defaults]
inventory = ./hosts
host_key_checking = False
```

That file is useful since we do not need to specify the hosts file as the inventory in command line and also the is no annoying key check.

2. I create the inventory file with the devices I want to use. That inventory file is called hosts.

<span style="color:MediumSeaGreen">**hosts**</span>:
``` ini
[routers]
192.168.0.100 ansible_user=cisco ansible_password=cisco
192.168.0.101 ansible_user=cisco ansible_password=cisco
```

3. I configure my ansible playbook called my_playbook.yaml.

<span style="color:MediumSeaGreen">**my_playbook.yaml**</span>:

``` yaml
---
- name: Running something
  hosts: routers
  gather_facts: False
  connection: local
  tasks:
   - name: My Task
     ios_command:
         commands: show ip int brief
     register: output
   - name: Display task
     debug: msg="{{ output.stdout_lines }}"
```

4. Finally I run the playbook made:

> ansible-playbook my_playbook.yaml

And here is the result:

``` yaml
(project1) [eorain@centos7 ansible_cisco_ios_show_int_des]$ time ansible-playbook my_playbook.yaml

PLAY [Running something] ********************************************************************************************************************************************

TASK [My Task] ******************************************************************************************************************************************************
ok: [192.168.0.101]
ok: [192.168.0.100]

TASK [Display task] *************************************************************************************************************************************************
ok: [192.168.0.100] => {
    "msg": [
        [
            "Interface              IP-Address      OK? Method Status                Protocol",
            "FastEthernet0/0        unassigned      YES NVRAM  administratively down down    ",
            "FastEthernet1/0        unassigned      YES NVRAM  administratively down down    ",
            "Ethernet2/0            192.168.0.100   YES NVRAM  up                    up      ",
            "Ethernet2/1            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet2/2            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet2/3            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet3/0            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet3/1            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet3/2            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet3/3            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet3/4            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet3/5            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet3/6            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet3/7            unassigned      YES NVRAM  administratively down down"
        ]
    ]
}
ok: [192.168.0.101] => {
    "msg": [
        [
            "Interface              IP-Address      OK? Method Status                Protocol",
            "FastEthernet0/0        unassigned      YES NVRAM  administratively down down    ",
            "FastEthernet1/0        unassigned      YES NVRAM  administratively down down    ",
            "Ethernet2/0            192.168.0.101   YES NVRAM  up                    up      ",
            "Ethernet2/1            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet2/2            192.168.255.1   YES NVRAM  up                    up      ",
            "Ethernet2/3            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet3/0            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet3/1            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet3/2            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet3/3            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet3/4            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet3/5            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet3/6            unassigned      YES NVRAM  administratively down down    ",
            "Ethernet3/7            unassigned      YES NVRAM  administratively down down"
        ]
    ]
}

PLAY RECAP **********************************************************************************************************************************************************
192.168.0.100              : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
192.168.0.101              : ok=2    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0


real    0m11.491s
user    0m7.962s
sys     0m0.934s
(project1) [eorain@centos7 ansible_cisco_ios_show_int_des]$
```

## Code 2: IOS config command (without save)

The following code is demonstrating the use of configuration commands on a Cisco IOS device with ansible.

All the files are located inside the same folder (whatever folder you want).

Before running the code we can see that the current configuration on the Cisco device interface is the following:

``` yaml
R1#sh run int e2/1
Building configuration...

Current configuration : 57 bytes
!
interface Ethernet2/1
 no ip address
 duplex full
end

R1#
```

1. I create an ansible.cfg file.

<span style="color:MediumSeaGreen">**ansible.cfg**</span>:

``` ini
[defaults]
inventory = ./hosts
host_key_checking = False
```

2. I create the inventory file with the devices I want to use. Note that this time I use a name to refer to each devices. That inventory file is called hosts.

<span style="color:MediumSeaGreen">**hosts**</span>:

``` ini
[routers]
device1 ansible_host=192.168.0.100 ansible_user=cisco ansible_password=cisco
device2 ansible_host=192.168.0.101 ansible_user=cisco ansible_password=cisco
```

3. I configure my ansible playbook called my_playbook.yaml. This time I just deal with one device. On that device I send commands to add an IP address on an L3 interface then I enable it.

<span style="color:MediumSeaGreen">**my_playbook.yaml**</span>:

``` yaml
---
- name: Running something
  hosts: device1
  gather_facts: False
  connection: local
  tasks:
   - name: My Task
     ios_config:
         lines:
           - ip address 192.168.254.1 255.255.255.0
           - no shut
         parents:
           - interface E2/1
```


4. Finally I run the playbook made:

> ansible-playbook my_playbook.yaml

And here is the result:

``` yaml
(project1) [eorain@centos7 ansible_cisco_ios_config]$ ansible-playbook my_playbook.yaml

PLAY [Running something] ***********************************************************************************************

TASK [My Task] *********************************************************************************************************
changed: [device1]

PLAY RECAP *************************************************************************************************************
device1                    : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

(project1) [eorain@centos7 ansible_cisco_ios_config]$ time ansible-playbook my_playbook.yaml

PLAY [Running something] ***********************************************************************************************

TASK [My Task] *********************************************************************************************************
changed: [device1]

PLAY RECAP *************************************************************************************************************
device1                    : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0


real    0m12.919s
user    0m5.796s
sys     0m0.581s
(project1) [eorain@centos7 ansible_cisco_ios_config]$
```

On the Cisco device we can see the modified interface configuration:

``` yaml
R1#sh run int e2/1
Building configuration...

Current configuration : 82 bytes
!
interface Ethernet2/1
 ip address 192.168.254.1 255.255.255.0
 duplex full
end

R1#
```

## Code 3: IOS config command (with save)

The following code is demonstrating the use of configuration commands on a Cisco IOS device with ansible.

All the files are located inside the same folder (whatever folder you want).

Before running the code we can see that the current configuration on the Cisco devices is the following:

<span style="color:MediumSeaGreen">**R1**</span>:
``` yaml
R1#sh run | i loggin
R1#s
```

<span style="color:MediumSeaGreen">**R2**</span>:
``` yaml
R2#sh run | i logging
R2#
```

1. I create an ansible.cfg file.

<span style="color:MediumSeaGreen">**ansible.cfg**</span>:

``` ini
[defaults]
inventory = ./hosts
host_key_checking = False
```

2. I create the inventory file with the devices I want to use. Note that this time I use a name to refer to each devices. That inventory file is called hosts.

<span style="color:MediumSeaGreen">**hosts**</span>:

``` ini
[routers]
device1 ansible_host=192.168.0.100 ansible_user=cisco ansible_password=cisco
device2 ansible_host=192.168.0.101 ansible_user=cisco ansible_password=cisco
```

3. I configure my ansible playbook called my_playbook.yaml. I want to add a SYSLOG server on all the Cisco IOS devices and to save the configuration on the devices. The IP address of the SYSLOG server is 192.168.0.1.

<span style="color:MediumSeaGreen">**my_playbook.yaml**</span>:

``` yaml
---
- name: Running something
  hosts: routers
  gather_facts: False
  connection: local
  tasks:
   - name: My Task
     ios_config:
         lines:
           - logging 192.168.0.1
         save_when: modified
```


4. Finally I run the playbook made:

> ansible-playbook my_playbook.yaml

And here is the result:

``` yaml
(project1) [eorain@centos7 ansible_cisco_ios_config_with_save]$ time ansible-playbook my_playbook.yaml

PLAY [Running something] ***********************************************************************************************

TASK [My Task] *********************************************************************************************************
changed: [device1]
changed: [device2]

PLAY RECAP *************************************************************************************************************
device1                    : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
device2                    : ok=1    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0


real    0m24.398s
user    0m8.244s
sys     0m0.861s
(project1) [eorain@centos7 ansible_cisco_ios_config_with_save]$
```

We can see the modified configuration of the Cisco devices:

<span style="color:MediumSeaGreen">**R1**</span>:
``` yaml
R1#sh run | i logging
logging host 192.168.0.1
R1#
R1#
R1#sh conf | i logging
logging host 192.168.0.1
R1#
```

<span style="color:MediumSeaGreen">**R2**</span>:
``` yaml
R2#sh run | i logging
logging host 192.168.0.1
R2#
R2#
R2#sh conf | i logging
logging host 192.168.0.1
R2#
```