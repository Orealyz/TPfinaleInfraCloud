resource "google_container_cluster" "primary" {
  name     = "gke-autopilot"
  location = var.region

  # Active le mode Autopilot (ne crée pas de node pool classique)
  enable_autopilot = true

  # Options facultatives
  network = "default"
}