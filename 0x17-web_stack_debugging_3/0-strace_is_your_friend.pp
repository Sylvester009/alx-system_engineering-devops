# 0. Strace is your friend

exec { 'fix-apache':
        command  => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
        provider => 'shell'
}
