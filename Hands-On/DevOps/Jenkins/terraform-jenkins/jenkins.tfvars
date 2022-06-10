key_name                = "Mustafa_macbook_key"
ssh_key_path            = "~/.ssh/id_rsa.pub"
region                  = "us-east-1"
vpc_id                  = "vpc-f52d178f"
subnet_id               = "subnet-ed49bccc"
map_public_ip_on_launch = true

prefix        = "Mustafa-jenkins-server"
instance_type = "t2.medium"
domain        = "clarusway.us"
record        = "jenkins"
