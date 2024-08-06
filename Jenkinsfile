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
                    sh 'docker build -t ved1111/django-app-practise:1.1 .'
                    sh 'docker scout cves ved1111/django-app-practise:1.1'
                    sh 'docker login -u $USER -p $PASS'
                    sh 'docker push ved1111/django-app-practise:1.1'
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
