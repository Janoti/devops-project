provider "google" {
    project = var.project
    region = var.region
    credentials = "service-account.json"
}