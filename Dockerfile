# We're using Ubuntu 20.10
FROM vckyouuu/geezprojects:buster

#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/princesadelina/GeezProjects /home/vckyou/
RUN mkdir /home/vckyou/bin/
WORKDIR /home/vckyou/

# Upgrade pip
# RUN pip install --upgrade pip

#Install python requirements
# RUN pip3 install -r https://raw.githubusercontent.com/princesadelina/GeezProjects/master/requirements.txt

CMD ["python3","-m","userbot"]
