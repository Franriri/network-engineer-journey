# Ansible introduction (CloudShell, no servers needed)

Ansible describes the state I want in a playbook and makes the target match it. Here the target is CloudShell itself (`localhost`).
The files were written with Claude. I ran them and explained the results.

## Install (CloudShell home has only 1 GB, so use /tmp)

```
python3 -m venv /tmp/ansible-venv
source /tmp/ansible-venv/bin/activate
pip install --no-cache-dir ansible-core
ansible --version
```

## Run

```
ansible -i inventory.ini local -m ping
ansible-playbook -i inventory.ini site.yml --syntax-check
ansible-playbook -i inventory.ini site.yml --check    # dry run, like terraform plan
ansible-playbook -i inventory.ini site.yml            # first run: changed=2
ansible-playbook -i inventory.ini site.yml            # second run: changed=0 (idempotent)
```

Edit the report file by hand, run the playbook again, and Ansible restores it (changed=1): this is how configuration drift gets corrected.

Clean up: `rm -rf ~/ansible-demo ~/ansible-demo-report.txt`
