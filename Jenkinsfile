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
                  if (isUnix()) {
                    sh "docker-compose build -d"
                  }
                  else {
                    bat "docker-compose build -d"
                  }
            }
        }
        stage ('Run') {
            steps {
                sh 'hostname'
            }
        }
        stage ('Test') {
            steps {
                sh 'hostname'
            }
        }
        stage ('Finalize') {
            steps {
                sh 'hostname'
            }
        }
    }
}
