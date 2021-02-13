## Variables
variable "project" {default = "devops-304700"}
variable "region" { default = "us-central1" }
variable "cluster_name" {default= "devops-project-cluster"}
variable "network" { default = "default" }
variable "subnetwork" { default = "" }
variable "ip_range_pods" { default = "" }
variable "ip_range_services" { default = "" }
variable "name" { default = "bk-devops-project-123456" }
