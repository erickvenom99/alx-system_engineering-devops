# reconfigure nginx
file { 'fix-nginx':
    ensure  => present,
    path    => '/etc/default/nginx',
    content => 'ULIMIT="-n 4096"',
}

service { 'nginx':
    ensure    => running,
    subscribe => File['/etc/default/nginx']
}

