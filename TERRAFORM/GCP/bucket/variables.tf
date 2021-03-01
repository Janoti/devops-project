## Variables
variable "project" {default = "devops-306215"}
variable "region" { default = "us-central1" }
variable "cluster_name" {default= "devops-project-cluster"}
variable "network" { default = "default" }
variable "subnetwork" { default = "" }
variable "ip_range_pods" { default = "" }
variable "ip_range_services" { default = "" }
variable "name" { default = "bk-devops-project-112344" }

variable "path" {default = "/home/janoti/devops-project/devops-project/TERRAFORM/terraform-gcp/credentials"}

