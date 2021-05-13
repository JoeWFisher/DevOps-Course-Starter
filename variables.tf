variable "prefix" {
 description = "The prefix used for all resources in this environment"
}
variable "location" {
 description = "The Azure location where all resources in this deployment should be created"
 default = "uksouth"
}
variable "clientId" {
 description = "The Github client Id env variable"
 default     = "b2aeabde28d46d2b4551"
}

variable "client_secret" {
 description = "The Gihub OAuth app secret"
 default = "1cecb9eeff3882645d3c64c79c56a66e6cc190fd"
}