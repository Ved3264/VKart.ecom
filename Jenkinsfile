#!/usr/bin/env groovy

@Library('Django-vkart-library')_

pipeline {
    agent any
    stages {
        stage("versioning") {
            steps {
                script {
                    versioning()
                }
            }
        }
        stage("build and push image") {
            steps {
                dockerImageBuild("${env.IMG_TAG}")
                dockerLogin()
                dockerPush("${env.IMG_TAG}")
            }
        }
        stage("deploy") {
            steps {
                script {
                    deploy_ec2()
                }
            }
        }
        stage("Commit and Push Changes") {
            steps {
                script {
                    git_commit()
                }
            }
        }

        
    }
}
