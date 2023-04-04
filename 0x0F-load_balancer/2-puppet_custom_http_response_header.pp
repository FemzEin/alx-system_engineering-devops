# Install Nginx and configure custom HTTP header response
class nginx {
  package { 'nginx':
    ensure => installed,
  }
  $encoded_hostname = URI.encode_www_form_component($facts['networking']['hostname'])
  file { '/etc/nginx/conf.d/custom_headers.conf':
    ensure  => file,
    content => "add_header X-Served-By ${encoded_hostname};",
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
