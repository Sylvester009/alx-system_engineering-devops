#creates a file in /tmp directory

file { "/tmp/school":
mode => '0744',
ensure => 'file',
owner => 'www-data',
group => 'www-data',
content => 'I love Puppet',
}