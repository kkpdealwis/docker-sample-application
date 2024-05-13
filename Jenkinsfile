pipeline {
    agent { label 'jenkins-pi' }
    tools{
        git 'Git-Linux'
    }
    stages{
        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t sensemate-bootcamp-sample .
                '''
            }
        }
    }
}
