#!/usr/bin/python
#

DOCUMENTATION = '''
---
module: ovm_vm
short_description: This module manages Virtual Machines inside Oracle-VM
description:
  - Module to manage Virtual Machine definitions inside Oracle-VM
author: "Stephan Arts, @stephanarts"
notes:
    - This module is tested with OVM 3.3 and 3.4
requirements:
    - requests package
options:
    name:
        description:
            - The virtual-machine name, inside oracle-vm the vm-name is
            - not unique. It uses the vm-id as the unique identifier.
            - However, since this is not very useful for us mortals,
            - this module treats the vm-name as a unique identifier and
            - will return an error if two VMs have the same name.
        required: True
'''

EXAMPLES = '''
- action: ovm_vm name='example_host'
'''

RETURN = '''
name:
  description:
    - The virtual-machine name, inside oracle-vm the vm-name is
    - not unique. It uses the vm-id as the unique identifier.
    - However, since this is not very useful for us mortals,
    - this module treats the vm-name as a unique identifier and
    - will return an error if two VMs have the same name.
id:
  description:
    - The virtual-machine id, inside oracle-vm the vm id is
    - the unique identifier. This is the Id used when referencing
    - the vm from other resources.
'''

def main():
    module = AnsibleModule(
        argument_spec = dict(
            state = dict(default='present',
                             choices=['present', 'absent']),
            name = dict(required=True),
        )
    )

    module.exit_json(changed=False)


from ansible.module_utils.basic import AnsibleModule
if __name__ == '__main__':
    main()
