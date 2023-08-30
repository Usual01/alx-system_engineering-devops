# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => "
    server {
      listen 80 default_server;
      server_name _;

      location / {
        return 301 https://teosa.tech/;
      }

      location /redirect_me {
        return 301 https://www.alxafrica.com/;
      }

      location = / {
        return 200 'Hello World!';
      }
    }
  ",
  require => Package['nginx'],
}

# Enable the default site
file { '/etc/nginx/sites-enabled/default':
  ensure  => 'link',
  target  => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
}

# Restart Nginx service
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
