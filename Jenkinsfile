pipeline {
    agent any
    stages {
        stage("test") {
            steps {
                echo "test success"
            }
        }
        stage("build") {
            steps {
                withCredentials([usernamePassword(credentialsId: 'Ved-DockerHub', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                    echo "start build app"
                    sh 'docker build -t ved1111/django-app-practise:1.3 .'
                    sh 'docker scout cves ved1111/django-app-practise:1.3'
                    sh 'echo "$PASS" | docker login -u "$USER" --password-stdin'
                    sh 'docker push ved1111/django-app-practise:1.3'
                    echo 'build successfully'
                }
            }
        }
        stage("deploy") {
            steps {
                echo 'deploy successfully'
            }
        }
    }
}
