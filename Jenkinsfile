pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from your version control system
                git 'https://github.com/AramM97/RedditTesting'
            }
        }
        stage('Install dependencies') {
            steps {
                // Install dependencies using pip
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                // Run your Selenium tests
                sh 'python test_comment.py'
            }
        }
    }

    post {
        always {
            // Clean up steps, such as stopping services or cleaning temporary files
            sh 'rm -rf __pycache__' // Clean up Python cache files
        }
        success {
            // Actions to take if the pipeline is successful
            echo 'Tests passed successfully!'
        }
        failure {
            // Actions to take if the pipeline fails
            echo 'Tests failed!'
        }
    }
}
