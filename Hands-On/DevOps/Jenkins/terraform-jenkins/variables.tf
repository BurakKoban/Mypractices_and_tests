
variable "key_name" {
  type = string
}

variable "ssh_key_path" {
  type = string
}

variable "region" {
  type = string
}

variable "prefix" {
  type = string
}

variable "ami" {
  type = map(string)
  default = {
    "us-east-1" = "ami-08e4e35cccc6189f4"
    "us-east-2" = "ami-07a0844029df33d7d"
    "us-west-1" = "ami-0c7945b4c95c0481c"
  }
}
variable "instance_type" {
  type = string
}

variable "domain" {}
variable "record" {}
variable "vpc_id" {}
variable "subnet_id" {}
