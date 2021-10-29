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
                sh "cd tests"
                sh "python e2e.py"
            }
        }
//         stage ('Finalize') {
//             steps {
//                 sh 'hostname'
//             }
//         }
   }
}
