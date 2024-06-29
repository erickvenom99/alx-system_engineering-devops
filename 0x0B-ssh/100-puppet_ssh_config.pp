#Using puppet to login to server password
#defines class
file { 'etc/ssh/ssh_config':
# ensure file exits
  ensure => present,
}

file_line { 'Turn off passwd auth':
#specify path to modified file
  path  => 'etc/ssh/ssh_config',
# defines modified lines
  line  => 'PasswordAuthentication no',
# A regular expression to match exiting line
  match => '^#PasswordAuthentication',
}

file_line { 'Declare identify file':
#specific modified path
  path  => '/etc/ssh/ssh_config',
#modified lines
  line  => 'IdentifyFile ~/.ssh/school',
#use regular expression to existing line
  match => '^IdentifyFile',
}