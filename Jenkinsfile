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
                dockerImageBuild 'ved1111/django-app-practise:1.3'
                dockerLogin()
                dockerPush 'ved1111/django-app-practise:1.3'
            }
        }
        stage("deploy") {
            steps {
                echo 'deploy successfully'
            }
        }
    }
}
