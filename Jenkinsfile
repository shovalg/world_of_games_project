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
            }
        }
        stage ('Finalize') {
            steps {
                bat 'docker-compose down'
                bat 'docker-compose push'
            }
        }
   }
}
// bat """cd tests
// python -c 'import e2e; e2e.main_function()'"""
