#! /bin/bash
ssh google_iwantm_me@animalapp-manager  << EOF
export API_CODE=iw455756477
if [ -d "QAAnimalApp" ]; then
    cd QAAnimalApp
    git pull
else
    git clone https://github.com:iwantm/QAAnimalApp.git
    cd QAAnimalApp/
fi 
docker-compose pull
docker stack deploy --compose-file docker-compose.yaml AnimalApp
EOF
