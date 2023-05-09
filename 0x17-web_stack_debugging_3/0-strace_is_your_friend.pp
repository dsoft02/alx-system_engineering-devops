# incorrect file name
file { '/var/www/html/wp-settings.php':
  ensure  => file,
  content => file('/var/www/html/wp-settings.php').content.gsub('class-wp-locale.phpp', 'class-wp-locale.php'),
}
