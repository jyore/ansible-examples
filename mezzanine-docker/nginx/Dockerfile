#
# Container for deploying an nginx service
#

FROM nginx:1.7

RUN rm -f /etc/nginx/conf.d.default.conf /etc/nginx/conf.d/example_ssl.conf

COPY nginx.conf /etc/nginx/conf.d/mezzanine.conf
