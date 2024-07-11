FROM ubuntu:20.04

# Install dependencies
RUN apt-get update &&     apt-get install -y curl apt-transport-https gnupg wget openjdk-11-jdk

# Install Elasticsearch
RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.10.2-amd64.deb &&     dpkg -i elasticsearch-7.10.2-amd64.deb &&     rm elasticsearch-7.10.2-amd64.deb

# Install Logstash
RUN wget https://artifacts.elastic.co/downloads/logstash/logstash-7.10.2.deb &&     dpkg -i logstash-7.10.2.deb &&     rm logstash-7.10.2.deb

# Install Kibana
RUN wget https://artifacts.elastic.co/downloads/kibana/kibana-7.10.2-amd64.deb &&     dpkg -i kibana-7.10.2-amd64.deb &&     rm kibana-7.10.2-amd64.deb

# Install Wazuh Manager
RUN curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | apt-key add - &&     echo "deb https://packages.wazuh.com/4.x/apt stable main" > /etc/apt/sources.list.d/wazuh.list &&     apt-get update &&     apt-get install -y wazuh-manager

# Install Apache NiFi
RUN wget https://archive.apache.org/dist/nifi/1.13.2/nifi-1.13.2-bin.tar.gz &&     tar -xvf nifi-1.13.2-bin.tar.gz &&     mv nifi-1.13.2 /opt/nifi &&     rm nifi-1.13.2-bin.tar.gz

# Copy Logstash configuration
COPY logstash/pipeline/logstash.conf /etc/logstash/conf.d/logstash.conf

# Copy NiFi configuration
COPY nifi/nifi.properties /opt/nifi/conf/nifi.properties

# Expose necessary ports
EXPOSE 9200 5601 5044 1514/udp 55000 8080

# Start services
CMD service elasticsearch start && service logstash start && service kibana start && service wazuh-manager start && /opt/nifi/bin/nifi.sh start && tail -f /dev/null
