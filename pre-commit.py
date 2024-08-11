#!/bin/python

import os

hook_path = ".git/hooks/pre-commit"
files_to_encrypt = [
    "host_vars/*",
    "roles/base/vars/credentials.yml",
]
files_to_encrypt_formated = "{}".format(' '.join(files_to_encrypt))

content = f"""#!/bin/sh
for FILE in {files_to_encrypt_formated}; do
    if ! grep -q "$ANSIBLE_VAULT;" "$FILE"; then
        echo "Encrypting $FILE..."
        ansible-vault encrypt "$FILE"
    else
        echo "File $FILE already encrypted"
    fi
done
"""

def create_pre_commit_hook():
    with open(hook_path, 'w') as f:
        f.truncate(0)
        f.write(content)
    
    os.chmod(hook_path, 0o755)

create_pre_commit_hook()

print("Pre-commit hook set up.")
