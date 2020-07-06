provider "kubernetes" {
}

terraform {
  backend "local" {
    path = "/mnt/SSD/_terraform_states/deploy_metrics.tfstate"
  }
}

resource "kubernetes_namespace" "deploy-metrics" {
  metadata {
    name = "deploy-metrics"
  }
}