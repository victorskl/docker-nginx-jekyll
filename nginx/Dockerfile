FROM nginx:latest

# Set the timezone - Alpine
#RUN apk update && apk add tzdata
#ENV TZ=Australia/Melbourne
#RUN cp /usr/share/zoneinfo/$TZ /etc/localtime \
# && echo $TZ > /etc/timezone

# Set the timezone - Debian
ENV TZ=Australia/Melbourne
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
 && echo $TZ > /etc/timezone \
 && dpkg-reconfigure -f noninteractive tzdata

#COPY nginx.conf /etc/nginx/nginx.conf