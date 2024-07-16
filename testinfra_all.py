import pytest

def host(testinfra_hosts):
    return testinfra_hosts.get("localhost") 

def test_nginx_installed(host):
    """Check if Nginx is installed."""
    assert host.package("nginx").is_installed

def test_certbot_installed(host):
    """Check if Certbot is installed."""
    assert host.package("certbot").is_installed

def test_python3_certbot_nginx_installed(host):
    """Check if python3-certbot-nginx is installed."""
    assert host.package("python3-certbot-nginx").is_installed

def test_nginx_config_exists(host):
    """Check if Nginx site configuration exists."""
    assert host.file("/etc/nginx/sites-available/site.conf").exists

def test_nginx_config_owner(host):
    """Check if Nginx site configuration has correct owner."""
    assert host.file("/etc/nginx/sites-available/site.conf").user == "root"

def test_nginx_config_group(host):
    """Check if Nginx site configuration has correct group."""
    assert host.file("/etc/nginx/sites-available/site.conf").group == "root"

def test_nginx_config_mode(host):
    """Check if Nginx site configuration has correct permissions."""
    assert host.file("/etc/nginx/sites-available/site.conf").mode == 0o644



def test_nginx_service_running(host):
    """Check if Nginx service is running."""
    assert host.service("nginx").is_running

def test_nginx_service_enabled(host):
    """Check if Nginx service is enabled."""
    assert host.service("nginx").is_enabled



def test_site_content_exists(host):
    """Check if site content exists."""
    assert host.file("/var/www/html/index.html").exists

def test_site_content_owner(host):
    """Check if site content has correct owner."""
    assert host.file("/var/www/html/index.html").user == "www-data"

def test_site_content_group(host):
    """Check if site content has correct group."""
    assert host.file("/var/www/html/index.html").group == "www-data"

def test_site_content_mode(host):
    """Check if site content has correct permissions."""
    assert host.file("/var/www/html/index.html").mode == 0o755

def test_user_exists(host):
    """Check if the user exists."""
    assert host.user("user").exists

def test_user_home_directory_exists(host):
    """Check if the user's home directory exists."""
    assert host.file("/home/user").exists

def test_user_home_directory_owner(host):
    """Check if the user's home directory has correct owner."""
    assert host.file("/home/user").user == "user"

def test_user_home_directory_group(host):
    """Check if the user's home directory has correct group."""
    assert host.file("/home/user").group == "www-data"

def test_user_home_directory_mode(host):
    """Check if the user's home directory has correct permissions."""
    assert host.file("/home/user").mode == 0o750


