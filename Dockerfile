FROM nginx:alpine

LABEL org.opencontainers.image.title="my-docker-workstation"
LABEL org.opencontainers.image.description="Week 1 custom NGINX static website docker practice"

COPY site/ /usr/share/nginx/html/

EXPOSE 80