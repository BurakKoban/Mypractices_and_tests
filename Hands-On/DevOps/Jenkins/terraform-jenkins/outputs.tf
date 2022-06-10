output "instance_ip_addr" {
  value = aws_instance.web.public_ip
}

output "jenkins_website" {
  value = "${aws_route53_record.jenkins.name}:8080"
}



