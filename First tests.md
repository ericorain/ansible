# Tests with ansible

Tests here are made with intention to evaluate ansible with network devices.

**Installation:**

>pip install ansible

**Current version**

> ansible --version

```
(project1) [eorain@centos7 ansible]$ ansible --version
ansible 2.8.0
  config file = None
  configured module search path = ['/home/eorain/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/eorain/prog/venv/project1/lib/python3.7/site-packages/ansible
  executable location = /home/eorain/prog/venv/project1/bin/ansible
  python version = 3.7.3 (default, Apr 13 2019, 17:43:27) [GCC 4.8.5 20150623 (Red Hat 4.8.5-36)]
(project1) [eorain@centos7 ansible]$
```


**Test 1: Ping**

The first test ansible documentation is about pinging devices

1. I create a file called "hosts" for 2 Cisco devices:
```
[cisco_ios]
device1 ansible_host=192.168.0.100
device2 ansible_host=192.168.0.101
```

2. I run the following command (similar to the example except that I use my personal INI file called "hosts"):
```
ansible all -i hosts -m ping
```

I got:

```
(project1) [eorain@centos7 ansible]$ ansible all -i hosts -m ping
device1 | UNREACHABLE! => {
    "changed": false,
    "msg": "Failed to connect to the host via ssh: Permission denied (publickey,keyboard-interactive,password).",
    "unreachable": true
}
device2 | UNREACHABLE! => {
    "changed": false,
    "msg": "Failed to connect to the host via ssh: Permission denied (publickey,keyboard-interactive,password).",
    "unreachable": true
}
(project1) [eorain@centos7 ansible]$
```

Well. To do a ping obviously ansible needs to do a ssh connection...

In the online documentation I found that:
> This is NOT ICMP ping, this is just a trivial test module.

3. Ok. Got it. So in order to make this non-ICMP ping I need to change the hosts file that way:
```
[cisco_ios]
device1 ansible_host=192.168.0.100 ansible_connection:ssh ansible_user=cisco ansible_password=cisco
device2 ansible_host=192.168.0.101 ansible_connection:ssh ansible_user=cisco ansible_password=cisco
```

New atempt:

```
(project1) [eorain@centos7 ansible]$ ansible all -i hosts -m ping
 [WARNING]:  * Failed to parse /home/eorain/prog/venv/project1/prog/ansible/hosts with yaml plugin: Syntax Error while
loading YAML.   expected '<document start>', but found '<scalar>'  The error appears to be in
'/home/eorain/prog/venv/project1/prog/ansible/hosts': line 2, column 1, but may be elsewhere in the file depending on
the exact syntax problem.  The offending line appears to be:  [cisco_ios] device1 ansible_host=192.168.0.100
ansible_connection:ssh ansible_user=cisco ansible_password=cisco ^ here

 [WARNING]:  * Failed to parse /home/eorain/prog/venv/project1/prog/ansible/hosts with ini plugin:
/home/eorain/prog/venv/project1/prog/ansible/hosts:2: Expected key=value host variable assignment, got:
ansible_connection:ssh

 [WARNING]: Unable to parse /home/eorain/prog/venv/project1/prog/ansible/hosts as an inventory source

 [WARNING]: No inventory was parsed, only implicit localhost is available

 [WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit localhost does not match
'all'

(project1) [eorain@centos7 ansible]$
```

Actually the sshpass needs to be installed

> sudo yum install -y sshpass

I also add a linux machine and modify the hosts file:

```
[cisco_ios]
device1 ansible_host=192.168.0.100 ansible_user=cisco ansible_password=cisco
device2 ansible_host=192.168.0.101 ansible_user=cisco ansible_password=cisco
device3 ansible_host=127.0.0.1 ansible_user=root ansible_password=root
```

4. Then I finally got that result:
```
(project1) [eorain@centos7 ansible]$ ansible all -i hosts -m ping
device3 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": false,
    "ping": "pong"
}
 [WARNING]: Unhandled error in Python interpreter discovery for host device1: unexpected output from Python interpreter
discovery

 [WARNING]: Unhandled error in Python interpreter discovery for host device2: unexpected output from Python interpreter
discovery

 [WARNING]: sftp transfer mechanism failed on [192.168.0.100]. Use ANSIBLE_DEBUG=1 to see detailed information

 [WARNING]: sftp transfer mechanism failed on [192.168.0.101]. Use ANSIBLE_DEBUG=1 to see detailed information

 [WARNING]: scp transfer mechanism failed on [192.168.0.100]. Use ANSIBLE_DEBUG=1 to see detailed information

 [WARNING]: scp transfer mechanism failed on [192.168.0.101]. Use ANSIBLE_DEBUG=1 to see detailed information

 [WARNING]: Platform unknown on host device2 is using the discovered Python interpreter at /usr/bin/python, but future
installation of another Python interpreter could change this. See
https://docs.ansible.com/ansible/2.8/reference_appendices/interpreter_discovery.html for more information.

device2 | FAILED! => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": false,
    "module_stderr": "Shared connection to 192.168.0.101 closed.\r\n",
    "module_stdout": "\r\nLine has invalid autocommand \"/bin/sh -c '/usr/bin/python '\"'\"'\"` echo Line has inva\"/AnsiballZ_ping.py'\"'\"' && sleep 0'\"",
    "msg": "MODULE FAILURE\nSee stdout/stderr for the exact error",
    "rc": 0
}
 [WARNING]: Platform unknown on host device1 is using the discovered Python interpreter at /usr/bin/python, but future
installation of another Python interpreter could change this. See
https://docs.ansible.com/ansible/2.8/reference_appendices/interpreter_discovery.html for more information.

device1 | FAILED! => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python"
    },
    "changed": false,
    "module_stderr": "Shared connection to 192.168.0.100 closed.\r\n",
    "module_stdout": "\r\nLine has invalid autocommand \"/bin/sh -c '/usr/bin/python '\"'\"'\"` echo Line has in\"/AnsiballZ_ping.py'\"'\"' && sleep 0'\"",
    "msg": "MODULE FAILURE\nSee stdout/stderr for the exact error",
    "rc": 0
}
(project1) [eorain@centos7 ansible]$
```

As a conclusion, ping works for Linux machine but not for Cisco switch.
As funny as it is ansible is doing ssh, sftp and scp but not ICMP to perform a "ping".

**Test 2: IOS show command**

All the files go in the same folder.

1. I create an ansible.cfg file:

```
[defaults]
inventory = ./hosts
host_key_checking = False
```

That file is useful since we do not need to specify the hosts file as the inventory in command line and also the is no annoying key check.

2. I create the inventory file with the devices I want to use. That inventory file is called hosts:

```
[routers]
192.168.0.100 ansible_user=cisco ansible_password=cisco
192.168.0.101 ansible_user=cisco ansible_password=cisco
```

3. I configure my ansible playbook called my_playbook.yaml:

```
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

```
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