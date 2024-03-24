pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/AramM97/RedditTesting'
            }
        }
        stage('Read .env file') {
            steps {
                // Read .env file and set environment variables
                withCredentials([file(credentialsId: 'jenkins-env-file', variable: 'ENV_FILE')]) {
                    bat 'type %ENV_FILE%'
                    script {
                        def envFileContent = readFile(env.ENV_FILE).trim()
                        envFileContent.eachLine { line ->
                            def (key, value) = line.tokenize('=')
                            env."${key.trim()}" = value.trim()
                        }
                    }
                }
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
                bat 'python test_runner.py'
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
