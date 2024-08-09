#!/usr/bin/env groovy

@Library('Django-vkart-library')_

pipeline {
    agent any
    stages {
        stage("versioning") {
            steps {
                script {
                    echo 'start versioning'
                    def dockerImage = "ved1111/django-app-practise"
                    def currentVersion = "1.0.0"
                    // Split the version into major, minor, and patch parts
                    def versionParts = currentVersion.tokenize('.')
                    def major = versionParts[0].toInteger()
                    def minor = versionParts[1].toInteger()
                    def patch = versionParts[2].toInteger()

                    // Increment the patch version
                    patch += 1

                    // Create the new version
                    def newVersion = "${major}.${minor}.${patch}"

                    // Build and tag the new Docker image
                    def newImageTag = "${dockerImage}:${newVersion}"
                    echo "Building Docker image: ${newImageTag}"
                    
                    // Push the new Docker image
                    echo "Pushing Docker image: ${newImageTag}"
                    

                    // Optionally, update the version in a file or environment variable
                    echo "Updated version to: ${newVersion}"
                    echo'end versionning
                }
            }
        }
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
