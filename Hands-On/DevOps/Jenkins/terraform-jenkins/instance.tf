
resource "aws_instance" "web" {
  #   count                  = 4
  ami                    = var.ami[var.region]
  instance_type          = var.instance_type
  vpc_security_group_ids = [aws_security_group.ec2.id]
  subnet_id              = var.subnet_id
  key_name               = var.key_name
  user_data              = <<-EOF
                 #!/bin/bash
                  sudo yum -y update
                  sudo amazon-linux-extras install java-openjdk11 -y
                  sudo amazon-linux-extras install epel -y
                  sudo wget -O /etc/yum.repos.d/jenkins.repo \
                  https://pkg.jenkins.io/redhat/jenkins.repo
                  sudo rpm --import https://pkg.jenkins.io/redhat/jenkins.io.key
                  sudo yum upgrade
                  yum install epel-release  java-11-openjdk-devel -y
                  sudo yum install jenkins -y
                  sudo systemctl daemon-reload
                  sudo systemctl start jenkins
                  sudo systemctl enable jenkins
              EOF

  root_block_device {
    volume_size           = 16
    volume_type           = "gp2"
    delete_on_termination = true
    tags = {
      Name = "Root Volume"
    }
  }

  tags = {
    Name = var.prefix
  }

}


