variable "prefix" {
 description = "The prefix used for all resources in this environment"
}
variable "location" {
 description = "The Azure location where all resources in this deployment should be created"
}
variable "clientId" {
 description = "The Github client Id env variable"
}

variable "client_secret" {
 description = "The Gihub OAuth app secret"
}

variable "access_key" {
  description = "Storage account access key"
}