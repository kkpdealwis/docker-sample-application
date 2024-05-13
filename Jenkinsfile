pipeline {
    agent { label 'jenkins-pi' }

    stages{
        stage('Build Docker Image') {
            step{
                sh '''
                    docker build -t sensemate-bootcamp-sample .
                '''
            }
        }
    }
}
