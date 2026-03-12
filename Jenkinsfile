pipeline {
    agent any
    environment {
        project = 'password strength check'
    }

    stages {
        stage("Install libraries") {
            steps{
                sh 'python3 -m pip install pytest'
                echo 'Libraries/Dependencies installed '
            }
        }
        stage("Testing file"){
            steps{ 
                sh 'python3 -m pytest ./test_main.py -v'
            }
        }
    }
    post {
        success {
            mail to: "${params.EMAIL}",
                subject: 'build test success',
                body: "${project} has ran successfully with no issue"
        }
        failure {
            mail to: "${params.EMAIL}",
                subject: 'build test fail',
                body: "${project} has ran to difficulties that must be amended"

        }
    }
}

