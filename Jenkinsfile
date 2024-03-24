pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/AramM97/RedditTesting'
            }
        }
        stage('Install dependencies') {
            steps {
                bat 'cd'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                bat 'python test_comments.py'
            }
        }
    }

    post {
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
