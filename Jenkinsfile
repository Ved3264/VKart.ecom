#!/usr/bin/env groovy

@Library('Django-vkart-library')_

pipeline {
    agent any
    stages {
        stage("test") {
            steps {
                echo "test success"
            }
        }
        stage("build and push image") {
            steps {
                dockerImageBuild 'django-app-practise:1.3'
                dockerLogin()
                dockerPush 'django-app-practise:1.3'
            }
        }
        stage("deploy") {
            steps {
                echo 'deploy successfully'
            }
        }
    }
}
