**Create EMR Cluster using key pair on aws

**Conect to Master instance using command: chmod 400 key-file-name.pem ssh -i "key-file-name.pem" hadoop@master-public-dns

**Install following on Master EC2 instance
: sudo pip install --upgrade pip  
pip install wheel 
sudo yum install python3 
pip install pyspark
 pip install findspark 
pip install findspark 
sudo yum install -y docker 
**Write python code to read dataset and calculate F1 score and give filename as 
--> file-name.py. Run the python code using command python3 filename.py

**start docker using command: sudo service docker start

**Build docker on EC2 instance and create docker image using command
: sudo docker build . -f docker-file-name -t image-name

**Build docker using command

: sudo docker build . -f docker-file-name -t image-name

**Run docker image using command: sudo docker run image-name

**Create image in docker hub account using command
: sudo docker build . -f docker-id-file -t docker-hub-id/image-name-on-docker-hub

**Login to Docker hub account using following command and enter password

: sudo docker login -u docker-hub-account-id/docker-id

**Push files to docker using command
: sudo docker push docker-account-id/docker-image-name

**Run the image of the Docker within the Docker Hub on EC2 Instance
 sudo docker run -t docker-hub-account-id/docker-image-name