# 0. Strace is your friend

exec { 'fix-wordpress-error':
        command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
        provider => 'shell'
        path    => '/usr/local/bin/:/bin/'
}
