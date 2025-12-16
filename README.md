# TPfinaleInfraCloud


## RENDU:
### Init 
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

Quand les fichiers terraform sont créés, lancer les commandes suivantes:

```
terraform init
terraform plan
terraform apply

```

Créer les comptes de services
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

Une fois push et la pipeline passée

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

Maintenant passage en https:

La pipeline le fait automatiquement, il faut simplement récupérer l'IP de l'Ingress, et mettre un enregistrement de type A sur cette IP, ensuite le certificat va se générer automatiquement.

```
curl https://orealyz.fr/
Hello la team :)⏎     
```


HTTP est maintenant bloquer, on peut passer que par HTTPS.


# Partie DB:

```
gcloud sql instances create my-app-db \
                                                 --database-version=POSTGRES_15 \
                                                 --region=europe-west1 \
                                                 --tier=db-g1-small


```

```
gcloud sql databases create myapp --instance=my-app-db

                                       gcloud sql users create myuser \
                                             --instance=my-app-db \
                                             --password=STRONG_PASSWORD

```

```
gcloud projects add-iam-policy-binding tp-final-gke-martin \
                                                   --member="serviceAccount:683176688160-compute@developer.gserviceaccount.com" \
                                                   --role="roles/cloudsql.client"

```


```
gcloud projects add-iam-policy-binding tp-final-gke-martin \
                                               --member="serviceAccount:github-actions-sa@tp-final-gke-martin.iam.gserviceaccount.com" \
                                               --role="roles/cloudsql.client"

```