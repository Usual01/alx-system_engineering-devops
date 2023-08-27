# this manifest changes SSH config

exec {'add_ssh_config':
command => 'echo "    IdentityFile ~/.ssh/school\n    PasswordAuthentication no" >> /etc/ssh/ssh_config',
path => 'usr/bin:/bin',
}
