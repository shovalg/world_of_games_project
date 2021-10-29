pipeline {
    agent any
    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/shovalg/world_of_games_project.git'
            }
        }
        stage ('Build') {
           steps {
                bat "docker-compose build"
            }
        }
        stage ('Run') {
            steps {
                bat "docker-compose up -d"
            }
        }
        stage ('Test') {
            steps {
                bat 'docker exec -it world-of-games-part4-world_of_games-1 bash -c cd tests'
//                  "&& python e2e.py"
            }
        }
//         stage ('Finalize') {
//             steps {
//                 sh 'hostname'
//             }
//         }
   }
}
