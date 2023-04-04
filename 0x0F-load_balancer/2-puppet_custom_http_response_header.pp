# Install Nginx and configure custom HTTP header response
class nginx {
  package { 'nginx':
    ensure => installed,
  }
  file { '/etc/nginx/conf.d/custom_headers.conf':
    ensure  => file,
    content => "add_header X-Served-By ${facts['networking']['hostname']};",
    notify  => Service['nginx'],
  }
  service { 'nginx':
    ensure => running,
    enable => true,
  }
}

# Apply the nginx class to the node
node 'default' {
  class { 'nginx': }
}