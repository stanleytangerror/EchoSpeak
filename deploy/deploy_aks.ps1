az login --tenant '7b33e762-00b4-4e51-97a0-26e09d6c78de'

# https://learn.microsoft.com/en-us/training/modules/aks-deploy-container-app/3-exercise-create-aks-cluster?tabs=linux
$RESOURCE_GROUP='rg-test-aks'
$CLUSTER_NAME='cluster-test-aks'
$LOCATION='westus'

az group create --name=$RESOURCE_GROUP --location=$LOCATION
az aks create --resource-group $RESOURCE_GROUP --name $CLUSTER_NAME --node-count 2 --generate-ssh-keys --node-vm-size Standard_B2s --network-plugin azure
az aks nodepool add --resource-group $RESOURCE_GROUP --cluster-name $CLUSTER_NAME --name userpool --node-count 2 --node-vm-size Standard_B2s

az aks get-credentials --name $CLUSTER_NAME --resource-group $RESOURCE_GROUP
kubectl get nodes

# https://learn.microsoft.com/en-us/training/modules/aks-deploy-container-app/5-exercise-deploy-app
kubectl apply -f ./deployment.yaml
kubectl get deploy contoso-website
kubectl get pods