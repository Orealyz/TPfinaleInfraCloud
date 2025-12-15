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

```
gcloud iam service-accounts create github-actions-sa \
        --display-name "GitHub Actions Service Account"

gcloud projects add-iam-policy-binding tp-final-gke-martin \
        --member="serviceAccount:github-actions-sa@tp-final-gke-martin.iam.gserviceaccount.com" \
        --role="roles/container.admin"

gcloud projects add-iam-policy-binding tp-final-gke-martin \
        --member="serviceAccount:github-actions-sa@tp-final-gke-martin.iam.gserviceaccount.com" \
        --role="roles/storage.admin"

gcloud projects add-iam-policy-binding tp-final-gke-martin \
        --member="serviceAccount:github-actions-sa@tp-final-gke-martin.iam.gserviceaccount.com" \
        --role="roles/iam.serviceAccountUser"

gcloud iam service-accounts keys create github-actions-sa-key.json \
        --iam-account=github-actions-sa@tp-final-gke-martin.iam.gserviceaccount.com

```


une fois push et la ci-cd passé 

```
gcloud container clusters get-credentials gke-autopilot --region europe-west1


```

Récupérer l'ip:
```
kubectl get svc my-app-service

NAME             TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)        AGE
my-app-service   LoadBalancer   34.118.226.13   104.155.44.246   80:32336/TCP   5m21s

```

```
curl http://104.155.44.246

Hello la team :)⏎                        
```