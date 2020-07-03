provider "kubernetes" {
}

resource "kubernetes_namespace" "deploy-metrics" {
  metadata {
    name = "deploy-metrics"
  }
}