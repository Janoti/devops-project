resource "google_storage_bucket" "bucket" {
  count = 1
  name = var.name
  location = var.region
  storage_class = "REGIONAL"
  project = var.project




versioning { enabled = true}

}