# Signin to holberton and reopen file
file { 'SigninFile':
    ensure  => present,
    path    => '/etc/security/limits.conf',
    content => '#erased'
}

