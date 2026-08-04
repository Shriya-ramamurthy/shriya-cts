gcloud auth login

gcloud config set project YOUR_PROJECT_ID

gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/myapp

gcloud run deploy myapp \
--image gcr.io/YOUR_PROJECT_ID/myapp \
--platform managed \
--allow-unauthenticated
sh cloudrun.sh