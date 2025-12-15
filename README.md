# TPfinaleInfraCloud


RENDU:

```
gcloud projects create tp-final-gke-martin

```

```
gcloud config set project tp-final-gke-martin

```
```
gcloud services enable \
                                           container.googleapis.com \
                                           artifactregistry.googleapis.com \
                                           iam.googleapis.com \
                                           cloudresourcemanager.googleapis.com

```

Quand les fichiers terraform sont créés

```
terraform init
terraform plan
terraform apply

```