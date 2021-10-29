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
                bat """cd tests
                python -c 'e2e.py'"""
//                 bat 'docker exec -it world-of-games-part4-world_of_games-1 sh -c cd tests'
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
// bat """cd tests
// python -c 'import e2e; e2e.main_function()'"""
