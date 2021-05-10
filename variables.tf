variable "prefix" {
 description = "The prefix used for all resources in this environment"
}
variable "location" {
 description = "The Azure location where all resources in this deployment should be created"
 default = "uksouth"
}
variable "clientId" {
 description = "The Github client Id env variable"
 default     = "dbe8e2efaedaa929cc70"
}