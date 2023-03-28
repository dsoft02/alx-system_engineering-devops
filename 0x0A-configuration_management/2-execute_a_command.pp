# using puppet to kill processes
exec { 'pkill -f killmenow':
    path     => ['/usr/bin', '/usr/sbin',],
}
