FROM quay.io/centos/centos:10

RUN dnf -y install httpd mod_wsgi \
    && dnf clean all

VOLUME /var/www/html /var/log/httpd
COPY vhost.conf /etc/httpd/conf.d
COPY myapp.wsgi /var/www/html

EXPOSE 80/tcp

# /usr/sbin/httpd -D FOREGROUND
ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]