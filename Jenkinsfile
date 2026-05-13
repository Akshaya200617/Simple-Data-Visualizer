pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                credentialsId: 'HariniGitID',
                url: 'https://github.com/Akshaya200617/Simple-Data-Visualizer.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t data-visualizer .'
            }
        }

        stage('Run Docker Container') {
            steps {
                docker run -d -p 5001:5000 data-visualizer
            }
        }
    }
}
