provider "google" {
  project = var.project_id
  region  = var.region
}
module "gke" {
  source          = "./gke.tf"
  cluster_name    = var.cluster_name
  location        = var.region
  node_count      = var.node_count
}

module "registry" {
  source        = "./registry.tf"
  project_id    = var.project_id
  registry_name = var.registry_name
}

module "iam" {
  source       = "./iam.tf"
  project_id   = var.project_id
  service_accounts = var.service_accounts
}