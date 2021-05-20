terraform {
  backend "azurerm" {
    resource_group_name = "SoftwirePilot_JosephFisher_ProjectExercise"
    storage_account_name = "storageaccountjosfis"
    container_name = "todoapp-container"
    key = "8O1ytbiAe65qZQZS3Sx9pDppNbJWYWSTFfklEwcVN3p0ZFbxLn4YZ5I5vv9sejmqFdrFrTDwr39xhJMabdG87Q=="
    
  }
}

provider "azurerm" {
 features {}
}
data "azurerm_resource_group" "main" {
 name = "SoftwirePilot_JosephFisher_ProjectExercise"
}
resource "azurerm_app_service_plan" "main" {
 name = "${var.prefix}-asp-terraform"
 location = var.location
 resource_group_name = data.azurerm_resource_group.main.name
 kind = "Linux"
 reserved = true
 sku {
  tier = "Basic"
  size = "B1"
 }
}

resource "azurerm_cosmosdb_account" "main" {
  name                = "${var.prefix}-cosmosdb-account"
  resource_group_name = data.azurerm_resource_group.main.name
  location            = var.location
  offer_type          = "Standard"
  kind                = "MongoDB"
  capabilities {
   name = "EnableServerless"
  } 
  capabilities {
   name = "EnableMongo"
  }
  consistency_policy {
    consistency_level       = "BoundedStaleness"
    max_interval_in_seconds = 10
    max_staleness_prefix    = 200
  }
  geo_location {
    location          = data.azurerm_resource_group.main.location
    failover_priority = 0
  }
}
resource "azurerm_cosmosdb_mongo_database" "main" {
 name = "${var.prefix}-cosmos-mongo-db"
 resource_group_name = data.azurerm_resource_group.main.name
 account_name = azurerm_cosmosdb_account.main.name

 #lifecycle {
  #prevent_destroy = true
 #}
} 
resource "azurerm_app_service" "main" {
 name = "${var.prefix}-terraform"
 location = var.location
 resource_group_name = data.azurerm_resource_group.main.name
 app_service_plan_id = azurerm_app_service_plan.main.id
 site_config {
  app_command_line = ""
  linux_fx_version = "DOCKER|joefish29/todo-app:latest"
 }
 app_settings = {
  "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io/v1"
  "clientId" = var.clientId
  "client_secret" = var.client_secret
  "FLASK_APP" = "app"
  "FLASK_ENV" = "developement"
  "LOAD_DISABLED" = ""
  "SECRET_KEY" = "real_key"
  "Mongo_db" = "todo_db"
  "Mongo_Url" = "mongodb://${azurerm_cosmosdb_account.main.name}:${azurerm_cosmosdb_account.main.primary_key}@${azurerm_cosmosdb_account.main.name}.mongo.cosmos.azure.com:10255/DefaultDatabase?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000"
 }
 
}
