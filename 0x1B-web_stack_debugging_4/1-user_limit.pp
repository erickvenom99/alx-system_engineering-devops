# Increase the hard file limit for the Holberton user
exec { 'increase-hard-file-limit-for-holberton':
    command => 'sed -i /^holberton\ hard/s/4/40000/ /etc/security/limits.conf',
    path    => '/usr/local/bin:/bin',
}

exec { 'increase-soft':
    command => 'sed -i /^holberton\ soft/s/5/50000/ /etc/security/limits.conf',
    path    => '/usr/local/bin:/bin',
}
