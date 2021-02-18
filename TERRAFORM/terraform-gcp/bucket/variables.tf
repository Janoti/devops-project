## Variables
variable "project" {default = "devops-304915"}
variable "region" { default = "us-central1" }
variable "cluster_name" {default= "devops-project-cluster"}
variable "network" { default = "default" }
variable "subnetwork" { default = "" }
variable "ip_range_pods" { default = "" }
variable "ip_range_services" { default = "" }
variable "name" { default = "bk-devops-project-1123" }
variable "path" {default = "/home/janoti/devops-project/devops-project/TERRAFORM/terraform-gcp/credentials"}

