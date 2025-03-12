pipeline {
    agent any

    stages {
        stage('SCM') {
            steps {
                git branch: 'main', url: 'https://github.com/jacektl/testapp'
            }
        }

        stage('Docker Build and Push') {
            steps {
                script {
                withCredentials([[
                    $class: 'UsernamePasswordMultiBinding',
                    credentialsId: 'dockerId',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD']]) {
                    // Build the Docker image
                    sh "docker build . -t laterna:v3 -f subfolder/Dockerfile"
                    sh "docker tag laterna:v3 jtlaga/laterna:v3"
                    sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                    sh "docker push jtlaga/laterna:v3"
                    }
                }
            }
        }

        stage('Run Docker Locally') {
            steps {
            // Pull the Docker image from Docker Hub
            sh 'docker pull jtlaga/laterna:v3'

            // Run the Docker i ge locally
            sh 'docker run -d -p 9091:80 jtlaga/laterna:v3'
            }
        }
    }
}