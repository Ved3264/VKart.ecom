#!/usr/bin/env groovy

@Library('Django-vkart-library')_

pipeline {
    agent any
    environment {
        IMAGE_TAG = ''
    }
    stages {
        stage("versioning") {
            steps {
                script {
                    def versionFile = new File('version.txt')
                    def currentVersion = versionFile.text.trim()

                    if (!currentVersion) {
                        error("Current version is not available")
                    }
                    def versionParts = currentVersion.tokenize('.')
                    def major = versionParts[0].toInteger()
                    def minor = versionParts[1].toInteger()
                    def patch = versionParts[2].toInteger()
                    // Increment the patch version
                    patch += 1
                    // Create the new version
                    def newVersion = "${major}.${minor}.${patch}"
                    // Optionally, update the version in the file
                    versionFile.text = newVersion
                    echo "Updated version to: ${newVersion} in file"
                    env.IMAGE_TAG = "ved1111/django-app-practise:${newVersion}"
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
                script {
                    if (env.IMAGE_TAG) {
                        dockerImageBuild image: env.IMAGE_TAG
                        dockerLogin()
                        dockerPush image: env.IMAGE_TAG
                    } else {
                        error("IMAGE_TAG is not defined")
                    }
                }
            }
        }
        stage("deploy") {
            steps {
                echo 'deploy successfully'
            }
        }
        stage("git update") {
            steps {
                script {
                    gitPush()
                }
            }
        }
    }
}
