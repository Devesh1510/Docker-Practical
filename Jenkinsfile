pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                sh 'docker build -t sample-app .'
            }
        }

        stage('Run') {
            steps {
                sh '''
                docker stop sample-app || true
                docker rm sample-app || true
                docker run -d -p 5000:5000 --name sample-app sample-app
                '''
            }
        }
    }
}