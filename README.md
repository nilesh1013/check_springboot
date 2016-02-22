check_springboot
===================

An [Spring Boot] availability and performance monitoring plugin for 
Nagios.

[Spring Boot]: http://projects.spring.io/spring-boot/


How it works
------------

This plugin works by submitting API requests to a local or remote 
Spring Boot server. This plugin calls spring boot health API
and check the status is UP or not.


Installation
------------
You might need to run this command as root (depends on your permission settings)

`pip install git+https://github.com/nilesh1013/check_springboot.git`

Usage:
-----
```
check_elasticsearch [options]

Options:
  -h, --help            show this help message and exit
  --host=HOST           Hostname or network address to probe. The
                        Spring Boot Service should be listening here.
  --port=PORT  			TCP port to probe. Spring Boot API should be
                        listening here.

```

Requirements
------------

- Python 2.6, 2.7, 3.0, 3.2 3.3, 3.4
[requests][]

[requests]: https://github.com/kennethreitz/requests
