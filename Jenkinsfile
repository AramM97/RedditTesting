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
                sh 'pwd'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run tests') {
            steps {
                // Run your Selenium tests using python directly
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
