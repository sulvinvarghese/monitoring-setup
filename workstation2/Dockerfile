FROM ubuntu:20.04

# Install dependencies
RUN apt-get update &&     apt-get install -y curl apt-transport-https gnupg wget cmake make gcc g++ flex bison libpcap-dev libssl-dev python3-dev swig zlib1g-dev openjdk-11-jdk git

# Install Wazuh Agent
RUN curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | apt-key add - &&     echo "deb https://packages.wazuh.com/4.x/apt stable main" > /etc/apt/sources.list.d/wazuh.list &&     apt-get update &&     apt-get install -y wazuh-agent

# Install Zeek
RUN wget https://download.zeek.org/zeek-3.0.0.tar.gz &&     tar -xvf zeek-3.0.0.tar.gz &&     cd zeek-3.0.0 &&     ./configure && make && make install &&     cd .. && rm -rf zeek-3.0.0*

# Install Hadoop
RUN wget http://apache.mirrors.pair.com/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz &&     tar -xvf hadoop-3.2.1.tar.gz &&     mv hadoop-3.2.1 /usr/local/hadoop

# Set up Hadoop environment variables
ENV HADOOP_HOME=/usr/local/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin

# Install Spark
RUN wget http://apache.mirrors.pair.com/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz &&     tar -xvf spark-2.4.5-bin-hadoop2.7.tgz &&     mv spark-2.4.5-bin-hadoop2.7 /usr/local/spark

# Set up Spark environment variables
ENV SPARK_HOME=/usr/local/spark
ENV PATH=$PATH:$SPARK_HOME/bin

# Install Apache Spot
RUN git clone https://github.com/apache/incubator-spot.git &&     cd incubator-spot &&     ./spot-setup.sh &&     cd ..

# Copy Zeek configuration
COPY zeek/site/local.zeek /usr/local/zeek/share/zeek/site/local.zeek

# Copy simulation scripts
COPY scripts/traffic_simulation.py /opt/scripts/traffic_simulation.py

# Expose necessary ports
EXPOSE 9997 9998

# Start services
CMD service wazuh-agent start && /usr/local/zeek/bin/zeekctl deploy && python3 /opt/scripts/traffic_simulation.py && tail -f /dev/null
