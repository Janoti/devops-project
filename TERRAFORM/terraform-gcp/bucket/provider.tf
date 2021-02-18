provider "google" {
    project = var.project
    region = var.region
    credentials = "${file("${var.path}/service-account.json")}"
}