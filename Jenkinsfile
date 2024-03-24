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
        always {
            bat 'rmdir /s /q __pycache__ 2>nul' // Clean up Python cache files for Windows machine

        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
