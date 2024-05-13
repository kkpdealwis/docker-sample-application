pipeline {
    agent { label 'jenkins-pi' }
    stages{
        stage('Build Docker Image') {
            steps {
                sh '''
                    whoami
                    docker build -t sensemate-bootcamp-sample .
                '''
            }
        }
    }
}
