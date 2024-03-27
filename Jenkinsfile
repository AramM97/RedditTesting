pipeline {
    agent any

    stages {
        stage('Start Selenium Hub') {
            steps {
                // Run Selenium Hub command in the background
                bat 'start /B java -jar selenium-server-4.17.0.jar hub'
            }
        }
        stage('Start Selenium Node') {
            steps {
                // Run Selenium Node command in the background
                bat 'start /B java -jar selenium-server-4.17.0.jar node --port 5555 --selenium-manager true'
            }
        }
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
                bat 'pytest test_runner.py --html=report.html'
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
